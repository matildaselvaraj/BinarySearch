
# for-loop

for i in range(5):
    print(i)


# while-loop

i = 0
while i < 5:
    print(i)
    i = i + 1


# if

password = input("Skriv ditt lösenord:  ")

if password == "Nina":
    print("Välkommen!")


# if ... else

password = input("Skriv ditt lösenord:  ")

if password == "Nina":
    print("Välkommen!")
else:
    print("Fel lösenord")


# if ... elif ... else

password = input("Skriv ditt lösenord:  ")

if password == "Nina":
    print("Välkommen!")
elif password == "NINA":
    print("Har du caps lock på?")
else:
    print("Fel lösenord")
