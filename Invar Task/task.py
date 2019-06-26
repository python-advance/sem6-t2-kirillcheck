# Задание 1.1

value = int(input("Введите максимальное целое положительное число \t" ))

def fibb(el):
  """Вычисление ряда чисел Фибоначчи рекурсией. 
      Вызов функции самой себя
  """
  if el > 1:
    return fibb(el-1) + fibb(el-2)
  return el
for i in range(value):
  print(i, "=", fibb(i))
  
#ответ при value = 10:
# 0 = 0
# 1 = 1
# 2 = 1
# 3 = 2
# 4 = 3
# 5 = 5
# 6 = 8
# 7 = 13
# 8 = 21
# 9 = 34

  
# Задание 1.2

value = int(input("Введите максимальное целое положительное число \t" ))

def fib():
"""
Итератор - генератор
"""
    a, b = 0, 1
    while True:            # Первая итерация
      yield a              # yield 0 => начинаем с нуля
      a, b = b, a + b      # a теперь = 1, b будет также 1, (0 + 1)
    
for index, fib_num in zip(range(value), fib()):
    print('{i}: {f}'.format(i=index, f=fib_num))
    
# ответ при value = 10:
# 0: 0
# 1: 1
# 2: 1
# 3: 2
# 4: 3
# 5: 5
# 6: 8
# 7: 13
# 8: 21
# 9: 34

#Задание 1.2
def fib_iter(value):
  """
  Реализацция по примеру лекции "Оператор for с семантикой итераторов"
  """
  lst = [0, 1, ]
  it = iter(list(range(2, value)))
  while True:
    try:
      elem = next(it)
    except StopIteration:
      break
    n = lst[elem - 1] + lst[elem - 2]
    lst.append(n)
  return lst

value = int(input("Введите максимальное целое положительное число \t" ))
result = fib_iter(value)
print(result)

#Задание 1.2
from itertools import islice

def fib(a=0, b=1):
    yield a
    while True:
        yield b
        a, b = b, a + b

start = int(input("От какого числа просиходит счет \t" ))
end = int(input("До какого числа просиходит счет \t" ))

fib_num = list(islice(fib(), start, end))
print(fib_num)
