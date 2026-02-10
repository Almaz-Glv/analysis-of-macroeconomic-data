from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseReport(ABC):
    """Абстрактный базовый класс для всех отчетов."""

    @abstractmethod
    def generate(self, data: List[Dict[str, Any]]) -> Any:
        """
        Генерирует отчет на основе данных.

        data: Список словарей с данными из CSV файлов.

        Данные для формирования отчета.
        """
        pass

    @abstractmethod
    def display(self, report_data: Any) -> str:
        """
        Форматирует отчет для вывода в консоль.

        report_data: Данные отчета.

        Возвращает отформатированную строку для вывода.
        """
        pass
