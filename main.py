#практична робота
"""Напишіть функцію count_vowels(s), яка приймає
аргумент у вигляді рядка s та повертає кількість
голосних літер у цьому рядку. Напишіть код, що
демонструє роботу функції та показує кількість
голосних літер у деяких рядках."""

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

s1 = input('Введіть рядок англ. мовою: ')

print(count_vowels(s1))

#3
"""Напишіть функцію squares_list(lst), яка приймає
список lst чисел та повертає новий список зі
значеннями, які є квадратами елементів вхідного списку.
Напишіть код, що демонструє роботу функції та показує
список з квадратами елементів у деяких списках."""

def squares_list(lst):
    return [x**2 for x in lst]
lst1 = [1, 2, 3, 4, 5]
print(squares_list(lst1))

#4
def long_words(dictionary):
    return [word for word in dictionary if len(word) >= 5]
dict1 = {'apple': 'a fruit', 'carrot': 'a vegetable', 'python': 'a programming language', 'bike': 'a vehicle'}
print(long_words(dict1))
