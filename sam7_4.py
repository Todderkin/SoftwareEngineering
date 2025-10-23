def replace_bad_words():
    with open('input.txt', 'r', encoding='utf-8') as file:
        bad_words = file.read().split()

    text = input("Введите предложение: ")

    for word in bad_words:
        start = 0
        while True:
            pos = text.lower().find(word, start)
            if pos == -1:
                break

            stars = '*' * len(word)
            text = text[:pos] + stars + text[pos + len(word):]
            start = pos + len(stars)

    print("Результат:")
    print(text)

replace_bad_words()