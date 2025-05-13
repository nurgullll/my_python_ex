import sys

script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # Файлдан келген дайын байттар
    raw_bytes = line.strip()
    osh = raw_bytes.replace(b'\xe1\x8a\xa0', b'')

    # Байттарды декодтау -> мәтін
    cooked_string = osh.decode(encoding, errors=errors)

    print(osh, "<===>", cooked_string)

# Файлды байт режимінде оқу

languages = open("languages.txt", mode="rb")

main(languages, encoding, error)


    

