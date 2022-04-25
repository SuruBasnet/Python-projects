# List of Users in Bank

users = [("hari", 1234), ("ram", 2244)]
balance = {
    "1234" : '22,000' ,
    "2244" : '3,00,000'
}

# Checking the username and pin.

def check(username, pin):
    for i in users:
        if username in i and pin in i:
            return True
        else:
            return False
            
# Logging in
            
def Login():
    print("Welcome to Mind Risers ATM")
    a = input("Enter your username: ")
    b = int(input("Enter your pin number: "))
    c = check(a,b)
    if c == True:
        print("Login success")
        print(f"Your balance is: {balance.get(str(b))}")
    elif c == False:
        print("Login failed (Try again)")
        Login()

Login()