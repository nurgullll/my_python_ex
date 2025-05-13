from sys import argv
script , input_file = argv

#функция құрып  оған параметр ретінде файлдың атын беріп рид арқылы оқимыз
def print_all(f):
    print(f.read())


# жаңаданфункция жасаймыз және seek қолданып файлды басынан бастап оқимыз
def rewind(f):
    f.seek(0)

# жаңа функция құрып оған екі параметр береміз
# біріншісі нешінші долда екенін санайды
# екіншісі файл
    

def print_a_line(f):
    print(f.readline())

# argv-тағы  input file ды curren_gile айнымалысы арқылы ашамыз
current_file = open(input_file,encoding='utf - 8')


print("Первым делом выведем этот файл целиоком:\n")
print_all(current_file)

print("Tenepь отмотаем назад, словно это кассета.")
rewind (current_file)

print("Выведем три строки:")
print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)