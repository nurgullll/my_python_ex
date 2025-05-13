from sys import argv
from os.path import exists


script , from_file , to_file = argv
in_file = open(from_file,'r+',encoding='utf-8')
print(f"Исходный файл существует?{exists(to_file)}")

out_file = open(to_file,'w',encoding='utf-8')
out_file.write(str(in_file))
print("Все прошло")





