#4
"""Задано словник зі словами та їх значеннями. Напишіть
функцію long_words(dictionary), яка приймає цей
словник та повертає список всіх слів, що містять не менше
ніж 5 символів (не забудьте оператор return). Напишіть
код, що демонструє роботу функції та показує список слів
у деяких словниках."""

def long_words(dictionary):
    return [word for word in dictionary if len(word) >= 5]
dict1 = {'apple': 'a fruit', 'carrot': 'a vegetable', 'python': 'a programming language', 'bike': 'a vehicle'}
print(long_words(dict1))
