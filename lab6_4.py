def personal_info(name, age, company='unnamed'):
    print(f"Имя: {name}  Возраст: {age}  Компания: {company}")

gri = ("Григорий", 22)
personal_info(*gri)

geo = ("Георгий", 41, "Yandex")
personal_info(*geo)