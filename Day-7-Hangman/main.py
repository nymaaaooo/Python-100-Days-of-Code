from stages import logo, stages
from word_list import word_list
import random
# from replit import clear

print(logo)

# Таах үгийг random -оор сонгох
randomWord = random.choice(word_list)
# print(randomWord)

# Үгийн урт
wordLen = len(randomWord) 

characters = []
end_of_game = False

# Таах оролдлогын тоо
live = len(stages) - 1

# Үгийн уртыг тодорхойлох тэмдэгт
for _ in range(wordLen):
    characters += "_"

# Үндсэн процесс
while not end_of_game:
    guessLetter = input("Үсгээ оруулна уу: ")

    for position in range(wordLen):
        letter = randomWord[position]

        if guessLetter == letter:
            characters[position] = letter
    
    if guessLetter not in randomWord:
        live -= 1
        if live == 0:
            end_of_game = True
            print(f"Чи үгийг тааж чадсангүй, {randomWord} гэсэн үг байсан.")

    # Жагсаалтын бүх элементүүдийг нэгтгэж, мөр болгон хувиргах.
    print(f"{' '.join(characters)}")

    if "_" not in characters:
        end_of_game = True
        print("Чи үгийг тааж чадлаа, Баяр хүргэе!")

    print(stages[live])

