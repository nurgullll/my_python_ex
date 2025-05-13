i = 0
numbers = []


def function(limit,step):
    for i in range(0,limit,step):
        print(f"В начале значение i равно {i}")
        numbers.append(i)
        print(f"Текущие значения : ", numbers)
        print(f"""В конце значение i равно {i + step}""")


print("Значения: ")

function(5,2)
for num in numbers:
    print(num)


















