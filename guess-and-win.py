import random as rm

total_stars = 0
print("_______________HUNT NUMBER________________\n\n")
print("Welcome to the game!")
won_msgs = ["Congrats!", "Wow!", "Unbelievable!", "Amazing!", "Super!"]
dismis_msgs=["Aww!","Opps!","Come on!","Watch it!"]

def game(num, guess, count):
    count = count - 1
    if num == guess:
        print(f"\nCongratulations!! You won the game! \n")
        return count, True
    elif count > 0:
        if num > guess:
            print(
                ">>>",rm.choice(dismis_msgs),f"'{num}' is very high. Try lower! \n      {count} chances are left…"
            )
            return count, False
        elif num < guess:
            print(
                ">>>",rm.choice(dismis_msgs),f"'{num}' is too low. Try higher! \n      {count} chances are left…"
            )
            return count, False
    else:
        print(
            f"\n>>>Sorry! You have run out of chances.\nThe correct number was {guess} !!"
        )
        return count, True


game_running = False
while not game_running:
    print("\nSelect your level to continue……\n    •easy\n    •hard\n    •insane")
    while True:
        game_level = input().lower().strip()

        if game_level == "easy":
            count = 10

            sn = rm.randint(1, 5)
            ln = rm.randint(6, 10)
            guess = rm.randint(sn, ln)
            print(f"*Range={sn}-{ln}\nOk!! Let's do this! Try a number!!..\n")
            break
        elif game_level == "hard":
            count = 10

            sn = rm.randint(10, 20)
            ln = rm.randint(30, 40)
            guess = rm.randint(sn, ln)
            print(f"*Range = {sn}-{ln}\nGood luck! This will be harder than you think! Try a number!!..\n")
          
            
            break
        elif game_level == "insane":
            count = 6

            sn = rm.randint(50, 70)
            ln = rm.randint(75, 100)
            guess = rm.randint(sn, ln)
            print(f"*Range = {sn}-{ln}\nYou must be an expert!!.. Then wish me luck! Try a number!!..\n")
                
            
            break
        else:
            print(" Please select your level to continue..")

    game_over = False
    while not game_over:
        num = input()
        if num.isdigit():
            num = int(num)
            count, game_over = game(num, guess, count)
            if num == guess:
                
                while True:
                    ask1 = input("Want to check your score?\n    •Yes    •No  ")
                    if ask1.upper() == "YES":
                        if game_level == "easy":
                            stars_earned = 1

                        elif game_level == "hard":
                            stars_earned = 2

                        else:
                            stars_earned = 4
                        total_stars = total_stars + stars_earned
                        print(
                            "\n>>>",
                            rm.choice(won_msgs),
                            f"You have: ⭐{total_stars}\n  Keep this up!")
                        break

                    elif ask1.upper()=="NO":
                        print("\nOk then……")
                        break
                    else:
                        print("\n Say yes or No!…")
                        
                    
        else:
            print(" Please enter a valid number……")

    while True:
        ask2 = input("Do you wish to play again?\n    •Yes    •No  ")
        if ask2.upper() == "NO":
            print(f"\nThank you for playing! You have earned ⭐{total_stars} in the end!")
           
            
            game_running = True
            break
        elif ask2.upper() == "YES":
            print(" \n\n        ________NEW GAME________         ")
            break
        else:
            print("\n Say Yes or No!…")
