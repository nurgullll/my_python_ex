def my_books(aty,sany):
    print("Какие книги ты сейчас читаешь?")
    print(f"Я сейчас читаю книгу: {aty}")
    print("Отлично ,до какой странице дочитали?")
    print(f"Я сейчас нахожусь в {sany} странице")
    print("Погнали \n")

print("1 способ")
my_books("Абай жолы", 117 )

print("2 способ")
kitap_aty = "Ұлпан"
bet_sany = 214
my_books(kitap_aty,bet_sany)

print("3 способ")
my_books(kitap_aty + " и  Абай жолы", bet_sany)

print("4-способ")
my_books(147,"Балалық шағымның аспаны.")

def my_books(*books):
    aty,sany = books
    print("Какие книги ты сейчас читаешь?")
    print(f"Я сейчас читаю книгу: {aty}")
    print("Отлично ,до какой странице дочитали?")
    print(f"Я сейчас нахожусь в {sany} странице")
    print("Погнали \n")

print("5-способ")
my_books("Кешірдім",119)

print("6 - способ")
bet_sany2 = 117
my_books("Оян қазақ!", bet_sany2)

print("7 - способ")
kitap_aty2 = "Құран кәрім"
my_books(222, kitap_aty2)

print("8-способ")
my_books(bet_sany2,kitap_aty2)

print("9 - способ")
bet_sany2 = 117
my_books("Оян қазақ!", bet_sany2 + 10)

print("7 - способ")
kitap_aty2 = "Құран кәрім"
my_books(222, kitap_aty2 + "кітабы")






    



