A = int(input("Give starting point number: "))
B = int(input("Give ending point number: "))
C = int(input("Give step number: "))

if A < B:
    print(A)
    while A + C < B:
        A = A + C
        print(A)
elif A > B:
    print(A)
    while A - C > B:
        A = A - C 
        print(A)
else:
    print(A)