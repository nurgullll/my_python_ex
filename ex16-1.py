from sys import argv

script , filename = argv

print(f"Я собираюсь открыть файл {filename}.")

print("Открытие файла...")
target = open(filename, "r",encoding='utf-8')

print(f"{filename} файле есть эти тексты")
print(target.read())
target.close()

