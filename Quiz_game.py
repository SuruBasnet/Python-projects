a = input("Enter your name: ")
score = 0

#Greetings
print(f"Welcome {a} to our quiz game.Here, we will ask you 5 quiz questions and if you guess them right then you get a score.And if you are able to get 5 total scores you will get a car.")
input("Press enter to start the game")

# Questions
def quiz():
    q1 = input("Who is the inventor of telephone?: ")
    q2 = input("Which is the biggest continent of the world?: ")
    q3 = input("Which country has the flag in shape of two triangles?: ")
    q4 = input("Who is known as the light of Asia?: ")
    q5 = input("What is the altitude of sagarmatha?: ")

#Setting the asnwers
    qa = q1.lower()
    qb = q2.lower()
    qc = q3.lower()
    qd = q4.lower()
    qe = q5.lower()

    qa = qa.replace(" ","")
    qb = qb.replace(" ","")
    qc = qc.replace(" ","")
    qd = qd.replace(" ","")
    qe = qe.replace(" ","")

# Answers and checkinng
    if qa == "alexandergrahambell":
        score+=1

    if qb == "asia":
        score+=1

    if qc == "nepal":
        score += 1

    if qd == "gautambuddha" or qd == "buddha":
        score += 1

    if qe == "8848" or qe == "8848m":
        score += 1

quiz()

print(f"{a} your total score in this quiz is: {score}")  
print("And you will not get a car")  
print("Thank you for playing")
g = input("Do you want to play again?(Type Yes/No): ")
if g == "Yes":
    quiz()
elif g == "No":
    print("Thank you for playing")

