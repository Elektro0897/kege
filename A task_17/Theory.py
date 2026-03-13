with open('Путь до файла') as file:
    # Считывает весь файл одной строкой. Возвращает str
    data = file.read()
    # Считывает одну еще не считанную строку из файла. Возвращает str
    data1 = file.readline()
    # Считывает все строки из файла. Возвращает list[str]
    data2 = file.readlines()
