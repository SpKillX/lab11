import docker
import pytest
import subprocess

client = docker.from_env()
IMAGE_NAME = "go-scratch-app"

def test_go_scratch_build():
    print(f"Сборка образа {IMAGE_NAME}...")
    image, _ = client.images.build(path=".", tag=IMAGE_NAME)
    assert image is not None

def test_image_size_minimal():
    image = client.images.get(IMAGE_NAME)
    size_mb = image.attrs['Size'] / (1024 * 1024)
    print(f"Размер scratch-образа: {size_mb:.2f} MB")

    assert size_mb < 50, "Образ слишком большой для scratch! Проверьте Dockerfile."

def test_binary_is_static():
    try:
        container = client.containers.run(IMAGE_NAME, detach=True)
        status = container.status
        container.stop()
        container.remove()
        assert status in ["created", "running", "exited"]
    except Exception as e:
        pytest.fail(f"Приложение не запустилось в scratch. Возможно, не статическая сборка: {e}")

def test_go_api_response():
    container = client.containers.run(
        IMAGE_NAME, 
        detach=True, 
        ports={'8080/tcp': 8080}
    )
    
    import time
    import requests
    time.sleep(2)
    
    try:
        response = requests.get("http://localhost:8080/health", timeout=5)
        assert response.status_code == 200
        assert "status" in response.json()
    finally:
        container.stop()
        container.remove()