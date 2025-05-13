"""things = ['а','б','в','г']
print(things[1])

things[1] = 'я'
print(things)

stuff = {'имя': 'Михайл','возраст':38,'вес':6*12+2}
print(stuff['имя'])

print(stuff['возраст'])
print(stuff['вес'])
stuff['город'] = "Москва"
print(stuff['город'])
stuff["Алақай"] = "Ура"
stuff[2]= "Неа"
print(stuff["Алақай"])
print(stuff[2])
del stuff['город']
del stuff['Алақай']
del stuff[2]
print(stuff) 
"""


states={'Россия': 'RU',
        'Германия': 'DE',
        'Узбекистан': 'UZ',
        'Зимбабве': 'ZW',
        'Турция': 'TR'}

cities = {
    'UZ': 'Газли',
    'TR': 'Сарыгерме',
    'DE': 'Мюнхен'
  }

cities['ZW'] = 'Гверу'
cities['RU'] = 'Москва'

print('-'*10)
print("Встране ZW есть город: ",cities['ZW'])
print("В стране RU есть город: ",cities["RU"])

print("-"*10)
print("Аббревиатруа Турции : ",states['Турция'])
print("Аббревиатруа Германии : ",states['Германия'])

print("-"*10)
print("В Турции есть город: ",cities[states['Турция']])
print("В Германии есть город: ",cities[states['Германия']])

print('-'*10)
for state,abbrev in list(states.items()):
    print(f"{state}  имеет аббревиатуру {abbrev}")
    
print('-'*10) 
for abbrev ,city in list(cities.items()):
     print(f"B стране {abbrev} есть город {city}") 
     
print("-"*10)
for state,abbrev in list (states.items()):
    print(f"В стране {state} используется аббревиатура{abbrev}")
    print(f"и есть город {cities[abbrev]}")
    
print("-"*10)
state = states.get("США")

if not state:
    print("Прощу прощения, США не существует или уничтожено.")
    
    
city = cities.get('US','НЕ СУЩЕСТВУЕТ') 
print(f"В стране 'US' есть город: {city}")       
      
    
    
    