# ЖАНУАРДЫ ТАП
aty = input("Атыңыз кім? - ")
print(f"Сәлем ,{aty}!Ойынға қош келдің!")
print("""Ол жануар үлкенбе?
      1. Иә
      2. Жоқ
      """)
ulken = int(input())
if ulken == 1:
    def ulken_zhanuar():
        y = 2
        zhanuar = " "
        print("""Ол ұшады ма?
                       1. Иә
                       2. Жоқ """)
        ushady = int(input(">"))
        print("""Ол суда өмір сүредіме?
                   1. Иә
                   2. Жоқ """)
        su = int(input(">"))
        if ushady == y and su == y:
            zhanuar = "Бегомот"
        return zhanuar
    zh = ulken_zhanuar()
    print(zh)
elif ulken == 2:
    def kishkentay_zhanuar():
        zhanuar = " "
        print("""Ол ұшады ма?
                       1. Иә
                       2. Жоқ """)
        ushady = int(input())
        print("""Ол суда өмір сүредіме?
                   1. Иә
                   2. Жоқ """)
        su = int(input())
        if ushady == 1 and su == 1:
            zhanuar = " Жоқ "
            return zhanuar
        elif ushady == 2 and su == 2:
            zhanuar = " Ит"
        return zhanuar
    zh = kishkentay_zhanuar()
    print(zh)
