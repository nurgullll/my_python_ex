# бұл функция split арқылы текстті сөздерге бөледі
def break_words(stuff):
    """ Эта функция разбирает текст на слова."""
    words = stuff.split(' ')
    return words

# бұл функция return арқылы бірден sorted функциясын қолданып сөздерге бөлінген тексті іріктейді
def sort_words(words):
    """Cортирует слова."""
    return sorted(words)

# бұл функция pop арқылы текстің бірінші сөзін шығарады яғни pop-тың жақшасының ішіне сөздің индексін береміз
def print_first_word(words):
    """Выводит первое слово после извлечение."""
    word = words.pop(0)
    print(word)

# бұл функция pop арқылы текстің cОңғы сөзін шығарады яғни pop-тың жақшасының ішіне сөздің индексін береміз
def print_last_word(words):
    """Выводит последнее слово после извелечения."""
    word = words.pop(-1)
    print(word)

# бұл функцияның ішіне өзіміз жасаған  break_words функциясын шақырамыз ,
# яғни дайын текст(сөздерге бөлінген) оларды,бірден sort_words функциясын шақыра отырып іріктейміз
def sort_sentence(sentence):
    """Принимает целое предложение и вовращает отсортированные слова."""
    words = break_words(sentence)
    return sort_words(words)

# бұл функция cөйлемнің бірінші және соңғы сөздерін қайтарады
# яғни break_words функциясындағы сөйлемдерді қабылдап ,
# оны words айнымалысына сақтаймыз ал  print_first_word & print_last_word функцияларына words айнымалысын параметр ретінде береміз
def print_first_and_last(sentence):
    """Выврдит первое и последнне слова предложения""" 
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


# бұл функция sort_sentence деген функцияның дайын іріктелген сөздерін алады және бірінші& соңғы сөздерді экранға шығарады
def print_first_and_last_sorted(sentence):
    """Сортирует слова, а затем выводит первое и последнее.""" 
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    