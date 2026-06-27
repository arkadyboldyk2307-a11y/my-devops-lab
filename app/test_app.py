import os

def test_files_exist():
    # Проверяем, что ты не забыл важные файлы
    assert os.path.exists("app/app.py")
    assert os.path.exists("app/requirements.txt")
    assert os.path.exists("app/Dockerfile")

def test_math():
    # Базовая проверка, что Python в контейнере адекватен
    assert 1 + 1 == 2