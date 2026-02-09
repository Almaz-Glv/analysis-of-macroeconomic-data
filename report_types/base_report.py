from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseReport(ABC):
    """Абстрактный базовый класс для всех отчетов"""

    @abstractmethod
    def generate(self, data: List[Dict[str, Any]]) -> Any:
        """
        Генерирует отчет на основе данных

        Args:
            data: Список словарей с данными из CSV файлов

        Returns:
            Данные для формирования отчета
        """
        pass

    @abstractmethod
    def display(self, report_data: Any) -> str:
        """
        Форматирует отчет для вывода в консоль

        Args:
            report_data: Данные отчета

        Returns:
            Отформатированная строка для вывода
        """
        pass
