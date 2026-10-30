guesses = []
print("PROGRAM STARTED")
while True:
    word = input("guess? ")
    print("You entered:", word)
    sentence = "hello"

    if word in sentence:
        guesses.append(word)

    print("Guesses:", guesses)

    for letter in sentence:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()

    print()