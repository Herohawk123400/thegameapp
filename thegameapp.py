"""
THE GAME APP

Description:       
This is an app full of games and 
everyday tools you might need in life. 
From stuff like Rock Paper Scissors against a bot, 
all the way to cool and useful calculators, and more.
"""
stop= "y"
import random
import time
import sys
tg=input("Would you like to use tools or games? ")
#if tg - aka type_game, the input = "games", then -->
if tg == "games":
    
    while stop == "y":
        game_type=input("What type of game would you like to play? (Options: rock paper scissors {type RPS}, 2 player battle {type TPB}, Mad Libs {type MLB}, tic-tac-toe {type TTT}, uno {type UNO},or guess the number {type GTN}). ")
        if game_type == "TTT":
            print("Commencing...")
            print("(Size: 9 squares.)")
            print("Btw, a piece of paper might be helpful, but your choice...")
            import random
            square1="S1"
            square2="S2"
            square3="S3"
            square4="S4"
            square5="S5"
            square6="S6"
            square7="S7"
            square8="S8"
            square9="S9"
            possible=[square1,square2,square3,square4,square5,square6,square7,square8,square9]
            print("Ps: Squares 1,2,3 are in the top row, 4,5,6 are in the middle, and 7,8,9 are in the bottom.")
            cfw="n"
            print()
            while cfw != "y":
                ua1 = input("What square would you like to place on?\nSquares to place on: " + str(possible)+" ")
                if ua1 in possible:
                    possible.remove(ua1)
                print()
                print("Computers turn!")
                #AI playing against you!
                ca1 = random.choice(possible)
                print("Computer chose: " + ca1 + " and you chose " + ua1 +".")
                print("Squares taken: " + ua1 + " and " + ca1 + ".")
                cfw=input("Has anyone won yet? (y/n) ")
                if ca1 in possible:
                    possible.remove(ca1)
                if cfw == "y":
                    who=input("Who won? (m/c) ")
                    if who == "m":
                        print("Yay! Play again later!" )
                        break
                    if who == "c":
                        print("Sad. Play again later!" )
                        break
                if cfw != "y":
                    print("Next round.")
                else:
                    stop=input("Would you like to keep using games or stop now? (y to continue, n to stop.) ")
                    break

        if game_type == "RPS":
            import random
            def play():
                user_action = input("Enter a choice: rock, paper, or scissors. ")
                possible_actions = ["rock", "paper", "scissors"]
                if user_action.lower() == "rock" or user_action.lower() == "paper" or user_action.lower() == "scissors":
                    user_action = user_action.lower()
                else:
                    print("Please enter a valid input.")
                    sys.exit()
                computer_action = random.choice(possible_actions)
                print("You chose " + user_action + ", computer chose " + computer_action )
                if user_action == "rock" and computer_action == "paper":
                    print("Whoops! paper beats rock! Try again!")
                elif user_action == "rock" and computer_action == "scissors":
                    print("Yay! rock beats scissors!")
                elif user_action == "rock" and computer_action == "rock":
                    print("Whoops! Its a tie! (rock and rock) Try again!")
                elif  user_action == "paper" and computer_action == "rock":
                    print("Yay! paper beats rock!")
                elif user_action == "paper" and computer_action == "scissors":
                    print("Whoops! scissors beats paper! Try again!")
                elif user_action == "paper" and computer_action == "paper":
                    print("Whoops! Its a tie! (paper and paper) Try again!")
                elif user_action == "scissors" and computer_action == "scissors":
                    print("Whoops! Its a tie! (scissors and scissors) Try again!")
                elif user_action == "scissors" and computer_action == "rock":
                    print("Whoops! rock beats scissors! Try again!")
                elif user_action == "scissors" and computer_action == "paper":
                    print("Yay! scissors beats paper!")
                    
            while True:
                play()
                play_again = input("Play again? (y/n): ")
                if play_again.lower() != "y":
                    stop=input("Would you like to keep using games or stop now? (y to continue, n to stop.) ")
                    break
        elif game_type == "MLB":
            noun1=input("Give me the first noun. ")
            noun2=input("Give me the second noun. ")
            verb1=input("Give me the first verb. ")
            verb2=input("Give me the second verb. ")
            adj1=input("Give me the first adjective. ")
            adj2=input("Give me the second adjective. ")
            story=input("What type of story would you like? Options: A day at the beach {type BD}, A visit to space {type SV}, or mining city {type MC}? ")
            if story == "MC":
                print("Once apon a time, " +noun1 + " was working very " + verb1 + " in the mines. But suddenly, his friend " + noun2 + " came and started " + adj1 + " him. So he started " + adj1 + " back at him. Then they started " + verb2 + " together, and they had an " + adj2 + " day!")
            if story == "BD":
                print("Once apon a time, " + noun1 + " was building a sand castle at the beach. Then his friend " + noun2 + " came and helped him build it. But suddenly, someone came " + adj1 + " toward them and started " + verb1 + " them. They both " + verb2 + " together with the stranger and had a "+adj2+" day.") 
            if story == "SV":
                print("Once apon a time, " + noun1 + " took a visit to space. He had such a " + adj1 + " time that he went again with his friend, " + verb1 + " all the way there. Once he got there, they found their friend, " + noun2 +". Then, they all started " + verb2+" together. When they all came back from their great trip, they were all oh-so " + adj2 + ".")
            stop=input("Would you like to keep using games or stop now? (y to continue, n to stop.) ")
        elif game_type == "GTN":
            import random
            def number_guessing_game():
                number = random.randint(1, 1000)
                attempts = 0

                print("Guess a number between 1 and 1000")

                while True:
                    try:
                        guess = int(input("Enter your guess: "))
                        attempts += 0
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        attempts += 0
                        print()
                        continue
        
                    if guess < number:
                        print("Too low!")
                        attempts +=1
                        print()
                    elif guess > number:
                        print("Too high!")
                        attempts +=1
                        print()
                    else:
                        print()
                        print("Congratulations! You guessed the number in " + str(attempts)+" attempts! (not true)")
                        break

            if __name__ == "__main__":
                number_guessing_game()
            stop=input("Would you like to keep using games or stop now? (y to continue, n to stop.) ")
        
        elif game_type == "UNO":
            print("Commencing...")
            import random
            import sys
            import time
            p1name = input("What is the first players name? ")
            p2name = input("What is the second players name? ")
            done = print("Come back later, its not done screw you.")
            sys.exit()
        elif game_type == "TPB":
            print("Commencing...")
            import random
            p1name=input("What is the first players name? ")
            p2name=input("What is the second players name? ")
            print()
            p1hp=input("What is player 1's hp? ")
            p2hp=input("What is player 2's hp? ")
            print()
            print()
            print()
            p1hp=int(p1hp)
            p2hp=int(p2hp)
            print("First, lets learn the rules. First, player 1 ALWAYS starts the match.")
            print("Here is the list of attacks;")
            attack1=print("Attack 1: bow: does 10 dmg.")
            attack2=print("Attack 2: sword: does 15 dmg.")
            attack3=print("Attack 3: mace: does 50 dmg, if you miss the attack, does 20 dmg to you.")
            print()
            attack1p1=input("What is " + p1name + "'s first attack? ")
            attack2p1=input("What is " + p1name + "'s second attack? ")
            attack3p1=input("What is " + p1name + "'s third attack? ")
            print()
            print()
            attack1p2=input("What is " + p2name + "'s first attack? ")
            attack2p2=input("What is " + p2name + "'s second attack? ")
            attack3p2=input("What is " + p2name + "'s third attack? ")
            print()
            print("Both of you have 100 health. First one to kill the other wins.")
            print("Please note that the mace one is very, VERY hard to excecute. (Totally...)")
            print("Ok, lets start the game now. You must get the other persons health to EXACTLY 0 to win.")
            print("If at any point one player reaches zero (or below), then the other person wins the game and the program should be ended.")
            print()
            print()
            print()

            C1P1HP=print("Player 1 starting health = " + str(p1hp))
            C1P2HP=print("Player 2 starting health = " + str(p2hp))
            print()
            while C1P1HP != "0" and C1P2HP != "0":
                at1p1=input("Ok, which attack will " + p1name + " use first? " + attack1p1 + ", "+ attack2p1 + ", or "+ attack3p1 + "?")

                if at1p1 == "bow":
                    print("Player 2 just lost 10 hp! Oh no!")
                    p2hp-=10
                    print("Player 2 hp is now at " + str(p2hp))
                    print()
    
                if at1p1 == "sword":
                    print("Player 2 just lost 15 hp! Oh no!")
                    p2hp-=15
                    print("Player 2 hp is now at " + str(p2hp))
                    print()
    
                if at1p1 == "mace":
                    user = input("Enter a choice: rock, paper, or scissors. ")
                    actions_maybe = ["rock", "paper", "scissors"]
                    other = random.choice(actions_maybe)
                    print("Ok, lets see; you chose " + user + ", and the computer chose " + other + ".")
                    if user == "scissors" and other == "rock":
                        print("You lose. Mace attack canceled.")
                        p1hp-=20
                        print("Player 1 hp is now at " + str(p1hp)+".")
                        print()
                    if user == "scissors" and other == "paper":
                        print("Yay! Mace attack succesful!") 
                        p2hp-=50
                        print("Player 2 hp is now at " + str(p2hp)+".")
                        print()
                    if user == "scissors" and other == "scissors":
                        print("You lose. Mace attack canceled.")
                        p1hp-=20
                        print("Player 1 hp is now at " + str(p1hp)+".")
                        print()
                    if user == "paper" and other == "rock":
                        print("Yay! Mace attack succesful!")
                        p2hp-=50
                        print("Player 2 hp is now at " + str(p2hp)+".")
                        print()
                    if user == "paper" and other == "scissors":
                        print("You lose. Mace attack canceled.")
                        p1hp-=20
                        print("Player 1 hp is now at " + str(p1hp)+".")
                        print()
                    if user == "paper" and other == "paper":
                        print("You lose. Mace attack canceled.")
                        p1hp-=20
                        print("Player 1 hp is now at " + str(p1hp)+".")
                        print()
                    if user == "rock" and other == "rock":
                        print("You lose. Mace attack canceled.")
                        p1hp-=20
                        print("Player 1 hp is now at " + str(p1hp)+".")
                        print()
                    if user == "rock" and other == "paper":
                        print("You lose. Mace attack canceled.")
                        p1hp-=20
                        print("Player 1 hp is now at " + str(p1hp)+".")
                        print()
                    if user == "rock" and other == "scissors":
                        print("Yay! Mace attack succesful!")
                        p2hp-=50
                        print("Player 2 hp is now at " + str(p2hp)+".")
                        print()
                print("Anyway, lets move on to player 2's attack.")

                at1p2=input("Ok, which attack will " + p2name + " use first? " + attack1p2 + ", "+ attack2p2 + ", or "+ attack3p2 + "?")
                print()
                if at1p2 == "bow":
                    print("Player 1 just lost 10 hp! Oh no!")
                    p1hp-=10
                    print("Player 1 hp is now at " + str(p1hp)+".")
                    print()
                if at1p2 == "sword":
                    print("Player 1 just lost 15 hp! Oh no!")
                    p1hp-=15
                    print("Player 1 hp is now at " + str(p1hp)+".")
                    print()
                if at1p2 == "mace":
                    user = input("Enter a choice: rock, paper, or scissors. ")
                    actions_maybe = ["rock", "paper", "scissors"]
                    other = random.choice(actions_maybe)
                    print("Ok, lets see; you chose " + user + ", and the computer chose " + other + ".")
                    if user == "scissors" and other == "rock":
                        print("You lose. Mace attack canceled.")
                        p2hp-=20
                        print("Player 2 hp is now at " + str(p2hp)+".")
                        print()
                    if user == "scissors" and other == "paper":
                        print("Yay! Mace attack succesful!") 
                        p1hp-=50
                        print("Player 1 hp is now at " + str(p1hp)+".")
                        print()
                    if user == "scissors" and other == "scissors":
                        print("You lose. Mace attack canceled.")
                        p2hp-=20
                        print("Player 2 hp is now at " + str(p2hp)+".")
                        print()
                    if user == "paper" and other == "rock":
                        print("Yay! Mace attack succesful!")
                        p1hp-=50
                        print("Player 1 hp is now at " + str(p1hp)+".")
                        print()
                    if user == "paper" and other == "scissors":
                        print("You lose. Mace attack canceled.")
                        p2hp-=20
                        print("Player 2 hp is now at " + str(p2hp)+".")
                        print()
                    if user == "paper" and other == "paper":
                        print("You lose. Mace attack canceled.")
                        p2hp-=20
                        print("Player 2 hp is now at " + str(p2hp)+".")
                        print()
                    if user == "rock" and other == "rock":
                        print("You lose. Mace attack canceled.")
                        p2hp-=20
                        print("Player 2 hp is now at " + str(p2hp)+".")
                        print()
                    if user == "rock" and other == "paper":
                        print("You lose. Mace attack canceled.")
                        p2hp-=20
                        print("Player 2 hp is now at " + str(p2hp)+".")
                        print()
                    if user == "rock" and other == "scissors":
                        print("Yay! Mace attack succesful!")
                        p1hp-=50
                        print("Player 1 hp is now at " + str(p1hp)+".")
                        print()
                print("Somebody might lose here...")
                print("If health goes into negatives, write 0, not a negative #.")
                print()
                print("Player 1 hp: " + str(p1hp))
                print("Player 2 hp: " + str(p2hp))
                C1P1HP=input("What is P1's health? ")
                C1P2HP=input("What is P2's health? ")
                stop=input("Would you like to keep using games or stop now? (y to continue, n to stop.) ")

        else:
            break
