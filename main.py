import os
import shutil
import threading

# Функція для переміщення файлу з джерела у призначення
def move_file(src, dest):
    try:
        shutil.move(src, dest)
        print(f"Moved {src} to {dest}")
    except Exception as e:
        print(f"Error moving {src} to {dest}: {str(e)}")

# Функція для обробки папки та переміщення файлів згідно їх розширень
def process_directory(path, dest_folder):
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1]
            dest_folder_extension = os.path.join(dest_folder, file_extension)

            # Перевіряємо, чи існує папка для даного розширення, і створюємо її, якщо ні
            if not os.path.exists(dest_folder_extension):
                os.makedirs(dest_folder_extension)

            dest_path = os.path.join(dest_folder_extension, file)
            move_file(file_path, dest_path)

# Основна функція
def main():
    source_folder = "Хлам"  # Вихідна папка
    dest_folder = "Сортовано"  # Папка для сортування за розширеннями

    # Перевіряємо, чи існує папка призначення та створюємо її, якщо ні
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Створюємо та запускаємо окремий потік для обробки папки
    thread = threading.Thread(target=process_directory, args=(source_folder, dest_folder))
    thread.start()
    thread.join()  # Завершуємо потік після завершення обробки

if __name__ == "__main__":
    main()
