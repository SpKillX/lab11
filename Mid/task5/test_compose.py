import subprocess
import json
import pytest

def test_network_connectivity():
    networks_cmd = subprocess.check_output(["docker", "network", "ls", "--format", "{{json .}}"])
    network_name = None
    
    for line in networks_cmd.decode().splitlines():
        net = json.loads(line)
        if "horeca-network" in net["Name"]:
            network_name = net["Name"]
            break
    
    if not network_name:
        pytest.fail("Сеть с ключевым словом 'horeca-network' не найдена. Убедитесь, что docker-compose up выполнен.")

    output = subprocess.check_output(["docker", "network", "inspect", network_name]).decode().lower()

    assert "go-app" in output
    assert "python-app" in output
    print(f"Успешно: Контейнеры найдены в сети '{network_name}'")