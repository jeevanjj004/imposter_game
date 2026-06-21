import random
player_details={}
no_player=int(input("ENTER THE NUMBER OF PLAYERS\n"))
words = [
    "Biriyani",
    "Chaya",
    "Puttu",
    "Pazham Pori",
    "Kothuku",
    "Palli",
    "Patta",
    "Auto",
    "Mundu",
    "Chappal",
    "Kuda",
    "Thenga",
    "Kappa",
    "Payasam",
    "Mobile",
    "Fan",
    "Torch",
    "Chool",
    "Lungi",
    "Meen"
]
for i in range(1,no_player+1):
        player_details[i]=input((f"name of {i} th player\n"))


while(1):
    
    imposter=random.randrange(1,no_player+1)
    print(f"you are the imposter {player_details[imposter]} player\n")

    current_word=random.choice(words)
    for i in range(1,no_player+1):
        if i==imposter:
            print(f" {player_details[i]} -->IMPOSTER\n")
        else:
            print(f" {player_details[i]} -->{current_word}\n")
    print("Reveal the Imposter\n Press 1\n")
    choice=int(input())
    if choice==1:
        print(f"{player_details[imposter]} is the IMPOSTER\n")
    else:
        print("choose a correct option\n")