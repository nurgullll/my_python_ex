#Бұл жерде айнымалы бермей бірден функцияны шақырған кезде мән бере аламыз
def cheese_and_crackers(cheese_count,boxes_of_cracers):
    print(f"У нас есть {cheese_count} сырков!")
    print(f"У нас есть {boxes_of_cracers}  пачек чипсов!")
    print("Этого достаточна для вечеринки!")
    print("Погнали \n")
#параметрлер арқылы
print("Мы можем непосредственно передать числа функции:")  
cheese_and_crackers(20,30)

# немесе біз жаңа айнымалы құрып оған мән береміз сосын функцияны шақырған кезде осы айнымалылар арөылы аргумент етеміз
print("ИЛИ, мы можем использовать переменные из нашего сценария:")
amount_of_cheese = 10
amount_of_cracers = 50

cheese_and_crackers(amount_of_cheese,amount_of_cracers)

#мәндерді қоса аламыз
print("Мы даже можем выполнять выисления внутри функции: ")
cheese_and_crackers(10+20,5+6)

# айнымалы мен мәнді қоса аламыз

print("И объединять переменные с вычислениями: ")
cheese_and_crackers(amount_of_cheese +100, amount_of_cracers+1000)