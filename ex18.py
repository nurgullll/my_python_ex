def print_two (*args):
    arg1,arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1,arg2):
    print(f"arg1: {arg1},arg: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("А я ничего не получаю.")

print_two("Нургуль","Хунтуган")
print_two_again("Нургуль","Хунтуган")
print_one("Первый!")
print_none()