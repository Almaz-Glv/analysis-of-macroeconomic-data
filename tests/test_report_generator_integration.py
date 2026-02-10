import pytest
import tempfile
import os
import subprocess
import sys


def test_integration():
    """Интеграционный тест всего приложения."""
    # Создаем тестовый CSV файл
    csv_content = """country,year,gdp,gdp_growth,inflation
        United States,2020,21000,2.1,3.4
        United States,2021,22000,2.1,8.0
        Germany,2020,3800,-0.3,6.2
        Germany,2021,3900,1.8,8.7"""

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(csv_content)
        temp_file = f.name

    try:
        # Запускаем скрипт
        result = subprocess.run(
            [sys.executable, 'report_generator.py',
             '--files', temp_file,
             '--report', 'average-gdp'],
            capture_output=True,
            text=True
        )

        # Проверяем результаты
        assert result.returncode == 0
        assert 'United States' in result.stdout
        assert 'Germany' in result.stdout
        assert '21500.00' in result.stdout  # Среднее United States
        assert '3850.00' in result.stdout   # Среднее Germany

    finally:
        os.unlink(temp_file)


def test_missing_files_argument():
    """Тест запуска без обязательных аргументов."""
    result = subprocess.run(
        [sys.executable, 'report_generator.py', '--report', 'average-gdp'],
        capture_output=True,
        text=True
    )

    assert result.returncode != 0
    assert 'error' in result.stderr.lower()


def test_invalid_report():
    """Тест с неверным именем отчета."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("country,year,gdp\nUnited States,2020,1000")
        temp_file = f.name

    try:
        result = subprocess.run(
            [sys.executable, 'report_generator.py',
             '--files', temp_file,
             '--report', 'invalid-report'],
            capture_output=True,
            text=True
        )

        assert result.returncode != 0
        assert 'не найден' in result.stderr

    finally:
        os.unlink(temp_file)
