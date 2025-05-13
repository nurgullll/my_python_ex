from sys import argv

script , filename = argv
print(f"Я собираюсь стереть файл {filename}.")
print("Если вы не хотите стирать его,нажмите сочетание клавиш CTRL + C (^C).")
print("Если хотите стереть файлб нажмите клавишу Enter")

input("?")

print("Открытие файла ...")
target = open(filename,'w')

print("Очистка файла. До свидания!")
target.truncate()

print("Теперь я запрашиваю у вас три строки: ")
line1 = input("строка 1 : ")
line2 = input("строка 2 : ")
line3 = input("строка 3 : ")

print("Это я запишу в файл.")

target.write(f"{line1}, \n {line2} \n, {line3}")

print("И наконец , я закрою файл.")
target.close()