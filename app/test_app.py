import os

def test_files_exist():
    # Проверяем, что ты не забыл важные файлы
    assert os.path.exists("app.py")
    assert os.path.exists("requirements.txt")
    assert os.path.exists("Dockerfile")

def test_math():
    # Базовая проверка, что Python в контейнере адекватен
    assert 1 + 1 == 2