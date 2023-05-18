### Hexlet tests and linter status:
[![Actions Status](https://github.com/baseven/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/baseven/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/3ec6a9e9fbb0ea763a95/maintainability)](https://codeclimate.com/github/baseven/python-project-49/maintainability)

## Описание
Набор консольных игр-викторин, где игроку предлагается ответить на три вопроса. Ответив на все правильно, игрок побеждает. Ошибка в ответе завершает игру.

## Список игр
```
1: brain-even

2: brain-calc

3: brain-gcd

4: brain-progression

5: brain-prime
```

## Предварительные требования
```
Python версии 3.6 или выше
pip версии 19 или выше
poetry версии 1.2.0 или выше
```

## Установка
Склонируйте репозиторий проекта локально
Создайте виртуальное окружение и установите зависимости
```
Make install
```
Выполните установку пакета в виртуальное окружение
```
Make build
Make package-install
```

## Запуск
Для запуска игры достаточно ввести ее имя, например:
```
brain-calc
```

## Описание игр:

### brain-even
"Проверка на четность". Пользователю показывается случайное число и ему нужно ответить yes, если число чётное, или no — если нечётное.
```
Question: 15
Your answer: no
Correct!
```
### brain-calc
"Калькулятор". Пользователю показывается случайное математическое выражение, которое нужно вычислить и записать правильный ответ.
```
Question: 4 + 10
Your answer: 14
Correct!
```
### brain-gcd
"Наибольший общий делитель (НОД)". Пользователю показывается два случайных числа и он должен вычислить и ввести наибольший общий делитель этих чисел.
```
Question: 25 50
Your answer: 25
Correct!
```
### brain-progression
"Арифметическая прогрессия". Пользователю показывается ряд чисел, образующий арифметическую прогрессию, заменив любое из чисел двумя точками. Пользователm должен определить это число.
```
Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 15
Correct!
```
### brain-prime
"Простое ли число?". Пользователю показывается случайное число и ему нужно ответить yes, если число простое, или no — если составное.

```
Question: 7
Your answer: yes
Correct!
```