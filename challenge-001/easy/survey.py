import sys

def main():
    name = input("Input your name: ")
    age = input("Input your age: ")
    username = input("Input your reddit username: ")

    result = "Your name is " + name + ", you are " + age + " years old, and your username is " + username

    print(result)

    f = open("easy-result.txt", "w")
    f.write(result)
    f.close()

if __name__ == "__main__":
    main()
