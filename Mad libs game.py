#Mad libs game
import os
FILENAME = "Mad_lib_stories.txt"
while True:
    noun_1 = input("Choose a noun: ")
    verb = input("Choose a verb (infinitive): ")
    adjective = input("Choose an adjective: ")
    color = input("Choose a color: ")
    place = input("Choose a place: ")
    noun_2 = input("Choose a second noun: ")
    story = (
        f"Today I woke up and realized I'm just a {noun_1}. "
        f"I decided to go to the {place} in search of a purpose, "
        f"but all I found was this {color} {adjective} {noun_2} "
        f"that likes to {verb}."
    )
    print(story)
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(story + "\n")
    play_again = input("Want to play again? (y/n) ").lower().strip()
    if play_again == "n":
        break
    