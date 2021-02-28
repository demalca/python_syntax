def print_upper_words(words, must_start_with):
    """change words that start with specified letters to uppercase"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})
