#!/usr/bin/env python3
import argparse
import sys
from typing import List

from utils.data_loader import load_csv_files
from report_types import ReportFactory


def parse_arguments() -> argparse.Namespace:
    """
    Парсит аргументы командной строки.

    Объект с аргументами.
    """
    parser = argparse.ArgumentParser(
        description='Генератор отчетов по макроэкономическим данным',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
            Примеры использования:
                %(prog)s --files data.csv --report average-gdp
                %(prog)s --files data1.csv data2.csv --report average-gdp
        """
    )

    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Пути к CSV файлам с данными'
    )

    parser.add_argument(
        '--report',
        required=True,
        help='Тип отчета (например: average-gdp)'
    )

    return parser.parse_args()


def main():
    """Основная функция"""
    try:
        # Парсим аргументы
        args = parse_arguments()

        # Загружаем данные
        data = load_csv_files(args.files)

        if not data:
            print("Предупреждение: Загружены пустые данные", file=sys.stderr)
            return

        # Создаем отчет
        report = ReportFactory.create_report(args.report)

        # Генерируем отчет
        report_data = report.generate(data)

        # Выводим отчет
        print(report.display(report_data))

    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
