from collections import defaultdict
from typing import List, Dict, Any, Tuple
from tabulate import tabulate # type: ignore

from report_types.base_report import BaseReport


class AverageGDPReport(BaseReport):
    """Отчет среднего ВВП по странам."""

    def generate(self, data: List[Dict[str, Any]]) -> List[Tuple[str, float]]:
        """
        Вычисляет среднее ВВП по каждой стране.

        data: Список словарей с данными.

        Список кортежей (страна, средний ВВП).
        """
        # Используем defaultdict для группировки данных по странам
        country_gdp = defaultdict(list)

        for row in data:
            country = row['country']
            try:
                # Преобразуем строку в число с плавающей точкой
                gdp = float(row['gdp'])
                country_gdp[country].append(gdp)
            except (ValueError, KeyError):
                # Пропускаем строки с некорректными данными
                continue

        # Вычисляем среднее для каждой страны
        averages = []
        for country, gdp_values in country_gdp.items():
            if gdp_values:  # Проверяем, что есть данные
                avg_gdp = sum(gdp_values) / len(gdp_values)
                averages.append((country, avg_gdp))

        # Сортируем по убыванию ВВП
        averages.sort(key=lambda x: x[1], reverse=True)

        return averages

    def display(self, report_data: List[Tuple[str, float]]) -> str:
        """
        Форматирует отчет для вывода в таблицу.

        report_data: Список кортежей (страна, средний ВВП).

        Возвращает отформатированную строку таблицы.
        """

        # Форматируем данные для tabulate
        table_data = []
        for country, avg_gdp in report_data:
            table_data.append([country, avg_gdp])

        return tabulate(
            table_data,
            headers=['Страна', 'Средний ВВП'],
            tablefmt='grid',
            floatfmt='.2f'
        )
