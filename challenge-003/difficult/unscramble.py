def main():
    scramble_dictionary = {}

    with open('dictionary.txt', 'r') as dict_file:
        for line in dict_file:
            # Words are encoded as tuples for which each index represents the
            # frequency of characters with ASCII values equal to that index
            frequency = [0 for x in range(255)]

            for char in line.strip():
                frequency[ord(char)] += 1

            scramble_dictionary[tuple(frequency)] = line.strip()


    with open('scramble.txt', 'r') as scramble_file:
        scramble = [line.strip() for line in scramble_file]

    for word in scramble:
        frequency = [0 for x in range(255)]

        for char in word:
            frequency[ord(char)] += 1

        print("Scrambled word: " + word + "")
        print("Original word: " + scramble_dictionary[tuple(frequency)] + "\n")


if __name__ == '__main__':
    main()
