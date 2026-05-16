import os

run_diary = True

while run_diary:
    old_diary = input("do you have a old diary ? yes or no ")

    if old_diary == "yes":
        if os.path.exists("diary.txt"):
            run_diary = False
            user = open("diary.txt", "r")
            save = user.read()
            print(save)
            user.close()

            user = open("diary.txt", "a")
            print("what do you want to write in your diary type exit to close your diary ")
            run = True
            while run:
                text = input()
                if text != "exit":
                    user.write(text + "\n")
                else:
                    run = False
                    user.close()
                    run2 = True
                    while run2:
                        continuing = input("do you want to open your diary again ? yes or no ")
                        if continuing == "yes":
                            run2 = False
                            run_diary = True
                        else:
                            print("goodbye")
                            run2 = False
        else:
            print("No diary found.")

    if old_diary == "no":
        if os.path.exists("diary.txt"):
            qeustion = True
            while qeustion:
                sure = input("are you sure you want to replace your old diary ? yes or no ")
                if sure == "yes":
                    qeustion = False   # FIXED
                    os.remove("diary.txt")
                    print("Old diary deleted.")
                    run_diary = False
                    user = open("diary.txt", "w")
                    print("what do you want to write in your diary type exit to close your diary ")
                    run = True
                    while run:
                        text = input()
                        if text != "exit":
                            user.write(text + "\n")
                        else:
                            run = False
                            user.close()
                            run2 = True
                            while run2:
                                continuing = input("do you want to open your diary again ? yes or no ")
                                if continuing == "yes":
                                    run2 = False
                                    run_diary = True
                                else:
                                    print("goodbye")
                                    run2 = False  
                else:
                    qeustion = False
        else:
            run_diary = False
            user = open("diary.txt", "w")
            print("since you dont have a  diary. Making a new one.")
            print("what do you want to write in your diary type exit to close your diary ")
            run = True
            while run:
                text = input()
                if text != "exit":
                    user.write(text + "\n")
                else:
                    run = False
                    user.close()
                    run2 = True
                    while run2:
                        continuing = input("do you want to open your diary again ? yes or no ")
                        if continuing == "yes":
                            run2 = False
                            run_diary = True
                        else:
                            print("goodbye")
                            run2 = False   

