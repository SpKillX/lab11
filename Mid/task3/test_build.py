import docker
import pytest
import time

client = docker.from_env()

def test_rust_build_and_run():
    image, _ = client.images.build(path=".", tag="rust-task3-final")
    
    container = client.containers.run("rust-task3-final", detach=True)
    
    try:
        start_time = time.time()
        success = False
        while time.time() - start_time < 10:
            logs = container.logs().decode('utf-8')
            if "Rust Service: Status OK" in logs:
                success = True
                break
            time.sleep(1)
        
        assert success, "Сервис не выдал 'Status OK' в течение 10 секунд"
    finally:
        container.stop()
        container.remove()