name = input("Введите имя:")
surname = input("Введите фамилию:")
year = input("Введите год рождения:")
town = input("Введите город проживания:")
mail = input("Введите e-mail:")
phone = input("Введите номер телефона:")


def my_data(n, s, y, t, m, p):
    return (name, surname, year, town, mail, phone)


print(my_data(name, surname, year, town, mail, phone))
