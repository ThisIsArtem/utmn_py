import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Ошибка выполнения команды: {command}\n{result.stderr}")
    else:
        print(f"Команда выполнена успешно: {command}\n{result.stdout}")

# Переключение на ветку prd
run_command("git checkout prd")

# Слияние изменений из ветки dev в prd
run_command("git merge dev")

# Установка тэга
tag_name = input("Введите имя тэга: ")
run_command(f"git tag {tag_name}")

# Запушить изменения и тэг в удаленный репозиторий
run_command("git push origin prd")
run_command(f"git push origin {tag_name}")

print("Ревизия успешно перенесена из dev в prd и тэг установлен.")