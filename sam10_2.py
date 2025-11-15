def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            if not data:
                raise ValueError("Файл пустой")
            print(data)
    except ValueError as ex:
        print(ex)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    print("Чтение из заполненного файла:")
    read_file("file.txt")

    print("Чтение из пустого файла:")
    read_file("error_file.txt")