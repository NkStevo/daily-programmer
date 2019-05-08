def main():
    print("----Caeser Cipher Program----")
    choice = input("Input 1 to encode text and 2 to decode text:\n")

    if choice == '1':
        text = input("Input the text you would like to be encoded:\n")
        print(encode(text))
    elif choice == '2':
        text = input("Input the text you would like to be decoded:\n")
        print(decode(text))
    else:
        print("Invalid input")


def encode(text):
    coded_text = ""

    for char in text:
        char_code = ord(char)

        if char_code >= ord('a') and char_code <= ord('z'):
            coded_text += chr(ord('a') + (char_code - ord('a') + 7) % 26)
        elif char_code >= ord('A') and char_code <= ord('Z'):
            coded_text += chr(ord('A') + (char_code - ord('A') + 7) % 26)
        else:
            coded_text += char

    return coded_text

def decode(text):
    coded_text = ""

    for char in text:
        char_code = ord(char)

        if char_code >= ord('a') and char_code <= ord('z'):
            coded_text += chr(ord('a') + (char_code - ord('a') - 7) % 26)
        elif char_code >= ord('A') and char_code <= ord('Z'):
            coded_text += chr(ord('A') + (char_code - ord('A') - 7) % 26)
        else:
            coded_text += char

    return coded_text

if __name__ == '__main__':
    main()
