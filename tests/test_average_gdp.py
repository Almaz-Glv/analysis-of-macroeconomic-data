import pytest
from report_types.average_gdp import AverageGDPReport


def test_generate_average_gdp():
    """Тест расчета среднего ВВП."""
    report = AverageGDPReport()

    # Тестовые данные
    test_data = [
        {'country': 'United States', 'gdp': '21000'},
        {'country': 'United States', 'gdp': '22000'},
        {'country': 'Germany', 'gdp': '3800'},
        {'country': 'Germany', 'gdp': '3900'},
        {'country': 'Germany', 'gdp': '4000'},
        # Тест с некорректными данными
        {'country': 'France', 'gdp': 'invalid'},
        # Тест с отсутствующим полем
        {'country': 'Italy'},
    ]

    result = report.generate(test_data)

    # Проверяем результаты
    assert len(result) == 2  # Только United States и Germany
    assert result[0][0] == 'United States'  # Первая страна - United States (больший ВВП)
    assert result[0][1] == 21500.0  # (21000 + 22000) / 2

    assert result[1][0] == 'Germany'
    assert result[1][1] == 3900.0  # (3800 + 3900 + 4000) / 3


def test_display():
    """Тест форматирования отчета"""
    report = AverageGDPReport()

    report_data = [
        ('United States', 21500.0),
        ('Germany', 3900.0),
    ]

    result = report.display(report_data)

    # Проверяем, что вывод содержит нужные данные
    assert 'United States' in result
    assert '21500.00' in result
    assert 'Germany' in result
    assert '3900.00' in result
