#!/usr/bin/env python3
"""
Скрипт для извлечения текста из PDF каталогов подшипников.

Этот скрипт предназначен для:
1. Извлечения текста из PDF каталогов производителей
2. Разбивки информации по темам (обозначения, размеры, монтаж, обслуживание)
3. Подготовки данных для интеграции в основную базу
"""

import os
import sys
from pathlib import Path

try:
    import PyPDF2
except ImportError:
    print("Требуется установка PyPDF2: pip install PyPDF2")
    sys.exit(1)


class PDFTextExtractor:
    """Класс для извлечения текста из PDF файлов."""
    
    def __init__(self, pdf_path):
        """
        Инициализация экстрактора.
        
        Args:
            pdf_path: Путь к PDF файлу
        """
        self.pdf_path = Path(pdf_path)
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF файл не найден: {pdf_path}")
    
    def extract_text(self, start_page=None, end_page=None):
        """
        Извлекает текст из PDF файла.
        
        Args:
            start_page: Начальная страница (опционально)
            end_page: Конечная страница (опционально)
            
        Returns:
            str: Извлеченный текст
        """
        text_content = []
        
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                total_pages = len(pdf_reader.pages)
                
                start = start_page if start_page is not None else 0
                end = end_page if end_page is not None else total_pages
                
                print(f"Извлечение из {self.pdf_path.name}")
                print(f"Всего страниц: {total_pages}, обработка: {start}-{end}")
                
                for page_num in range(start, min(end, total_pages)):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()
                    text_content.append(f"\n--- Страница {page_num + 1} ---\n")
                    text_content.append(text)
                    
                    if (page_num - start + 1) % 10 == 0:
                        print(f"Обработано страниц: {page_num - start + 1}")
        
        except Exception as e:
            print(f"Ошибка при извлечении текста: {e}")
            return None
        
        return ''.join(text_content)
    
    def save_extracted_text(self, output_path, start_page=None, end_page=None):
        """
        Извлекает текст и сохраняет в файл.
        
        Args:
            output_path: Путь для сохранения извлеченного текста
            start_page: Начальная страница (опционально)
            end_page: Конечная страница (опционально)
            
        Returns:
            bool: True если успешно, False иначе
        """
        text = self.extract_text(start_page, end_page)
        
        if text is None:
            return False
        
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# Извлеченный текст из {self.pdf_path.name}\n\n")
                f.write(f"**Источник**: {self.pdf_path}\n")
                f.write(f"**Дата извлечения**: {Path(__file__).stat().st_mtime}\n\n")
                f.write("---\n\n")
                f.write(text)
            
            print(f"Текст сохранен в: {output_path}")
            return True
        
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")
            return False


def main():
    """Основная функция для обработки PDF каталогов."""
    
    # Каталог с PDF файлами
    catalogs_dir = Path(__file__).parent / "catalogs"
    
    if not catalogs_dir.exists():
        print(f"Директория с каталогами не найдена: {catalogs_dir}")
        return
    
    # Список PDF файлов для обработки
    pdf_files = list(catalogs_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("PDF файлы не найдены в директории catalogs/")
        return
    
    print(f"Найдено PDF файлов: {len(pdf_files)}\n")
    
    # Создание директории для извлеченных текстов
    extracted_dir = Path(__file__).parent / "extracted_texts"
    extracted_dir.mkdir(exist_ok=True)
    
    # Обработка каждого PDF файла
    for pdf_file in pdf_files:
        print(f"\n{'='*60}")
        print(f"Обработка: {pdf_file.name}")
        print('='*60)
        
        extractor = PDFTextExtractor(pdf_file)
        output_file = extracted_dir / f"{pdf_file.stem}_extracted.txt"
        
        # Извлечение только первых 10 страниц для примера
        # Для полного извлечения удалите параметры start_page и end_page
        success = extractor.save_extracted_text(output_file, start_page=0, end_page=10)
        
        if success:
            print(f"✓ Успешно обработан: {pdf_file.name}")
        else:
            print(f"✗ Ошибка обработки: {pdf_file.name}")
    
    print(f"\n{'='*60}")
    print("Обработка завершена!")
    print(f"Результаты сохранены в: {extracted_dir}")
    print('='*60)


if __name__ == "__main__":
    main()
