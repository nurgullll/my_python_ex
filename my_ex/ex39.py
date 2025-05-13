states = { "Палестина":"PS",
          "Казахстан":"KZ",
          
          "Япония":"JP",
          "Франция":"FR",
          "Біріккен Араб Әмірліктері ":"AE"}


cities = {"PS":"Рамалла",
          "KZ":"Астана",
          "JP":"Токио",
          "FR":"Париж",
          "AE":"Дубай"}

"""print("-"*10)
print("PS мемлекетінде " + cities["PS"] + " қаласы бар.")
print("KZ мемелекетінде " + cities["KZ"] + " қаласы бар")

print("*"*10)
print("Қазақстан аббревиатурасы:",states["Казахстан"])
print("Палестина аббревиатурасы:",states["Палестина"])

print("-"*10)
print("Палестинада  бар қала: " + cities[states["Палестина"]] )
print("Қазақстанда бар қала: "+cities[states["Казахстан"]] )



print("-"*10)
for memleket, abbr in list(states.items()):
    print(f"{memleket}  мемлекетінің аббревиатруасы {abbr}.")

print("-"*10)    
for abbr,qala in list(cities.items()):
    print(f"{abbr} мемлекетінде {qala} деген қала бар.")

    
print("-"*10) 
for memleket,abbr in list(states.items()):
    print(f"{memleket} аббревиатруасы {abbr}")
    print(f"және бұл мемлекетте {cities[abbr]} деген қала бар")   
    
    
 
print("-"*10)
state  = states.get("US")

if not state:
    print("Мұндей ел жоқ")
    
city = cities.get("US","мұндай ел жоқ")
print(f"МЕМЛЕКЕТ 'US' ОСЫ ҚАЛА БАР{city}")    
    
print(states.values())
print(states.keys())
print(states.items())

states["Түркия"] = "TR"
cities["TR"] = "Анкара"


choose = input("Қандай  мемелекетің астанасы керек?")
if choose in states:
    print(f"Бұл мемлекеттің астанасы: " + cities[states[choose]])
    
  
states["Катар"] ="К"    
    
print("*"*10)
for state in list(states.keys()):
    if state[0] == 'К':
        print(state) 
        
        
        
abbreviations_to_countries = {}        
for state,abbv in list(states.items()):
    abbreviations_to_countries[abbv] = state
    
print(abbreviations_to_countries.items())    
 
 
delete_user = input("Қандай елді өшіру керек?")

for state, abbr in list(states.items()):
   if delete_user in states:
       if states[delete_user] in cities:
           del cities[states[delete_user]]
           del states[delete_user]
           
           
    
print(states.items())  
print(cities.items()) 



question = input(">")

if question in states:
    print(states[question],question) 
    
    
cities["KZ"] = "Алматы"

x = 0     
for state in list(states.keys()):
    x+=1
print(f"Бізде жалпы {x} мемлекет бар") 

"""

city = input(" > ")
if city in cities:
    print(states[cities[city]])
    
        
       
   
    
            
        
        
     