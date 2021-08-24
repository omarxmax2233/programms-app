import time                                  #FOR TIME
from playsound import playsound                       # FOR PLAY MUSIC
import pyttsx3                                                        # FOR TRANSFORM TEXT TO VOICE (boy)
from gtts import gTTS              # FOR TRANSFORM TEXT TO VOICE (girl)
import datetime                                                      # TO KNOW THE TIME NOW
import webbrowser                       # TO DEAL WITH THE WEB BROWSER
import random                                                        # TO MAKE A RANDOM CHOICE
import os                                             # TO MAKE SERVER
from colorama import Fore                                            # TO BE MORE BEAUTIFUL

x = datetime.datetime.now()


# welcome message

print("welcome in oms studio".upper())

time.sleep(1.3)

# list of apps
apps = ["calculator{1}", "music_player{2}", "timer{3}","DICE{4}","olexa{5}","game{6}",  "final{final}"]

for u in apps:
    time.sleep(0.2)
    print(u)
# select app

select = input("enter the number of the app  :  ")

while select == "1":
    print("loading.......")
    time.sleep(3)
    print("")
    print("please wait")
    time.sleep(1)
    print("")
    print(Fore.LIGHTGREEN_EX , "sucssefull")
    print("")

    # main app

    print(Fore.WHITE , "welcome to calcaulator app with oms studio".upper())

    op = input("enter the number :  ")
    exec('print(' + op + ')')
    time.sleep(12)
    exit() ## #

while select == "2":
    # loading

    print("loading.......")
    time.sleep(3)
    print("")
    print("please wait")
    time.sleep(1)
    print("")
    print(Fore.LIGHTGREEN_EX, "sucssefull")
    print("")

    # main app

    print(Fore.WHITE ,"welcome to music player app with oms studio".upper())
    music = input("chosse music : ")
    if music == "1":
        playsound("1a.mp3")
    if music == "2":
        playsound("2a.mp3")
    if music == "3":
        playsound("3a.mp3")
    if music == "4":
        playsound("4a.mp3")
    time.sleep(12)
    exit()

while select == "3":
    print("loading.......")
    time.sleep(3)
    print("")
    print("please wait")
    time.sleep(1)
    print("")
    print(Fore.LIGHTGREEN_EX , "sucssefull")
    print("")
    print(Fore.WHITE ,"welcome to TIMER app with oms studio".upper())
    #   MAIN
    hour = int(input("enter the hour : "))
    minite = int(input("enter the minite : "))
    second = int(input("enter the second : "))
    time = hour * 3 * 60 * 60 + minite * 60 * 60 + second * 60
    print('{}:{}:{}'.format(hour, minite, second))

    while time > 0:
        time = time - 1
        hour = time // (3 * 60 * 60)
        minite = time // (60 * 60)
        second = time // 60
        print("left time is", hour, minite, second)
        os.system("cls")

    if time == 0:
        print("finish")
        playsound('alarm.mp3')
        time.sleep(12)
        exit()


while select == "4" :

    z = input("Do you want us to give you a random element: ")

    while z == "yes":
        x = input("Enter list elements: ")

        y = x.split()

        print(random.choice(y))

    while z == "no":
        print("see you later")

        break

    while z != "yes" and z != "no":

        print("plz choose yes or no ")

        v = input("Do you want us to give you a random element: ")

        if v == "yes":
            x = input("Enter list elements: ")

            y = x.split()

            print(random.choice(y))
        if v == "no":
            print("see you later")



        time.sleep(15)

        exit()

while select == "5":

    print(Fore.WHITE ,"welcome to OLEXA player app with oms studio".upper())

    chosse = input("7ANAFY OR 3ABLA : ")

    # 7ANAFY

    if chosse == "7ANAFY":
        Q = input("what is the quation :  ")

        if Q == "hi":
            robot = pyttsx3.init()
            robot.setProperty("rate", 130)
            robot.say("hi MR OMAR")
            robot.runAndWait()
            exit()
        if Q == "what time is it now":
            robot = pyttsx3.init()
            robot.setProperty("rate", 130)
            robot.say(x.strftime("%I , %M , %p"))
            robot.runAndWait()
            exit()
        if Q == "tell me about egypt":
            robot = pyttsx3.init()
            robot.setProperty("rate", 100)
            robot.say(
                "Egypt is an Arab country located in the northeastern corner of the continent of Africa the capital is "
                "cairo ,The official language is Arabic")
            robot.runAndWait()
            exit()
        if Q == "what is the best language":
            robot = pyttsx3.init()
            robot.setProperty("rate", 130)
            robot.say("python for ever")
            robot.runAndWait()
            exit()
    # 3ABLA

    if chosse == "3ABLA":

        text = input("what is the quation :  ")

        if text == "hi":

            audio = gTTS(text="hi MR OMAR ")

            audio.save('robot.mp3')

            playsound('robot.mp3')
            exit()
        if text == "can you search about":

            webbrowser.open('https://www.google.com/search?q=' + input("search about : "))
            audio = gTTS(text="of course MR omar", slow=True)
            audio.save('robot.mp3')

            playsound('robot.mp3')
            exit()

while select == "6" :

    txt = "WELCOME TO ROCK, PAPER, SCISSORS!"
    print(Fore.WHITE ,txt.center(100))

    choose = ["rock", "paper", "scissor"]

    player = True

    while player:


        # choice of computer
        computer = random.choice(choose)
        # choice of player
        player_choice = input("Enter your choice > :  ")

        print(computer)

        # player == computer

        if player_choice == computer:
            print("Tie")

        # paper == rock
        elif player_choice == "paper" and computer == "rock":
            print("you win")
        # paper == scissor
        elif player_choice == "paper" and computer == "scissor":
            print("you lost")

        # rock == paper
        elif player_choice == "rock" and computer == "paper":
            print("you lost")
        # rock == scissor
        elif player_choice == "rock" and computer == "scissor":

            print("you win")

        # scissor == rock
        elif player_choice == "scissor" and computer == "rock":

            print("you lost")

        # scissor == paper

        elif player_choice == "scissor" and computer == "paper":

            print("you win")

while select == "final":
    print("FREE FREE FREE  PALASTINE :")
    print("")
    print("")
    print("")
    print("")
    print(Fore.RED ,"                 *********************************************************")
    print(Fore.RED ,"                 *********************************************************")
    print(Fore.RED ,"                 *********************************************************")
    print(Fore.LIGHTWHITE_EX ,"                 *********************************************************")
    print(Fore.LIGHTWHITE_EX ,"                 *********************************************************")
    print(Fore.LIGHTWHITE_EX ,"                 *********************************************************")

    print(Fore.LIGHTBLACK_EX ,"                 *********************************************************")
    print(Fore.LIGHTBLACK_EX ,"                 *********************************************************")
    print(Fore.LIGHTBLACK_EX ,"                 *********************************************************")

    print("#palstine")
    print("#gaza")
    print("#FREE PALASTINE")
    print("#FREE PALASTINE")
    print("‏#FreePalestine")
    input("\033[2;30m")
    time.sleep(15)
    exit()
