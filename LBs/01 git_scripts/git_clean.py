import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Ошибка выполнения команды: {command}\n{result.stderr}")
    else:
        print(f"Команда выполнена успешно: {command}\n{result.stdout}")

# Сброс всех изменений
run_command("git reset --hard HEAD")

# Очистка неотслеживаемых файлов и директорий
run_command("git clean -fd")

print("Репозиторий полностью очищен от изменений.")