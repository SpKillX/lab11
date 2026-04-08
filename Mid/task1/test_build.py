import docker
import pytest

client = docker.from_env()

def test_docker_image_builds():
    image, logs = client.images.build(path=".", tag="python-test-app")
    assert image is not None
    print("Образ успешно собран.")

def test_container_runs_and_responds():
    container = client.containers.run(
        "python-test-app", 
        detach=True, 
        ports={'8000/tcp': 8000}
    )
    
    try:
        import time
        import requests
        time.sleep(3)
        
        response = requests.get("http://localhost:8000/docs")
        assert response.status_code == 200
    finally:
        container.stop()
        container.remove()