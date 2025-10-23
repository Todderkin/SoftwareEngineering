def filter_words():
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    print("Исходный текст:")
    print(text)

    words = text.split()
    filtered_words = []

    for word in words:
        clean_word = ''.join(char for char in word if char.isalpha())

        if len(clean_word) >= 3 and len(clean_word) <= 8:
            filtered_words.append(word)

    result = ' '.join(filtered_words)

    print("\nТекст после фильтрации:")
    print(result)

    with open('filtered_text.txt', 'w', encoding='utf-8') as file:
        file.write(result)

filter_words()