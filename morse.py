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

english_dict = {value : key  for key , value in morse_dict.items()}

print("""                                                                            
                                  /        /o    _/_o                        
 _ _ _   __ _   (   _    _, __ __/ _    __/,  _, / ,  __ _ _   __,  _   __  ,
/ / / /_(_)/ (_/_)_(/_  (__(_)(_/_(/_  (_/_(_(__(__(_(_)/ / /_(_/(_/ (_/ (_/_
                                                                          /  
                                                                         '   
""")


print("1. englsih to morse: ")
print("2. morse code to english: \n")
read = int(input("choose between (1/2) : "))

if read == 1:
    text = input("enter something... : ").upper()
    output = [morse_dict[char] for char in text if char in morse_dict]
    print("\n .... translating to morse code ..... \n")
    print(" ".join(output))

elif read == 2:
    text1 = input("enter something... : ").upper()
    output1 = [english_dict[char] for char in text1 if char in english_dict]
    print("\n .... translating to morse code ..... \n")
    print(" ".join(output1))

else :
    print(" !!! choose a valid option !!! ")