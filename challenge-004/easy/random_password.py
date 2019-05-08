import string, random

def main():
    count = int(input("How many passwords would you like to generate?"))
    length = int(input("What length are the passwords (max: 127)"))

    if length > 127:
        length = 127

    characters = string.ascii_letters + string.digits + " !#$%&()*+,-./:;<=>?@[\]^_`{|}~"
    passwords = []

    for x in range(count):
        password = ''.join(random.choice(characters) for x in range(length))
        passwords.append(password.strip())

    for password in passwords:
        print(password)

if __name__ == '__main__':
    main()
