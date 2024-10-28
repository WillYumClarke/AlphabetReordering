import random

# Original string
alphabet = "abcdefghijklmnopqrstuvwxyz"
combinations = 100000

with open("alphabets.txt", "w") as file:
    for _ in range(combinations):
        shuffled = list(alphabet)      # Convert string to list for shuffling
        random.shuffle(shuffled)       # Shuffle the list in place
        file.write("".join(shuffled) + "\n")   # Join list to string and write to file

print("10 random combinations written to newalpha.txt")
