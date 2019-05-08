import json

def main():
    with open('ciphertext.json') as json_file:
        ciphertext = json.load(json_file)

        print("----Substitution Cipher Program----")
        choice = input("Input 1 to encode text and 2 to decode text:\n")

        if choice == '1':
            text = input("Input the text you would like to be encoded:\n")
            print(encode(text, ciphertext))
        elif choice == '2':
            text = input("Input the text you would like to be decoded:\n")
            print(decode(text, ciphertext))
        else:
            print("Invalid input")

def encode(text, ciphertext):
    coded_text = ""

    for char in text:
        char_code = ord(char)

        if (char_code >= ord('a') and char_code <= ord('z')) or (char_code >= ord('A') and char_code <= ord('Z')):
            coded_text += ciphertext[char]
        else:
            coded_text += char

    return coded_text

def decode(text, ciphertext):
    coded_text = ""
    inverse_ciphertext = {value: key for key, value in ciphertext.items()}

    for char in text:
        if char in inverse_ciphertext:
            coded_text += inverse_ciphertext[char]
        else:
            coded_text += char

    return coded_text

if __name__ == '__main__':
    main()
