def analyze_text():
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    lines = text.split('\n')
    words = text.split()

    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1

    print("Input file contains:")
    print(letters, "letters")
    print(len(words), "words")
    print(len(lines), "lines")

analyze_text()