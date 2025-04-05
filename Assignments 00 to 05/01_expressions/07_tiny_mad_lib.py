def main():
    adjective = input("Please type an adjective and press enter: ").lower()
    noun = input("Please type a noun and press enter: ").lower()
    adverb = input("Please type an adverb and press enter: ").lower()
    SENTENCE = f"😆 The {adjective} {noun} ran {adverb} into a wall, then pretended it was on purpose."
    print(SENTENCE)
   
if __name__ == '__main__':
    main()