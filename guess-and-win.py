import random as rm

total_stars = 0
print("_______________HUNT NUMBER________________\n\n")
print("Welcome to the game!")

won_msgs = ["Congrats!", "Wow!", "Unbelievable!", "Amazing!", "Super!"]
dismiss_msgs = ["Aww!", "Oops!", "Come on!", "Watch it!"]


def game(user_guess, target_num, count):
    count -= 1
    if user_guess == target_num:
        print("\nCongratulations!! You won the game! \n")
        return count, True
    elif count > 0:
        if user_guess > target_num:
            print(
                ">>>",
                rm.choice(dismiss_msgs),
                f"'{user_guess}' is too high. Try lower! \n      {count} chances left…",
            )
        else:
            print(
                ">>>",
                rm.choice(dismiss_msgs),
                f"'{user_guess}' is too low. Try higher! \n      {count} chances left…",
            )
        return count, False
    else:
        print(
            f"\n>>>Sorry! You have run out of chances.\nThe correct number was {target_num} !!"
        )
        return count, True


game_running = True
while game_running:
    print(
        "\nSelect your level to continue……\n    •easy\n    •hard\n    •insane"
    )

    while True:
        game_level = input().lower().strip()

        if game_level == "easy":
            count = 10
            sn, ln = rm.randint(1, 10), rm.randint(11, 15)
            stars_earned = 1
            break
        elif game_level == "hard":
            count = 10
            sn, ln = rm.randint(20, 25), rm.randint(36, 55)
            stars_earned = 2
            break
        elif game_level == "insane":
            count = 6
            sn, ln = rm.randint(50, 70), rm.randint(75, 100)
            stars_earned = 4
            break
        else:
            print(" Please select a valid level (easy, hard, insane)..")

    target_num = rm.randint(sn, ln)
    print(f"*Range = {sn}-{ln}\nLet's do this! Try guessing a number!!..\n")

    game_over = False
    while not game_over:
        num = input().strip()
        if num.isdigit():
            user_guess = int(num)
            count, game_over = game(user_guess, target_num, count)

            if user_guess == target_num:
                total_stars += stars_earned  # ජයග්‍රහණය කළ විට පමණක් එක වරක් එකතු වේ

                while True:
                    ask1 = (
                        input("Want to check your score?\n    •Yes    •No  ")
                        .strip()
                        .upper()
                    )
                    if ask1 == "YES":
                        print(
                            "\n>>>",
                            rm.choice(won_msgs),
                            f"You have: ⭐{total_stars}\n  Keep this up!",
                        )
                        break
                    elif ask1 == "NO":
                        print("\nOk then……")
                        break
                    else:
                        print("\n Say Yes or No!…")
        else:
            print(" Please enter a valid number……")

    while True:
        ask2 = (
            input("Do you wish to play again?\n    •Yes    •No  ")
            .strip()
            .upper()
        )
        if ask2 == "NO":
            print(
                f"\nThank you for playing! You earned ⭐{total_stars} total!"
            )
            game_running = False
            break
        elif ask2 == "YES":
            print(" \n\n        ________NEW GAME________         ")
            break
        else:
            print("\n Say Yes or No!…")
