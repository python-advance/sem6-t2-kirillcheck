# sem6-t2
## Лабораторная работа "Итераторы"

### Инвариантное задание
    2.1. Разработать функцию, возвращающую элементы ряда Фибоначчи по данному максимальному значению.
    2.2. Создание программы, возвращающей список чисел Фибоначчи с помощью итератора.
    2.3. Формирование отчета по практическому заданию и публикация его в портфолио.
    
### Вариативное задание
    2.1. Разработать функцию, возвращающую список чисел ряда Фибоначчи с использованием 
    бесконечных итераторов (модуль itertools).
    
### Лекционные данные 
    Основное назначение итераторов – это упрощение навигации по элементам объекта, который 
    представляет собой некоторую коллекцию (список, словарь и т.п.). Итератор представляет 
    собой объект перечислитель, который для данного объекта выдает следующий элемент, либо 
    бросает исключение, если элементов больше нет.

    Основное место использования итераторов – это цикл for.
    
    Генераторы — функции, которая использует не только оператор return, но и оператор yield. 
    В результате использования оператора yield работа функции приостанавливается, а не прерывается 
    (как при использовании return). Когда у вас в функции есть yield, то это не функция, а генератор.
    
    Протокол итератора состоит из двух методов:

        1) метод __iter__ возвращает экземпляр класса, реализующего протокол итераторов, например, self;
        2) метод __next__ возвращает следующий по порядку элемент итератора. Если такого элемента нет, 
           то выбрасывается специальное исключение StopIteration. Важное замечание по поводу метода __next__: 
           если метод поднял исключение StopIteration, то все последующие его вызовы также должны поднимать 
           это же исключение (когда мы его реализовываем)
           
           Каждый вызов next() делает две важные вещи:
               - модифицирует внутреннее состояние объекта;
               - возвращает следующий элемент последовательности.
