youtuber = "Arsalan Khan"

print("\nSubscribe to " + youtuber)
print("Subscribe to {}".format(youtuber))
print(f"Subscribe to {youtuber}")


def main():
    print("\nWelcome to the Mad Libs game!")

    # Prompt the user for various types of words
    adjective1 = input("\nEnter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adverb1 = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")

    # Create the story template with placeholders
    story = f"""
    Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} {adverb1}.
    One day, it found a {adjective2} {noun2} and decided to take it home.
    """

    # Display the completed story
    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main()
