import pytest
import tempfile
import os
from utils.data_loader import load_csv_files


def test_load_csv_files():
    """Тест загрузки CSV файлов."""
    # Создаем временный CSV файл
    csv_content = """country,year,gdp
        United States,2020,21000
        United States,2021,22000
        Germany,2020,3800
        Germany,2021,3900"""

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(csv_content)
        temp_file = f.name

    try:
        # Загружаем данные
        data = load_csv_files([temp_file])

        # Проверяем результаты
        assert len(data) == 4
        assert data[0]['country'] == 'United States'
        assert data[0]['gdp'] == '21000'
        assert data[2]['country'] == 'Germany'

    finally:
        # Удаляем временный файл
        os.unlink(temp_file)


def test_load_multiple_files():
    """Тест загрузки нескольких файлов."""
    csv1_content = """country,year,gdp
        United States,2020,21000"""

    csv2_content = """country,year,gdp
        Germany,2020,3800"""

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f1:
        f1.write(csv1_content)
        temp_file1 = f1.name

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f2:
        f2.write(csv2_content)
        temp_file2 = f2.name

    try:
        data = load_csv_files([temp_file1, temp_file2])
        assert len(data) == 2

    finally:
        os.unlink(temp_file1)
        os.unlink(temp_file2)


def test_file_not_found():
    """Тест обработки отсутствующего файла."""
    with pytest.raises(FileNotFoundError):
        load_csv_files(['nonexistent.csv'])


def test_not_csv_file():
    """Тест обработки не-CSV файла."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("test")
        temp_file = f.name

    try:
        with pytest.raises(ValueError, match="не является CSV"):
            load_csv_files([temp_file])
    finally:
        os.unlink(temp_file)
