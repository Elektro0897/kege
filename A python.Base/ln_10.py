from timeit import timeit

def delete_vowels(text):
    new_word = ''
    for i in text:
        if i in 'euioaEUIOA':
            continue
        else:
            new_word += i

def delete_vowels2(text):
    new_word = ''
    for i in text:
        if i not in 'euioaEUIOA':
            new_word += i

data = input()
time1 = timeit('delete_vowels(data)', globals=globals(), number=10000)
time2 = timeit('delete_vowels2(data)', globals=globals(), number=10000)
print(time1)
print(time2)