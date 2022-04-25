marks = {}

a = input("Enter your name: ")
a1 = int(input("Enter your total marks obtained: "))
b = input("Enter your name: ")
b1 = int(input("Enter your total marks obtained: "))
c = input("Enter your name: ")
c1 = int(input("Enter your total marks obtained: "))
d = input("Enter your name: ")
d1 = int(input("Enter your total marks obtained: "))

marks[a] = a1
marks[b] = b1
marks[c] = c1
marks[d] = d1

f = 0
g = 0
h = 0
k = 0
for i in marks:
    if marks.get(i) > f:
        f = marks.get(i)
        f1 = (i)
for i in marks:
    if marks.get(i) > g and marks.get(i)<= f:
        g = marks.get(i)
        g1 = i
for i in marks:
    if marks.get(i) > h and marks.get(i) <= g:
        h = marks.get(i)
        h1 = i
for i in marks:
    if marks.get(i) > k and marks.get(i) < h:
        k = marks.get(i)
        k1 = i

print("In first position is: " , f1)
print("In second position is: " , g1)
print("In third position is: " , h1)
print("In last position is: " , k1)