import getpass

print("You can only type : Rock or Paper or Scissor")

p1 = getpass.getpass("P1 Enter your hand: ")
p2 = getpass.getpass("P2 Enter your hand: ")



def func(a,b):
    if a == "Rock" and b == "Scissor":
        g = print(f"Player 1 wins (p1 = Rock p2 = Scissor)")
    elif b == "Rock" and a == "Scissor":
        g = print("Player 2 wins (p1 = Scissor p2 = Rock)")
    if a == "Rock" and b == "Paper":
        g = print("Player 2 wins (p1 = Rock p2 = Paper)")
    elif b == "Rock" and a == "Paper":
        g = print("Player 1 wins (p1 = Paper p2 = Rock)")
    if a == "Paper" and b == "Scissor":
        g = print("Player 2 wins (p1 = Paper p2 = Scissor)")
    elif b == "Paper" and a == "Scissor":
        g = print("Player 1 wins (p1 = Scissor p2 = Paper)")
    if a == "Rock" and b == "Rock":
        g = print("Tie (p1 and p2 = Rock)")
    if a == "Scissor" and b == "Scissor":
        g = print("Tie (p1 and p2 = Scissor)")
    if a == "Paper" and b == "Paper":
        g = print("Tie (p1 and p2 = Paper)")
    return g

func(p1,p2)
        