elif tg == "tools":
    while stop == "y":
        tool=input("What type of tool would you like to use? (Options: Encoder {type ENC}, Calculator {type CALC}, Random number generator {type RNG}, random password generator {type RPG}, or Shopping list {type RSL}. ")
        print()
        if tool == "CALC":
            num1=int(input("What is the first number? "))
            num2=int(input("What is the second number? "))
            sign=input("Would you like to multiply, divide, add, subtract, or take the mod (mod 10 only)? (Symbols in order: * / + - %) ")
            if sign == "*":
                total=str(num1*num2)
                print("Your final number after multiplying is: " + total + ".")
            if sign == "/":
                total=str(num1/num2)
                print("Your final number after dividing is: " + total + ".")
            if sign == "+":
                total=str(num1+num2)
                print("Your final number after adding is: " + total + ".")
            if sign == "-":
                total=str(num1-num2)
                print("Your final number after subtracting is: " + total + ".")
            if sign == "%":
                mod1=int(input("What is the number you would like to take the modulus of? "))
                total=str(mod1 % 10)
                print("Your final number after taking mod 10 is: " + total + ".")
            stop=input("Would you like to keep using tools or stop now? (y to continue, n to stop.) ")
            print()
            print()
        elif tool == "RPG":
            length=input("What would you like the length of your password to be? {Max 20} ")
            length = int(length)
            Type=input("What type of password would you like? One with only numbers [type NUM], one with lowercase and uppercase letters [type LET], or one with letters, numbers, and symbols [type ALL]? ")
            if Type == "NUM":
                import random
                n1=str(random.randint(1,9))
                n2=str(random.randint(1,9))
                n3=str(random.randint(1,9))
                n4=str(random.randint(1,9))
                n5=str(random.randint(1,9))
                n6=str(random.randint(1,9))
                n7=str(random.randint(1,9))
                n8=str(random.randint(1,9))
                n9=str(random.randint(1,9))
                n10=str(random.randint(1,9))
                n11=str(random.randint(1,9))
                n12=str(random.randint(1,9))
                n13=str(random.randint(1,9))
                n14=str(random.randint(1,9))
                n15=str(random.randint(1,9))
                n16=str(random.randint(1,9))
                n17=str(random.randint(1,9))
                n18=str(random.randint(1,9))
                n19=str(random.randint(1,9))
                n20=str(random.randint(1,9))
                if length == 1:
                    number = n1
                elif length == 2:
                    number = n1+n2
                elif length == 3:
                    number == n1+n2+n3
                elif length == 4:
                    number == n1+n2+n3+n4
                elif length == 5:
                    number = n1+n2+n3+n4+n5
                elif length == 6:
                    number = n1+n2+n6+n4+n5+n6
                elif length == 7:
                    number = n1+n2+n3+n4+n5+n6+n7
                elif length == 8:
                    number = n1+n2+n3+n4+n5+n6+n7+n8
                elif length == 9:
                    number = n1+n2+n3+n4+n5+n6+n7+n8+n9
                elif length == 10:
                    number = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10
                elif length == 11:
                    number = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11
                elif length == 12:
                    number = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12
                elif length == 13:
                    number = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13
                elif length == 14:
                    number = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14
                elif length == 15:
                    number = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15
                elif length == 16:
                    number = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16
                elif length == 17:
                    number = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17
                elif length == 18:
                    number = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17+n18
                elif length == 19:
                    number = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17+n18+n19
                elif length == 20:
                    number = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17+n18+n19+n20
                else:
                    sys.exit()
                print()
                print("Your number password is: " + number + ".")
                print()
                stop=input("Would you like to keep using tools or stop now? (y to continue, n to stop.) ")
            elif Type == "LET":
                import string
                string.ascii_letters 
                "abcdefghijklmnopqrstuvwxyz"
                import random
                n1=random.choice(string.ascii_letters)
                n2=random.choice(string.ascii_letters)
                n3=random.choice(string.ascii_letters)
                n4=random.choice(string.ascii_letters)
                n5=random.choice(string.ascii_letters)
                n6=random.choice(string.ascii_letters)
                n7=random.choice(string.ascii_letters)
                n8=random.choice(string.ascii_letters)
                n9=random.choice(string.ascii_letters)
                n10=random.choice(string.ascii_letters)
                n11=random.choice(string.ascii_letters)
                n12=random.choice(string.ascii_letters)
                n13=random.choice(string.ascii_letters)
                n14=random.choice(string.ascii_letters)
                n15=random.choice(string.ascii_letters)
                n16=random.choice(string.ascii_letters)
                n17=random.choice(string.ascii_letters)
                n18=random.choice(string.ascii_letters)
                n19=random.choice(string.ascii_letters)
                n20=random.choice(string.ascii_letters)
                if length == 1:
                    letter = n1
                elif length == 2:
                    letter = n1+n2
                elif length == 3:
                    letter == n1+n2+n3
                elif length == 4:
                    letter == n1+n2+n3+n4
                elif length == 5:
                    letter = n1+n2+n3+n4+n5
                elif length == 6:
                    letter = n1+n2+n6+n4+n5+n6
                elif length == 7:
                    letter = n1+n2+n3+n4+n5+n6+n7
                elif length == 8:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8
                elif length == 9:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9
                elif length == 10:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10
                elif length == 11:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11
                elif length == 12:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12
                elif length == 13:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13
                elif length == 14:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14
                elif length == 15:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15
                elif length == 16:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16
                elif length == 17:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17
                elif length == 18:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17+n18
                elif length == 19:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17+n18+n19
                elif length == 20:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17+n18+n19+n20
                else:
                    sys.exit()
                print()
                print("Your password is: " + letter + ".")
                print()
                stop=input("Would you like to keep using tools or stop now? (y to continue, n to stop.) ")
            elif Type == "ALL":
                import random
                my_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "?"]
                n1= random.choice(my_list)
                n2= random.choice(my_list)
                n3= random.choice(my_list)
                n4= random.choice(my_list)
                n5= random.choice(my_list)
                n6= random.choice(my_list)
                n7= random.choice(my_list)
                n8= random.choice(my_list)
                n9= random.choice(my_list)
                n10= random.choice(my_list)
                n11= random.choice(my_list)
                n12= random.choice(my_list)
                n13= random.choice(my_list)
                n14= random.choice(my_list)
                n15= random.choice(my_list)
                n16= random.choice(my_list)
                n17= random.choice(my_list)
                n18= random.choice(my_list)
                n19= random.choice(my_list)
                n20= random.choice(my_list)
                if length == 1:
                    letter = n1
                elif length == 2:
                    letter = n1+n2
                elif length == 3:
                    letter == n1+n2+n3
                elif length == 4:
                    letter == n1+n2+n3+n4
                elif length == 5:
                    letter = n1+n2+n3+n4+n5
                elif length == 6:
                    letter = n1+n2+n6+n4+n5+n6
                elif length == 7:
                    letter = n1+n2+n3+n4+n5+n6+n7
                elif length == 8:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8
                elif length == 9:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9
                elif length == 10:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10
                elif length == 11:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11
                elif length == 12:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12
                elif length == 13:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13
                elif length == 14:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14
                elif length == 15:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15
                elif length == 16:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16
                elif length == 17:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17
                elif length == 18:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17+n18
                elif length == 19:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17+n18+n19
                elif length == 20:
                    letter = n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17+n18+n19+n20
                else:
                    sys.exit()
                print()
                print("Your hard-to-guess password is : " + letter )
                print()
                stop=input("Would you like to keep using tools or stop now? (y to continue, n to stop.) ")
        elif tool == "RNG":
            import random
            bound1=int(input("What is your first boundary? (EX: 1) "))
            bound2=int(input("What is your second boundary? (EX:100) "))
            num=random.randint(bound1,bound2)
            print("Your randomly generated number within those bounds is: " + str(num) + "!")
            stop=input("Would you like to keep using tools or stop now? (y to continue, n to stop.) ")
        elif tool == "RSL":
            i1=input("What is the first item on your shopping list? ")
            i2=input("What is the second item on your shopping list? ")
            i3=input("What is the third item on your shopping list? ")
            i4=input("What is the fourth item on your shopping list? ")
            i5=input("What is the fifth item on your shopping list? ")
            i6=input("What is the sixth item on your shopping list? ")
            i7=input("What is the seventh item on your shopping list? ")
            i8=input("What is the eighth item on your shopping list? ")
            i9=input("What is the ninth item on your shopping list? ")
            i0=input("What is the last item on your shopping list? ")
            List=[i1,i2,i3,i4,i5,i6,i7,i8,i9,i0]
            store=input("Which store are you going to to buy everything? ")
            c1=float(input("What is the cost of " + i1 + "?" ))
            c2=float(input("What is the cost of " + i2 + "?" ))
            c3=float(input("What is the cost of " + i3 + "?" ))
            c4=float(input("What is the cost of " + i4 + "?" ))
            c5=float(input("What is the cost of " + i5 + "?" ))
            c6=float(input("What is the cost of " + i6 + "?" ))
            c7=float(input("What is the cost of " + i7 + "?" ))
            c8=float(input("What is the cost of " + i8 + "?" ))
            c9=float(input("What is the cost of " + i9 + "?" ))
            c0=float(input("What is the cost of " + i0 + "?" ))
            dc=float(input("What is the total discount from all the items, if there is one? "))
            cost=0
            c9+=c0
            c8+=c9
            c7+=c8
            c6+=c7
            c5+=c6
            c4+=c5
            c3+=c4
            c2+=c3
            c1+=c2
            cost+=c1
            print("Total Items: " + str(List))
            print("Store to buy from: " + store)
            print("Total cost: " + str(cost))
            print("Total discount: " + str(dc))
            print("-----------------------")
            cost1=(cost-dc)
            print("Total cost of items at " + store + ": $" + str(cost1)+".")
            print("Thanks for using!")
            stop=input("Would you like to keep using tools or stop now? (y to continue, n to stop.) ")

        else:
            break
            
