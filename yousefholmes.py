# dependecies import
from termcolor import colored,cprint
from os import system
import keyboard
import time
import sys
from cfonts import render
from playsound import playsound
import pygame

# variables
answer=0

# clear the terminal
clear = lambda: system('cls')
clear()

# text animation
def textAnimation(text,delay,color,first_delay):
    time.sleep(first_delay)
    for char in str(text):
        sys.stdout.write(colored(char,color))
        sys.stdout.flush()
        time.sleep(delay)

# get player name
player_name=input(colored("Player Name:","green"))

# welcomig player
clear()
print(render("Yousef Holmes",font="chrome",colors=['red','red','yellow'],align='center'))
print(render("================================================================",font="console",colors=['cyan'],align='center'))
print(render(f"Hellooo {player_name} to YousefHolmes.",colors=["cyan"],font="console",align='center',space=False))
print(render("This is textadventure game.The story is depend on your choice's (Be careful).",colors=["yellow"],font="console",align='center'))
cprint(render("When you ready press s on your keyboard",colors=['red'],font="console",align='center',space=False),attrs=['bold'])
print(render("================================================================",font="console",colors=['cyan'],align='center'))

# backgroundSound
def backgroundSound(condition):
    pygame.mixer.init()
    background_sound = pygame.mixer.Sound("./sounds/background.mp3")
    if(condition=="start"):
        background_sound.set_volume(0.5)
        background_sound.play(1000) 
        
# questionSound
def questionSound():
    question_sound = pygame.mixer.Sound("./sounds/question.mp3")
    question_sound.set_volume(0.7)
    question_sound.play()
    
# horrorSound
def horrorSound():
    horror_sound = pygame.mixer.Sound("./sounds/horror.wav")
    horror_sound.set_volume(0.7)
    horror_sound.play()   

# pointSound
def pointSound():
    point_sound = pygame.mixer.Sound("./sounds/point.wav")
    point_sound.set_volume(0.7)
    point_sound.play()  

# dialoge text
def dialoge(text,color):
    textAnimation(text, 0.075, color, 0.5)

# question's text
def question(question):
    questionSound()
    textAnimation(question,0.075,'magenta',0.2)
    print(render("\n\nPress the selected option on your keyboard",font="console",align='center',colors=['red']))
    key_pressed=""
    while(key_pressed!='1' and key_pressed!='2' and key_pressed!='3' and key_pressed!='4'):
        key_pressed=keyboard.read_key()
    pointSound()    
    return key_pressed

# pause all sounds
def pauseSounds():
    pygame.mixer.pause()

# unpause all sounds
def unpauseSounds():
    pygame.mixer.unpauseSounds()

