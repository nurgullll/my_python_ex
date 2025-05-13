people = 30
cars = 40
trucks = 15




if cars > people and trucks > cars:
   print("Поедем на машине.")
elif cars < people:
   print("He поедем на машине.")
else:
   print("Мы не можем выбрать")   

 
if trucks>cars or people<trucks:
   print("Слишком много автобусов.")
elif trucks<cars:
   print("Может,поехать на автобусе?.")
else:
   print("Мы до сих пор не можем выбрать.")   

if people>trucks:
   print("Хорошо,давайте поедем на автобусе.")
else:
   print("Прекрасно,давайте останемся дома.")   