import csv
from typing import List, Dict, Any
import os


def load_csv_files(file_paths: List[str]) -> List[Dict[str, Any]]:
    """
    Загружает данные из нескольких CSV файлов.

    file_paths: Список путей к CSV файлам.

    Возвращает объединенные данные из всех файлов.
    """
    all_data = []

    for file_path in file_paths:
        # Проверяем существование файла
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        # Проверяем расширение файла
        if not file_path.lower().endswith('.csv'):
            raise ValueError(f"Файл не является CSV: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            # Преобразуем каждую строку в словарь
            file_data = [dict(row) for row in reader]
            all_data.extend(file_data)

    return all_data
