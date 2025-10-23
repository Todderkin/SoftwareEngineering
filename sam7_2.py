def expense_tracker():
    expenses = []

    while True:
        print("1 - Добавить расход")
        print("2 - Посмотреть расходы")
        print("3 - Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            category = input("Категория: ")
            amount = input("Сумма: ")
            description = input("Описание: ")

            expense = f"{category} | {amount} руб. | {description}"
            expenses.append(expense)

            with open('expenses.txt', 'a', encoding='utf-8') as file:
                file.write(expense + '\n')

            print("Расход добавлен!")

        elif choice == '2':
            print("Все расходы:")
            for expense in expenses:
                print(expense)

        elif choice == '3':
            break

expense_tracker()