from sound import *

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', 
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', 
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', 
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', 
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', 
    '$': '...-..-', '@': '.--.-.', ' ': '/'}

english_dict = {value : key for key , value in morse_dict.items()}

print("""                                                                            
                                  /        /o    _/_o                        
 _ _ _   __ _   (   _    _, __ __/ _    __/,  _, / ,  __ _ _   __,  _   __  ,
/ / / /_(_)/ (_/_)_(/_  (__(_)(_/_(/_  (_/_(_(__(__(_(_)/ / /_(_/(_/ (_/ (_/_
                                                                          /  
                                                                         '   
""")

class Translator:
    def __init__(self , morse_dict , english_dict):
        self.morse_dict = morse_dict
        self.english_dict = english_dict

    def english_to_morse(self):
        text = input("enter something... : ").strip().upper()
        output = [self.morse_dict[char] for char in text if char in self.morse_dict]
        print("\n .... translating to morse code ..... \n")
        joining = "".join(output)
        print(" ".join(output))
        for symbols in joining:
            if symbols == ".":
                dot()
            elif symbols == "-":
                dash()
            else :
                return 0

        
    def morse_to_english(self):
        text1 = input("Enter Morse code (separate letters with spaces): ").strip()
        translation = text1.split()
        print("\n .... Translating to English ..... \n")
        result = "".join([self.english_dict[char] for char in translation if char in self.english_dict])
        print(result.capitalize())


print("1. englsih to morse: ")
print("2. morse code to english: \n")
read = int(input("choose between (1/2) : "))

trans = Translator(morse_dict , english_dict)
if read == 1:
    trans.english_to_morse()
elif read == 2:
    trans.morse_to_english() 
else :
    print("enter a valid choice....")

