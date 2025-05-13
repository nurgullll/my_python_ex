people = 20
cats = 30
dogs = 15


if people < cats and cats>dogs:
   print("Слишком много кошек") 
   
if cats > 10 or  dogs>10:
   print("10-нан улкен")  
if not(dogs < 10 or cats<10):
   print("ит")

if not(dogs<10 and cats<10 ):
   print("мысык")

if people <cats:
   print("Слишком много кошек! Мир обречен!")
if people > cats:
   print("He так много кошек! Мир спасен!")
if people < dogs:
   print("Мир утоп в слюнях!")
 
if people > dogs:
   print("He все так плохо!")

   dogs += 5

if people >= dogs:
   print("Людей больше или столько же, сколько собак.")
if people <= dogs:
   print("Людей меньше или столько же, сколько собак.")

if people == dogs:
   print("Людей столько же, сколько собак.")