# homework3
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

print ("Введите количество элементов массива:")
n = int(input())
a = []
print ("Введите элементы массива:")
for i in range (1, n+1):
    i = int(input())
    a.append(i)
print ("Введите x:")    
for x in a:
    x = int(input())
    print("Количество х в массиве:", a.count(x))

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

print ("Введите количество элементов массива:")
n = int(input())
a = []
dictel = {}
print ("Введите элементы массива:")
for i in range (1, n+1):
    i = int(input())
    a.append(i)
print ("Введите x:")
x = int(input())
for keys in list(a):
    while i < x:
        distance = x - i
        keys, values = i, distance
        dictel[keys] = values
        i+=1 
        keys+=1
print(min(dictel))


# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае 
# с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость 
# введенного пользователем слова. Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

dict2 = {"A, E, I, O, U, L, N, S, T, R" :1, 
         "D, G," :2, 
         "B, C, M, P" :3, 
         "F, H, V, W, Y" :4,
         "K" :5,
         "J, X" :8,
         "Q, Z" :10} 
print ('Insert a word:')
word = input()
list1 = []
list1.extend(word)
for letters in list1:
    sum1 = [letters[dict2.values]]
    print(sum1)

# word = input()
# def word_cost(word):
#     total_cost = 0
#     for characters in word:
#         total_cost += word_cost.get(characters) 
#     return total_cost

# def get_cost(char):
#     char_costs = {
#         1: ["A, E, I, O, U, L, N, S, T, R"], 
#         2: ["D, G"], 
#         3: ["B, C, M, P"], 
#         4: ["F, H, V, W, Y"],
#         5: ["K"],
#         8: ["J, X"],
#         10: ["Q, Z"]
#     }
#     for cost in char_costs:
#         if char in char_costs[cost]:
#             return cost 
#     return 0

# print(word_cost)
