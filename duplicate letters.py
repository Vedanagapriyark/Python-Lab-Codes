def check_duplicate_letters(sentence):
    sentence = sentence.lower().replace(" ", "")  # Ignore case and spaces
    seen = set()
    for char in sentence:
        if char in seen:
            return True
        seen.add(char)
    return False

# Input
sentence = input("Enter a sentence: ")

# Output
if check_duplicate_letters(sentence):
    print("The sentence contains duplicate letters.")
else:
    print("The sentence does not contain duplicate letters.")

OUTPUT:
Enter a sentence: helloe everyone
The sentence contains duplicate letters.
