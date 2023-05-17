import math


print("Практическая работа #5 по теории вероятностей, Вариант 12")
# Исходные данные
input_arr = [0.41, 1.63, -1.53, -0.2, 0.85, 0.09, 1.54, 0.25, 1.24, -0.26,
            1.08, 0.42, -0.92, 0.91, 1.15, -0.82, 0.26, 0.96, 1.57, 0.72]
input_arr.sort()
n = len(input_arr)
m = 0 # мат ожидание
m2 = 0 # мат ожидание от x^2
acc_freq = [0] # накопленная частота
rel_freq = [] # относительная частота
# Вариационный ряд
prev = None
print("Вариационный ряд:\nxi\tfi\tОтносительная частота")
for i in range(n):
    fi = input_arr.count(input_arr[i])
    m += input_arr[i]*fi/n
    m2 += fi/n * input_arr[i]**2
    if input_arr[i] == prev: continue
    rel_freq.append(fi/n)
    acc_freq.append(round(acc_freq[-1]+fi/n, 2))
    print(f'{input_arr[i]}\t{fi}\t{fi/n}')
# Экстремальные значения и размах
print(f'\nx_min: {input_arr[0]}')
print(f'x_max: {input_arr[-1]}')
print(f'R: {input_arr[-1]-input_arr[0]}')
# Мат ожидание и среднеквадратическое отклонение
print(f'M(X): {m}')
d = m2-m**2
print(f'D(X): {d}')
sig = math.sqrt(d)
print(f'σ: {sig}')
# Эмирическая функция
print('\nF(x) = ')
j = 0
for i in range(len(acc_freq)):
    print(f'{acc_freq[i]}, ', end='')
    if i == 0:
        print(f'x < {input_arr[0]}')
    elif i == len(acc_freq)-1:
        print(f'x > {input_arr[-1]}')
    else:
        j_next = j
        while input_arr[j_next] == input_arr[j]:
            j_next += 1
        print(f'{input_arr[j]} < x <= {input_arr[j_next]}')
        j = j_next

# График этой функции
from matplotlib import pyplot as plt 
x = []
for val in input_arr:
    if val not in x:
        x.append(val)
x = [input_arr[0]] + x
plt.step(x, acc_freq)
plt.show()
# Гистограмма и полигон приведённых частот
x = []
x2 = []
y = []
h = (input_arr[-1]-input_arr[0])/len(input_arr)
ii = input_arr[0]
while ii < input_arr[-1]+h:
    x2.append(ii+h/2)
    x.append(ii)
    y.append(0)
    ii += h
j = 1
for i in range(n):
    while input_arr[i] > x[j]:
        j += 1
    y[j-1] += 1

del y[-1]
del x2[-1]

plt.stairs(y,x)
plt.show()
plt.plot(x2, y)
plt.show()
