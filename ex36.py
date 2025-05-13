def books_question():
    print("Ғабит Мүсіреповтың шығармасын тап")
    books2 = ["Ұлпан", "Оң қол","Әке","Абай жолы","Сүйекші","Бақытсыз Жамал"]
    print(books2)
    book2 = "Ұлпан"
    book_choose = ""
    while book_choose!=book2:
        book_choose = input(">")
        
    print("ЖАРАЙСЫҢ ҚАЗЫН СЕНІКІ!")    
    
def  qubyzhyk():
    print("Сенің алдыңда ҚАРЫНЫ АШ құбыжық ұйықтап жатыр!")
    print("""1 - Құбыжықты ояту
             2 - Ақырын оны айналып өту
            """)
    choose = int(input(">"))
    if choose == 1:
        die("ҚҰБЫЖЫҚ СЕНІ ЖЕП ҚОЙДЫ!")
    elif choose == 2:
        books_question() 
    else:
        qubyzhyk()       
    
    
def books_list():
    print("Мұхтар Әуезовтың шығармасын тап")
    books = ["Ұлпан", "Оң қол","Әке","Абай жолы","Сүйекші","Бақытсыз Жамал"]
    print(books)
    choose = input(">")
    for i in range(len(books)):
        if  books[i]== choose and choose == "Абай жолы":
            print("ДҰРЫС!")
            books_question()
    die("ДҰРЫС ТАППАДЫҢ!")        
     
 
def daliz():
    print("""
          Кітапхана сөресінде 5 кітап тұр.\n
          Сен бірінші мен соңғы кітапты алып тастасаң, неше кітап қалады?
          """)
    san = int(input(">"))
    if san==3:
        print("ЖАРАЙСЫҢ ДҰРЫС ТАПТЫҢ!")
        books_list()
    elif san <3 and san>0:
        print("ТАҒЫ ОЙЛАН!") 
        daliz()
    else:
        die("ДҰРЫС ТАППАДЫҢ!")     
    
    
def start():
    print("ДАЙЫНСЫҢБА?")
    choose = input(">")
    if choose == "Иә" or choose == "иә":
        daliz()
    elif choose == "Жоқ" or choose == "жоқ":
        die("СЕН ДАЙЫН ЕМЕССІҢ!")
    else:
        start()
        
    
def die(cause):
    print("Ойын бітті!",cause)        

start()
