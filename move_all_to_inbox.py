#!/usr/bin/env python3
"""
Скрипт для перемещения всех файлов из всех директорий и архивов в inbox/.
Архивы удаляются после извлечения.
"""

import os
import shutil
import zipfile
import tarfile
import tempfile
from pathlib import Path

def extract_archive(archive_path, extract_to):
    """Извлекает архив и возвращает список извлечённых файлов."""
    extracted_files = []
    
    if zipfile.is_zipfile(archive_path):
        with zipfile.ZipFile(archive_path, 'r') as zf:
            zf.extractall(extract_to)
            extracted_files = [os.path.join(extract_to, name) for name in zf.namelist()]
    elif tarfile.is_tarfile(archive_path):
        with tarfile.open(archive_path, 'r:*') as tf:
            tf.extractall(extract_to)
            extracted_files = [os.path.join(extract_to, name) for name in tf.getnames()]
    
    return extracted_files

def collect_all_files(repo_root):
    """Рекурсивно собирает все файлы, извлекая архивы."""
    all_files = []
    archives_to_delete = []
    
    temp_dir = tempfile.mkdtemp()
    
    for root, dirs, files in os.walk(repo_root):
        # Пропускаем .git и inbox
        if '.git' in root or 'inbox' in root:
            continue;
            
        for file in files:
            file_path = os.path.join(root, file)
            
            # Если это архив - извлекаем
            if file.endswith(('.zip', '.tar', '.tar.gz', '.tgz', '.tar.bz2', '.z01', '.z02', '.z03')):
                print(f"Извлечение архива: {file_path}")
                try:
                    extracted = extract_archive(file_path, temp_dir)
                    all_files.extend(extracted)
                    archives_to_delete.append(file_path)
                except Exception as e:
                    print(f"Ошибка при извлечении {file_path}: {e}")
                    # Если не удалось извлечь, добавляем сам архив
                    all_files.append(file_path)
            else:
                all_files.append(file_path)
    
    # Рекурсивно обрабатываем извлечённые файлы
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(('.zip', '.tar', '.tar.gz', '.tgz', '.tar.bz2')):
                try:
                    extracted = extract_archive(file_path, temp_dir)
                    all_files.extend(extracted)
                except Exception as e:
                    print(f"Ошибка при извлечении вложенного архива {file_path}: {e}")
                    all_files.append(file_path)
            else:
                all_files.append(file_path)
    
    return all_files, archives_to_delete

def move_to_inbox(repo_root):
    """Перемещает все файлы в inbox/ и удаляет архивы."""
    inbox_dir = os.path.join(repo_root, 'inbox')
    os.makedirs(inbox_dir, exist_ok=True)
    
    all_files, archives = collect_all_files(repo_root)
    
    moved_count = 0
    for file_path in all_files:
        if os.path.isfile(file_path):
            file_name = os.path.basename(file_path)
            dest_path = os.path.join(inbox_dir, file_name)
            
            # Обработка дубликатов имён
            counter = 1
            base_name, ext = os.path.splitext(file_name)
            while os.path.exists(dest_path):
                dest_path = os.path.join(inbox_dir, f"{base_name}_{counter}{ext}")
                counter += 1
            
            try:
                shutil.move(file_path, dest_path)
                moved_count += 1
                print(f"Перемещён: {file_path} -> {dest_path}")
            except Exception as e:
                print(f"Ошибка перемещения {file_path}: {e}")
    
    # Удаление архивов
    for archive_path in archives:
        try:
            os.remove(archive_path)
            print(f"Удалён архив: {archive_path}")
        except Exception as e:
            print(f"Ошибка удаления архива {archive_path}: {e}")
    
    # Удаление пустых директорий
    for root, dirs, files in os.walk(repo_root, topdown=False):
        if root != inbox_dir and '.git' not in root:
            try:
                if not os.listdir(root):
                    os.rmdir(root)
                    print(f"Удалена пустая директория: {root}")
            except Exception as e:
                pass
    
    print(f"\nВсего перемещено файлов: {moved_count}")
    print(f"Удалено архивов: {len(archives)}")

if __name__ == '__main__':
    repo_root = os.getcwd()
    move_to_inbox(repo_root)