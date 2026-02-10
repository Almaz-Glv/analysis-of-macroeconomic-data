from report_types.average_gdp import AverageGDPReport


class ReportFactory:
    """Фабрика для создания отчетов."""

    # Реестр доступных отчетов
    _reports = {
        'average-gdp': AverageGDPReport,
    }

    @classmethod
    def create_report(cls, report_name: str):
        """
        Создает экземпляр отчета по имени.

        report_name: Имя отчета.

        Возвращает экземпляр класса отчета.

        Возвращает ошибку если отчет не найден.
        """
        report_class = cls._reports.get(report_name)
        if not report_class:
            raise ValueError(f"Отчет '{report_name}' не найден. "
                             f"Доступные отчеты: \
                             {', '.join(cls._reports.keys())}")

        return report_class()

    @classmethod
    def register_report(cls, report_name: str, report_class):
        """
        Регистрирует новый тип отчета.

        report_name: Имя отчета.

        report_class: Класс отчета.
        """
        cls._reports[report_name] = report_class
