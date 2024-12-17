text = "Hello Zorld"
alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 3
encrypted_text = ''

for char in text.lower():
    if char == '':
        encrypted_text=''
    else:
        index = alphabet.find(char)
        new_index= (index + shift) % len(alphabet)
        encrypted_text += alphabet[new_index]
print('text:', text)
print('encrypted text:', encrypted_text)