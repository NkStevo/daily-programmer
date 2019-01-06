def main():
    name = input("Input your name:\n")
    answer_check = True
    second_outcome = ""

    print("Hello " + name + ", you are at the entrance of a dungeon and there are two paths ahead of you, left and right. Which path will you take?")
    print("Type \'left\' to go left or \'right\' to go right:")

    answer = user_input("left", "right")

    if answer == "left":
        print("You enter the next room to see an ogre standing tall in the doorway. Will you attack him or befriend him?")
        print("Type \'befriend\' to befriend him or \'attack'\' to attack him:")

        answer = user_input("befriend", "attack")
    else:
        print("You enter the next room to see a fountain overflowing with faintly glowing water and a staircase behind it. Will you drink from it?")
        print("Type \'yes\' to drink from it or \'no\' to leave it:")

        answer = user_input("yes", "no")

    if answer == "befriend":
        print("The ogre is delighted to make a new friend and leads you down a staircase to the final room of the dungeon.")
    elif answer == "attack":
        print("The ogre is so enraged by the unprovoked assault that he punches a hole straight through the ground. You fall through and land in the final room of the dungeon.")
    elif answer == "yes":
        print("The water contains a lethal poison which melts your insides to silly putty...\nGAME OVER")
        return
    else:
        print("You ignore the fountain and walk down the steps into the final room of the dungeon")

    print("An orb resting on a pedestal in the center of the room glows with a golden light and says \"" + name + ", I can grant you either immense knowledge or incredible power. Which do you choose?\"")
    print("Type \'knowledge\' for immense knowledge or \'power\' for incredible power:")

    answer = user_input("knowledge", "power")

    if answer == "knowledge":
        print("You live out the rest of your days as the greatest scholar the world has ever known and leave the world with the greatest technological advancements of all time...\nTHE END")
    else:
        print("You become a terrible tyrant that rules over the world with an iron fist...\nTHE END")

def user_input(response1, response2):
    answer = input()

    if answer == response1 or answer == response2:
        return answer

    while True:
        print("You answer was invalid")
        print("Type \'" + response1 + "\' or \'" + response2 + "\':")
        answer = input()

        if answer == response1 or answer == response2:
            return answer


if __name__ == '__main__':
    main()
