from random import randint,choice
import art

instagram_account = ["Pratyay","Rohit","Kaustubh","Kunal","Yash","Gaurav","Atharva","Sarvesh","Vijay","Avinash"]
instagram_followers = []

for i in range(10):
    followers = randint(100000,5000000)
    instagram_followers.append(followers)

instagram = {}
for i in range(10):
    instagram[instagram_account[i]]=instagram_followers[i]



def higher_lower_game():
    score = 0
    right_answer = True
    
    A = choice(instagram_account)
    B = choice(instagram_account)
    # index1 = randint(0,9)
    # index2 = randint(0,9)
    # A = instagram_account[index1]
    # B = instagram_account[index2]

    # instagram_followers[index1] > instagram_followers[index2]
    while(right_answer):
            
        print(f"Compare A: {A}")
        print(art.vs)
        print(f"Compare B: {B}")
        answer = input("Who have more number of followers A or B: ")
        if answer == "A" and (A > B):
            score+=1
            print(f"Your score is: {score}")
            A = B
        elif answer == "B" and (A < B):
            score+=1
            print(f"Your score is: {score}")
            A = B
        else:
            right_answer = False
            print(f"Your final score is: {score}")

        while(A == B):
             B = choice(instagram_account)
            # index2 = randint(0,9)
            # B = instagram_account[index2]
            
    

play_game = True

while(play_game):
    print(art.logo)
    higher_lower_game()
    choice = input("Do you want to play it again Y or N: ")
    if(choice == "N"):
        play_game = False
    
    
