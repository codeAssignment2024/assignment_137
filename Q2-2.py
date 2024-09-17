string = '56aAww1984sktr235270aYmn145ss785fsq31D0'

number_string = ''.join([char for char in string if char.isdigit()])
letter_string = ''.join([char for char in string if char.isalpha()])

even_numbers = [int(char) for char in number_string if int(char) % 2 == 0]
ascii_even_numbers = [ord(str(num)) for num in even_numbers]

uppercase_letters = [char for char in letter_string if char.isupper()]
ascii_uppercase_letters = [ord(char) for char in uppercase_letters]

print("Number String:", number_string)
print("Letter String:", letter_string)
print("Even Numbers:", even_numbers)
print("ASCII Code for Even Numbers:", ascii_even_numbers)
print("Uppercase Letters:", uppercase_letters)
print("ASCII Code for Uppercase Letters:", ascii_uppercase_letters)

ciphered_quote = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

def decrypt(cipher, shift):
    decrypted = []
    for char in cipher:
        if char.isalpha():
            shifted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted.append(shifted)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

for s in range(1, 26):
    print(f"Shift {s}: {decrypt(ciphered_quote, s)}")
