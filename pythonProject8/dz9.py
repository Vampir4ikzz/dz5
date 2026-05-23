import random
import string
def random_letter_generator():
    letters = string.ascii_letters
    while True:
        yield random.choice(letters)
gen = random_letter_generator()
print("10 випадкових букв:")
for _ in range(10):
    print(next(gen), end=" ")