# game logic
def yousefHolmes():
    clear()
    textAnimation(" \nIn the name of God",0.08,'green',0)
    time.sleep(2)
    clear()
    textAnimation(" A murder takes place in ",0.08,'white',0)
    textAnimation(" Espinas Hotel, ",0.075,'white',1)
    textAnimation(" Area 23, ",0.075,'white',1)
    textAnimation(" District 3, ",0.075,'white',2)
    textAnimation(" Tehran.  ",0.2,'white',0.5)
    textAnimation(" \n\nPolice send Detective Maleki with his assiatant ",0.08,'white',0)
    textAnimation(f"'{player_name}'",0.2,'yellow',0.5)
    textAnimation(" to the crime scene.    \n\nDetective Maleki goes to the crime scene and see's that a man has been shot and there was message written on the wall:\n\n",0.08,'white',0)
    textAnimation("'(As you ordered, Mr. Mohammadi!)'",0.3,'red',1)
    textAnimation("\n\nDetective Maleki asks the hotel manager.\n\n   Detective Maleki: ",0.08,'white',0)
    dialoge("Who is Mr. Mohammadi? Is it the name of the victim or someone else?",'cyan')
    textAnimation("\n\nThe section manager checks the system,",0.08,'white',0)
    textAnimation(" But",0.08,'white',1)
    textAnimation(" there was no name for the room in the system  \n\nDetective Maleki asks all the relevant managers ",0.08,'white',1)
    textAnimation("'who has booked the guest of this room'",0.075,'cyan',0.5)
    textAnimation("\n\nAll the staff say that it was'nt their shift that night and they do'nt know anything! \n\nThe Detective Maleki has confused but continues with power and starts interrogating everyone but he does'nt have enough\n\ntime to make the right decision!",0.08,'white',0.5)
    textAnimation("\n\nYou are in the role of Detective assistant",0.075,'white',0.5)
    textAnimation(f" {player_name}.",0.2,'yellow',0)
    textAnimation("\n\n   Maleki :",0.08,'white',0) 
    dialoge(f" '{player_name}' who we should start interrogating first?",'cyan')
    answer=int(question("  \n\n1- The crew cleaning the floor rooms\n\n2- Hotel manager  \n\n3- The person who reported the murder"))
    if(answer==1):
        clear()
        textAnimation("\nMaleki asked his questions to both crews of the desired class, but the crew said that the guest of this room \n\nnever allowed us to clean his room!",0.08,'white',1)
        dialoge("\n\n\n   Who are you continuing interrogation with?",'blue')
        answer=int(question("\n\n2: Hotel manager\n\n3: The person who reported the murde"))
        keyboard.read_key()
        if(answer==2):
            clear()
            textAnimation(f"\n\nThe hotel manager came to the interrogation room after being late and said that this guest had come to this hotel by his \nwife and they paid us a lot of money to keep them in the hotel.\n\nTheir wife is Armita Mohammadi! Maleki and {player_name} become a little suspicious and tell the hotel manager to stay at the hotel until further \nnotice Maleki calls the victim's wife but no results are obtained",0.08,'white',0)
            textAnimation("\n\nafter that, mr.Maleki searched for the reporter.\n\nThe reporter is not found, but his number is tracked and the detective is informed that the reported phone is in the hotel manager's room!\nMaleki orders the arrest of the manager, but the manager insists that he is innocent!",0.08,'white',0)
            textAnimation(f"\n\nMaleki continues his research and realizes that all the dialogues of the hotel staff and crew are similar\n\n and only the manager talks to them differently.\n\nIt seems that all the personnel have committed murder together, but this cannot be proven, so Mr.Maleki and {player_name} will continue their investigation to prove the truth of the case.",0.08,'white',0)
            dialoge("\n\n   What we should do now ?",'blue')
            answer=int(question("\n\n 1: Taking the victim's mobile phone and authenticating the body\n\n 2: Finding his acquaintances and necessary interrogations\n\n 3: Torture and severe interrogation of hotel staff"))
            keyboard.read_key()
            if(answer==1):
                clear()
                textAnimation("\n\nThe victim's mobile phone is checked\n\nbut there is no contact inside his phone!It seems that the mobile phone in the case of the victim is fake!\n\nMaleki and his assistant get stuck with a whole range of regional investigations and investigations,\n\n and the murder case is handed over to someone else.",0.08,'white',0)
                time.sleep(4)
                gameOver()
            elif (answer==2):
                clear()
                horrorSound()
                textAnimation("\n\nNo acquaintance is found and no result is obtained. Detectives do not have much time\n\nIf this does not work, the case may be closed or left to someone else\n\nbut within 5 hours, all the staff are seriously and interrogated, and finally one of them suddenly gets angry and admits \n\nthat all this was a dirty plan of the manager who wanted to get a new position!",0.08,'white',0) 
                textAnimation("\n\nMaleki tells him to explain more, I do not understand what you mean\n\nThe person says: The victim was none other than the manager of this hotel\n\nand he behaved and managed in such a way that all the staff and employees of the hotel were firstly deprived of their",0.08,'white',0)
                textAnimation("\n\nsalaries and secondly they were humiliated and not properly spoken to. They were never treated properly. And he did not approve of our\n\nsituation, he never consulted with us in any work, and he increased our working hours, but without additional pay. He did not give us any leave and we were completely disappointed to work inside this hotel",0.08,'white',0)
                textAnimation("\n\nuntil the deputy manager, who is the current manager, gathered us all and drew up a plan to kill the main manager, and the current manager is named Jafar Mohammadi. And by his order a person\n\ninforms the building manager at night that a customer is working with you in room 666! The manager goes into the room and kills his killer and leaves that text and changes the victim's mobile phone and leaves no trace of himself!",0.08,'white',0)
                textAnimation(f"\n\n{player_name} asks:\n\n   who is the killer?",0.08,'yellow',0)
                textAnimation("\n\nThe person says: the killer is all the hotel staff. Each of them hit the victim together to reduce their crime if identified, and according to the law\n\nnone of us will be tried because our crime is divided and reduced. Eventually, we will each go to prison for 3 months, but my suggestion to you is now that You know the truth",0.08,'white',0)
                textAnimation("\n\ndo not inform the center and close this case because this person has no friends, no wife and no children. He has no heir to divide his property and it goes directly to the government\n\nHis only contacts were the marketers, traders, his colleagues and ourselves",0.08,'white',0)
                textAnimation("\n\nMaleki, who understands the truth, closes the case and lights his cigarette in a cozy corner in room 666 and disappears watching the sentence on the wall ...",0.08,'white',0)
                time.sleep(6)
                win()
            elif (answer==3):
                clear()
                horrorSound()
                textAnimation("\n\nwithin 5 hours, all the staff are seriously and interrogated, and finally one of them suddenly gets angry and admits \n\nthat all this was a dirty plan of the manager who wanted to get a new position!",0.08,'white',0) 
                textAnimation("\n\nMaleki tells him to explain more, I do not understand what you mean\n\nThe person says: The victim was none other than the manager of this hotel\n\nand he behaved and managed in such a way that all the staff and employees of the hotel were firstly deprived of their",0.08,'white',0)
                textAnimation("\n\nsalaries and secondly they were humiliated and not properly spoken to. They were never treated properly. And he did not approve of our\n\nsituation, he never consulted with us in any work, and he increased our working hours, but without additional pay. He did not give us any leave and we were completely disappointed to work inside this hotel",0.08,'white',0)
                textAnimation("\n\nuntil the deputy manager, who is the current manager, gathered us all and drew up a plan to kill the main manager, and the current manager is named Jafar Mohammadi. And by his order a person\n\ninforms the building manager at night that a customer is working with you in room 666! The manager goes into the room and kills his killer and leaves that text and changes the victim's mobile phone and leaves no trace of himself!",0.08,'white',0)
                textAnimation(f"\n\n{player_name} asks who is the killer?",0.08,'yellow',0)
                textAnimation("\n\nThe person says: the killer is all the hotel staff. Each of them hit the victim together to reduce their crime if identified, and according to the law\n\nnone of us will be tried because our crime is divided and reduced. Eventually, we will each go to prison for 3 months, but my suggestion to you is now that You know the truth",0.08,'white',0)
                textAnimation("\n\ndo not inform the center and close this case because this person has no friends, no wife and no children. He has no heir to divide his property and it goes directly to the government\n\nHis only contacts were the marketers, traders, his colleagues and ourselves",0.08,'white',0)
                textAnimation("\n\nMaleki, who understands the truth, closes the case and lights his cigarette in a cozy corner in room 666 and disappears watching the sentence on the wall ...",0.08,'white',0)
                time.sleep(6)
                win() 
        elif (answer==3):
            clear()
            textAnimation("\n\nThe reporter is not found, but his number is tracked and the detective is informed that the reported phone is in the hotel manager's room!",0.08,'white',0)         
            textAnimation("\n\nMaleki orders the arrest of the manager, but the manager insists that he is innocent!",0.08,'white',0)
            textAnimation("\n\nMaleki continues his research and realizes that all the dialogues of the hotel staff and the crew are similar and only the manager talks to them differently.",0.08,'white',0)
            textAnimation("\n\nIt seems that all the personnel have committed murder together, but this cannot be proven, so he will continue his investigation to prove the truth of the case.",0.08,'white',0)
            dialoge("\n\n   What we should do now ?",'blue')
            answer=int(question("\n\n 1: Taking the victim's mobile phone and authenticating the body\n\n 2: Finding his acquaintances and necessary interrogations\n\n 3: Torture and severe interrogation of hotel staff"))
            keyboard.read_key()
            if(answer==1):
                clear()
                textAnimation("\n\nThe victim's mobile phone is checked\n\nbut there is no contact inside his phone!It seems that the mobile phone in the case of the victim is fake!\n\nMaleki and his assistant get stuck with a whole range of regional investigations and investigations,\n\n and the murder case is handed over to someone else.",0.08,'white',0)
                time.sleep(6)
                gameOver()
            elif (answer==2):
                clear()
                horrorSound()
                textAnimation("\n\nNo acquaintance is found and no result is obtained. Detectives do not have much time\n\nIf this does not work, the case may be closed or left to someone else\n\nbut within 5 hours, all the staff are seriously and interrogated, and finally one of them suddenly gets angry and admits \n\nthat all this was a dirty plan of the manager who wanted to get a new position!",0.08,'white',0) 
                textAnimation("\n\nMaleki tells him to explain more, I do not understand what you mean\n\nThe person says: The victim was none other than the manager of this hotel\n\nand he behaved and managed in such a way that all the staff and employees of the hotel were firstly deprived of their",0.08,'white',0)
                textAnimation("\n\nsalaries and secondly they were humiliated and not properly spoken to. They were never treated properly. And he did not approve of our\n\nsituation, he never consulted with us in any work, and he increased our working hours, but without additional pay. He did not give us any leave and we were completely disappointed to work inside this hotel",0.08,'white',0)
                textAnimation("\n\nuntil the deputy manager, who is the current manager, gathered us all and drew up a plan to kill the main manager, and the current manager is named Jafar Mohammadi. And by his order a person\n\ninforms the building manager at night that a customer is working with you in room 666! The manager goes into the room and kills his killer and leaves that text and changes the victim's mobile phone and leaves no trace of himself!",0.08,'white',0)
                textAnimation(f"\n\n{player_name} asks who is the killer?",0.08,'yellow',0)
                textAnimation("\n\nThe person says: the killer is all the hotel staff. Each of them hit the victim together to reduce their crime if identified, and according to the law\n\nnone of us will be tried because our crime is divided and reduced. Eventually, we will each go to prison for 3 months, but my suggestion to you is now that You know the truth",0.08,'white',0)
                textAnimation("\n\ndo not inform the center and close this case because this person has no friends, no wife and no children. He has no heir to divide his property and it goes directly to the government\n\nHis only contacts were the marketers, traders, his colleagues and ourselves",0.08,'white',0)
                textAnimation("\n\nMaleki, who understands the truth, closes the case and lights his cigarette in a cozy corner in room 666 and disappears watching the sentence on the wall ...",0.08,'white',0)
                time.sleep(6)
                win()
            elif (answer==3):
                clear()
                horrorSound()
                textAnimation("\n\nwithin 5 hours, all the staff are seriously and interrogated, and finally one of them suddenly gets angry and admits \n\nthat all this was a dirty plan of the manager who wanted to get a new position!",0.08,'white',0)  
                textAnimation("\n\nMaleki tells him to explain more, I do not understand what you mean\n\nThe person says: The victim was none other than the manager of this hotel\n\nand he behaved and managed in such a way that all the staff and employees of the hotel were firstly deprived of their",0.08,'white',0)
                textAnimation("\n\nsalaries and secondly they were humiliated and not properly spoken to. They were never treated properly. And he did not approve of our\n\nsituation, he never consulted with us in any work, and he increased our working hours, but without additional pay. He did not give us any leave and we were completely disappointed to work inside this hotel",0.08,'white',0)
                textAnimation("\n\nuntil the deputy manager, who is the current manager, gathered us all and drew up a plan to kill the main manager, and the current manager is named Jafar Mohammadi. And by his order a person\n\ninforms the building manager at night that a customer is working with you in room 666! The manager goes into the room and kills his killer and leaves that text and changes the victim's mobile phone and leaves no trace of himself!",0.08,'white',0)
                textAnimation(f"\n\n{player_name} asks who is the killer?",0.08,'yellow',0)
                textAnimation("\n\nThe person says: the killer is all the hotel staff. Each of them hit the victim together to reduce their crime if identified, and according to the law\n\nnone of us will be tried because our crime is divided and reduced. Eventually, we will each go to prison for 3 months, but my suggestion to you is now that You know the truth",0.08,'white',0)
                textAnimation("\n\ndo not inform the center and close this case because this person has no friends, no wife and no children. He has no heir to divide his property and it goes directly to the government\n\nHis only contacts were the marketers, traders, his colleagues and ourselves",0.08,'white',0)
                textAnimation("\n\nMaleki, who understands the truth, closes the case and lights his cigarette in a cozy corner in room 666 and disappears watching the sentence on the wall ...",0.08,'white',0)
                time.sleep(6)
                win()
                
    elif (answer==2):
        clear()
        textAnimation(f"\n\nThe hotel manager came to the interrogation room after being late and said that this guest had come to this hotel by his \nwife and they paid us a lot of money to keep them in the hotel.\n\nTheir wife is Armita Mohammadi! Maleki and {player_name} become a little suspicious and tell the hotel manager to stay at the hotel until further \nnotice Maleki calls the victim's wife but no results are obtained",0.08,'white',0)
        textAnimation("\n\nafter that, mr.Maleki searched for the reporter.\n\nThe reporter is not found, but his number is tracked and the detective is informed that the reported phone is in the hotel manager's room!\nMaleki orders the arrest of the manager, but the manager insists that he is innocent!",0.08,'white',0)
        textAnimation(f"\n\nMaleki continues his research and realizes that all the dialogues of the hotel staff and crew are similar\n\n and only the manager talks to them differently.\n\nIt seems that all the personnel have committed murder together, but this cannot be proven, so Mr.Maleki and {player_name} will continue their investigation to prove the truth of the case.",0.08,'white',0)            
        dialoge("\n\n   What we should do now ?",'blue')
        answer=int(question("\n\n 1: Taking the victim's mobile phone and authenticating the body\n\n 2: Finding his acquaintances and necessary interrogations\n\n 3: Torture and severe interrogation of hotel staff"))
        keyboard.read_key()
        if(answer==1):
            clear()
            textAnimation("\n\nThe victim's mobile phone is checked\n\nbut there is no contact inside his phone!It seems that the mobile phone in the case of the victim is fake!\n\nMaleki and his assistant get stuck with a whole range of regional investigations and investigations,\n\n and the murder case is handed over to someone else.",0.08,'white',0)
            time.sleep(6)
            gameOver()
        elif (answer==2):
                clear()
                horrorSound()
                textAnimation("\n\nNo acquaintance is found and no result is obtained. Detectives do not have much time\n\nIf this does not work, the case may be closed or left to someone else\n\nbut within 5 hours, all the staff are seriously and interrogated, and finally one of them suddenly gets angry and admits \n\nthat all this was a dirty plan of the manager who wanted to get a new position!",0.08,'white',0) 
                textAnimation("\n\nMaleki tells him to explain more, I do not understand what you mean\n\nThe person says: The victim was none other than the manager of this hotel\n\nand he behaved and managed in such a way that all the staff and employees of the hotel were firstly deprived of their",0.08,'white',0)
                textAnimation("\n\nsalaries and secondly they were humiliated and not properly spoken to. They were never treated properly. And he did not approve of our\n\nsituation, he never consulted with us in any work, and he increased our working hours, but without additional pay. He did not give us any leave and we were completely disappointed to work inside this hotel",0.08,'white',0)
                textAnimation("\n\nuntil the deputy manager, who is the current manager, gathered us all and drew up a plan to kill the main manager, and the current manager is named Jafar Mohammadi. And by his order a person\n\ninforms the building manager at night that a customer is working with you in room 666! The manager goes into the room and kills his killer and leaves that text and changes the victim's mobile phone and leaves no trace of himself!",0.08,'white',0)
                textAnimation(f"\n\n{player_name} asks who is the killer?",0.08,'yellow',0)
                textAnimation("\n\nThe person says: the killer is all the hotel staff. Each of them hit the victim together to reduce their crime if identified, and according to the law\n\nnone of us will be tried because our crime is divided and reduced. Eventually, we will each go to prison for 3 months, but my suggestion to you is now that You know the truth",0.08,'white',0)
                textAnimation("\n\ndo not inform the center and close this case because this person has no friends, no wife and no children. He has no heir to divide his property and it goes directly to the government\n\nHis only contacts were the marketers, traders, his colleagues and ourselves",0.08,'white',0)
                textAnimation("\n\nMaleki, who understands the truth, closes the case and lights his cigarette in a cozy corner in room 666 and disappears watching the sentence on the wall ...",0.08,'white',0)
                time.sleep(6)
                win()
        elif (answer==3):
                clear()
                horrorSound()
                textAnimation("\n\nwithin 5 hours, all the staff are seriously and interrogated, and finally one of them suddenly gets angry and admits \n\nthat all this was a dirty plan of the manager who wanted to get a new position!",0.08,'white',0) 
                textAnimation("\n\nMaleki tells him to explain more, I do not understand what you mean\n\nThe person says: The victim was none other than the manager of this hotel\n\nand he behaved and managed in such a way that all the staff and employees of the hotel were firstly deprived of their",0.08,'white',0)
                textAnimation("\n\nsalaries and secondly they were humiliated and not properly spoken to. They were never treated properly. And he did not approve of our\n\nsituation, he never consulted with us in any work, and he increased our working hours, but without additional pay. He did not give us any leave and we were completely disappointed to work inside this hotel",0.08,'white',0)
                textAnimation("\n\nuntil the deputy manager, who is the current manager, gathered us all and drew up a plan to kill the main manager, and the current manager is named Jafar Mohammadi. And by his order a person\n\ninforms the building manager at night that a customer is working with you in room 666! The manager goes into the room and kills his killer and leaves that text and changes the victim's mobile phone and leaves no trace of himself!",0.08,'white',0)
                textAnimation(f"\n\n{player_name} asks who is the killer?",0.08,'yellow',0)
                textAnimation("\n\nThe person says: the killer is all the hotel staff. Each of them hit the victim together to reduce their crime if identified, and according to the law\n\nnone of us will be tried because our crime is divided and reduced. Eventually, we will each go to prison for 3 months, but my suggestion to you is now that You know the truth",0.08,'white',0)
                textAnimation("\n\ndo not inform the center and close this case because this person has no friends, no wife and no children. He has no heir to divide his property and it goes directly to the government\n\nHis only contacts were the marketers, traders, his colleagues and ourselves",0.08,'white',0)
                textAnimation("\n\nMaleki, who understands the truth, closes the case and lights his cigarette in a cozy corner in room 666 and disappears watching the sentence on the wall ...",0.08,'white',0)
                time.sleep(6)
                win() 
    elif (answer==3):
        clear()
        textAnimation("The reporter is not found, but his number is tracked and the detective is informed that the reported phone is in the hotel manager's room!",0.08,'white',0)
        dialoge("\n\n   what is your idea? who is next?",'blue')
        answer=int(question("\n\n1: The crew cleaning the floor rooms\n\n2: Hotel manager"))
        if(answer==1):
            clear()
            textAnimation("\nMaleki asked his questions to both crews of the desired class, but the crew said that the guest of this room \n\nnever allowed us to clean his room!",0.08,'white',1)
            dialoge("\n\n\n   Who are you continuing interrogation with?",'blue')
            answer=int(question("\n\n2: Hotel manager"))
            keyboard.read_key()
            if(answer==2):
                clear()
                textAnimation(f"\n\nThe hotel manager came to the interrogation room after being late and said that this guest had come to this hotel by his \nwife and they paid us a lot of money to keep them in the hotel.\n\nTheir wife is Armita Mohammadi! Maleki and {player_name} become a little suspicious and tell the hotel manager to stay at the hotel until further \nnotice Maleki calls the victim's wife but no results are obtained",0.08,'white',0)
                textAnimation(f"\n\nMaleki continues his research and realizes that all the dialogues of the hotel staff and crew are similar\n\n and only the manager talks to them differently.\n\nIt seems that all the personnel have committed murder together, but this cannot be proven, so Mr.Maleki and {player_name} will continue their investigation to prove the truth of the case.",0.08,'white',0)
                dialoge("\n\n   What we should do now ?",'blue')
                answer=int(question("\n\n 1: Taking the victim's mobile phone and authenticating the body\n\n 2: Finding his acquaintances and necessary interrogations\n\n 3: Torture and severe interrogation of hotel staff"))
                keyboard.read_key()
                if(answer==1):
                    clear()
                    textAnimation("\n\nThe victim's mobile phone is checked\n\nbut there is no contact inside his phone!It seems that the mobile phone in the case of the victim is fake!\n\nMaleki and his assistant get stuck with a whole range of regional investigations and investigations,\n\n and the murder case is handed over to someone else.",0.08,'white',0)
                    time.sleep(4)
                    gameOver()
                elif (answer==2):
                    clear()
                    horrorSound()
                    textAnimation("\n\nNo acquaintance is found and no result is obtained. Detectives do not have much time\n\nIf this does not work, the case may be closed or left to someone else\n\nbut within 5 hours, all the staff are seriously and interrogated, and finally one of them suddenly gets angry and admits \n\nthat all this was a dirty plan of the manager who wanted to get a new position!",0.08,'white',0) 
                    textAnimation("\n\nMaleki tells him to explain more, I do not understand what you mean\n\nThe person says: The victim was none other than the manager of this hotel\n\nand he behaved and managed in such a way that all the staff and employees of the hotel were firstly deprived of their",0.08,'white',0)
                    textAnimation("\n\nsalaries and secondly they were humiliated and not properly spoken to. They were never treated properly. And he did not approve of our\n\nsituation, he never consulted with us in any work, and he increased our working hours, but without additional pay. He did not give us any leave and we were completely disappointed to work inside this hotel",0.08,'white',0)
                    textAnimation("\n\nuntil the deputy manager, who is the current manager, gathered us all and drew up a plan to kill the main manager, and the current manager is named Jafar Mohammadi. And by his order a person\n\ninforms the building manager at night that a customer is working with you in room 666! The manager goes into the room and kills his killer and leaves that text and changes the victim's mobile phone and leaves no trace of himself!",0.08,'white',0)
                    textAnimation(f"\n\n{player_name} asks who is the killer?",0.08,'yellow',0)
                    textAnimation("\n\nThe person says: the killer is all the hotel staff. Each of them hit the victim together to reduce their crime if identified, and according to the law\n\nnone of us will be tried because our crime is divided and reduced. Eventually, we will each go to prison for 3 months, but my suggestion to you is now that You know the truth",0.08,'white',0)
                    textAnimation("\n\ndo not inform the center and close this case because this person has no friends, no wife and no children. He has no heir to divide his property and it goes directly to the government\n\nHis only contacts were the marketers, traders, his colleagues and ourselves",0.08,'white',0)
                    textAnimation("\n\nMaleki, who understands the truth, closes the case and lights his cigarette in a cozy corner in room 666 and disappears watching the sentence on the wall ...",0.08,'white',0)
                    time.sleep(6)
                    win()
                elif (answer==3):
                    clear()
                    horrorSound()
                    textAnimation("\n\nwithin 5 hours, all the staff are seriously and interrogated, and finally one of them suddenly gets angry and admits \n\nthat all this was a dirty plan of the manager who wanted to get a new position!",0.08,'white',0) 
                    textAnimation("\n\nMaleki tells him to explain more, I do not understand what you mean\n\nThe person says: The victim was none other than the manager of this hotel\n\nand he behaved and managed in such a way that all the staff and employees of the hotel were firstly deprived of their",0.08,'white',0)
                    textAnimation("\n\nsalaries and secondly they were humiliated and not properly spoken to. They were never treated properly. And he did not approve of our\n\nsituation, he never consulted with us in any work, and he increased our working hours, but without additional pay. He did not give us any leave and we were completely disappointed to work inside this hotel",0.08,'white',0)
                    textAnimation("\n\nuntil the deputy manager, who is the current manager, gathered us all and drew up a plan to kill the main manager, and the current manager is named Jafar Mohammadi. And by his order a person\n\ninforms the building manager at night that a customer is working with you in room 666! The manager goes into the room and kills his killer and leaves that text and changes the victim's mobile phone and leaves no trace of himself!",0.08,'white',0)
                    textAnimation(f"\n\n{player_name} asks who is the killer?",0.08,'yellow',0)
                    textAnimation("\n\nThe person says: the killer is all the hotel staff. Each of them hit the victim together to reduce their crime if identified, and according to the law\n\nnone of us will be tried because our crime is divided and reduced. Eventually, we will each go to prison for 3 months, but my suggestion to you is now that You know the truth",0.08,'white',0)
                    textAnimation("\n\ndo not inform the center and close this case because this person has no friends, no wife and no children. He has no heir to divide his property and it goes directly to the government\n\nHis only contacts were the marketers, traders, his colleagues and ourselves",0.08,'white',0)
                    textAnimation("\n\nMaleki, who understands the truth, closes the case and lights his cigarette in a cozy corner in room 666 and disappears watching the sentence on the wall ...",0.08,'white',0)
                    time.sleep(6)
                    win()
        elif(answer==2):
            clear()
            textAnimation(f"\n\nThe hotel manager came to the interrogation room after being late and said that this guest had come to this hotel by his \n\nwife and they paid us a lot of money to keep them in the hotel.\n\nTheir wife is Armita Mohammadi! Maleki and {player_name} become a little suspicious and tell the hotel manager to stay at the hotel until further\n \nnotice Maleki calls the victim's wife but no results are obtained",0.08,'white',0)
            textAnimation("\n\nafter that, mr.Maleki searched for the reporter.\n\nThe reporter is not found, but his number is tracked and the detective is informed that the reported phone is in the hotel manager's room!\nMaleki orders the arrest of the manager, but the manager insists that he is innocent!",0.08,'white',0)
            textAnimation(f"\n\nMaleki continues his research and realizes that all the dialogues of the hotel staff and crew are similar\n\n and only the manager talks to them differently.\n\nIt seems that all the personnel have committed murder together, but this cannot be proven, so Mr.Maleki and {player_name} will continue their investigation to prove the truth of the case.",0.08,'white',0)
            dialoge("\n\n   What we should do now ?",'blue')
            answer=int(question("\n\n 1: Taking the victim's mobile phone and authenticating the body\n\n 2: Finding his acquaintances and necessary interrogations\n\n 3: Torture and severe interrogation of hotel staff"))
            keyboard.read_key()
            if(answer==1):
                clear()
                textAnimation("\n\nThe victim's mobile phone is checked\n\nbut there is no contact inside his phone!It seems that the mobile phone in the case of the victim is fake!\n\nMaleki and his assistant get stuck with a whole range of regional investigations and investigations,\n\n and the murder case is handed over to someone else.",0.08,'white',0)
                time.sleep(4)
                gameOver()
            elif (answer==2):
                clear()
                horrorSound()
                textAnimation("\n\nNo acquaintance is found and no result is obtained. Detectives do not have much time\n\nIf this does not work, the case may be closed or left to someone else\n\nbut within 5 hours, all the staff are seriously and interrogated, and finally one of them suddenly gets angry and admits \n\nthat all this was a dirty plan of the manager who wanted to get a new position!",0.08,'white',0) 
                textAnimation("\n\nMaleki tells him to explain more, I do not understand what you mean\n\nThe person says: The victim was none other than the manager of this hotel\n\nand he behaved and managed in such a way that all the staff and employees of the hotel were firstly deprived of their",0.08,'white',0)
                textAnimation("\n\nsalaries and secondly they were humiliated and not properly spoken to. They were never treated properly. And he did not approve of our\n\nsituation, he never consulted with us in any work, and he increased our working hours, but without additional pay. He did not give us any leave and we were completely disappointed to work inside this hotel",0.08,'white',0)
                textAnimation("\n\nuntil the deputy manager, who is the current manager, gathered us all and drew up a plan to kill the main manager, and the current manager is named Jafar Mohammadi. And by his order a person\n\ninforms the building manager at night that a customer is working with you in room 666! The manager goes into the room and kills his killer and leaves that text and changes the victim's mobile phone and leaves no trace of himself!",0.08,'white',0)
                textAnimation(f"\n\n{player_name} asks who is the killer?",0.08,'yellow',0)
                textAnimation("\n\nThe person says: the killer is all the hotel staff. Each of them hit the victim together to reduce their crime if identified, and according to the law\n\nnone of us will be tried because our crime is divided and reduced. Eventually, we will each go to prison for 3 months, but my suggestion to you is now that You know the truth",0.08,'white',0)
                textAnimation("\n\ndo not inform the center and close this case because this person has no friends, no wife and no children. He has no heir to divide his property and it goes directly to the government\n\nHis only contacts were the marketers, traders, his colleagues and ourselves",0.08,'white',0)
                textAnimation("\n\nMaleki, who understands the truth, closes the case and lights his cigarette in a cozy corner in room 666 and disappears watching the sentence on the wall ...",0.08,'white',0)
                time.sleep(6)
                win()
            elif (answer==3):
                clear()
                horrorSound()
                textAnimation("\n\nwithin 5 hours, all the staff are seriously and interrogated, and finally one of them suddenly gets angry and admits \n\nthat all this was a dirty plan of the manager who wanted to get a new position!",0.08,'white',0) 
                textAnimation("\n\nMaleki tells him to explain more, I do not understand what you mean\n\nThe person says: The victim was none other than the manager of this hotel\n\nand he behaved and managed in such a way that all the staff and employees of the hotel were firstly deprived of their",0.08,'white',0)
                textAnimation("\n\nsalaries and secondly they were humiliated and not properly spoken to. They were never treated properly. And he did not approve of our\n\nsituation, he never consulted with us in any work, and he increased our working hours, but without additional pay. He did not give us any leave and we were completely disappointed to work inside this hotel",0.08,'white',0)
                textAnimation("\n\nuntil the deputy manager, who is the current manager, gathered us all and drew up a plan to kill the main manager, and the current manager is named Jafar Mohammadi. And by his order a person\n\ninforms the building manager at night that a customer is working with you in room 666! The manager goes into the room and kills his killer and leaves that text and changes the victim's mobile phone and leaves no trace of himself!",0.08,'white',0)
                textAnimation(f"\n\n{player_name} asks who is the killer?",0.08,'yellow',0)
                textAnimation("\n\nThe person says: the killer is all the hotel staff. Each of them hit the victim together to reduce their crime if identified, and according to the law\n\nnone of us will be tried because our crime is divided and reduced. Eventually, we will each go to prison for 3 months, but my suggestion to you is now that You know the truth",0.08,'white',0)
                textAnimation("\n\ndo not inform the center and close this case because this person has no friends, no wife and no children. He has no heir to divide his property and it goes directly to the government\n\nHis only contacts were the marketers, traders, his colleagues and ourselves",0.08,'white',0)
                textAnimation("\n\nMaleki, who understands the truth, closes the case and lights his cigarette in a cozy corner in room 666 and disappears watching the sentence on the wall ...",0.08,'white',0)
                time.sleep(6)
                win()
                
# start game function
def startGame():
    backgroundSound("start")
    key_pressed=""
    while(key_pressed!='s'):
        key_pressed=keyboard.read_key()
    if(key_pressed=="s"):
        yousefHolmes()
        
# win game function
def win():     
    time.sleep(1)
    clear()
    pauseSounds()
    win_sound=pygame.mixer.Sound("./sounds/win.mp3")
    win_sound.set_volume(0.7)
    win_sound.play()
    print(render("WIN!",font="block",colors=['green','yellow'],align='center'))
    time.sleep(10)
    
#game over function
def gameOver():
    time.sleep(1)
    clear()
    pauseSounds()
    gameover_sound = pygame.mixer.Sound("./sounds/gameover.mp3")
    gameover_sound.set_volume(0.7)
    gameover_sound.play()
    print(render("Game Over!",font="block",colors=['red','yellow'],align='center'))
    time.sleep(10)

# start the game
startGame()
