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