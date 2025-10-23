from collections import Counter

def analyze_article():
    with open('sam7_1.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    words = text.split()
    total_words = len(words)

    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)[0]

    print("Количество слов в статье:", total_words)
    print("Самое частое слово:", most_common_word[0])
    print("Оно встречается", most_common_word[1], "раз")


analyze_article()