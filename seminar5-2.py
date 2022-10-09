#Создайте программу для игры с конфетами человек против человека.

from random import *
import os
message = ['твой ход']

candies_total=2021
max_candys_per_round=28
count = 0
player1='игрок 1'
player2='игрок 2'

x=randint(1,2)
if x==1:
  first_player=player1
  second_player=player2
else:
  first_player=player2
  second_player=player1

print (f"Первым ходит {first_player} ")

while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {first_player} = '))
            if step > candies_total or step > max_candys_per_round:
                step = int(input(
                    f'\n Максимум можно взять {max_candys_per_round} конфет {first_player}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 1
        else:
            print('Игра закончена')

        if count == 1:
            step = int(input(f'\n{choice(message)}, {second_player} '))
            if step > candies_total or step > max_candys_per_round:
                step = int(input(
                    f'\nМаксимум можно взять {max_candys_per_round} конфет {first_player}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 0
        else:
            print('Игра закончена')

if count == 1:
        print(f'{second_player} ПОБЕДИЛ')
if count == 0:
        print(f'{first_player} ПОБЕДИЛ')


def player_vs_bot():
    candies_total = 2021
    max_candys_per_round = 28
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print('\nОпределим кто первый ходит\n')

    first_player = randint(-1, 0)

    print(f'Поздравляю {players[first_player+1]} ты ходишь первым !')

    while candies_total > 0:
        first_player += 1

        if players[first_player % 2] == 'Компьютер':
            print(
                f'\nХодит {players[first_player%2]} \nНа кону {candies_total}. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                calculation = candies_total//28
                step = candies_total - ((calculation*max_candys_per_round)+1)
                if step == -1:
                    step = max_candys_per_round -1
                if step == 0:
                    step = max_candys_per_round
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nДелаем ход,  {players[first_player%2]} \nНа кону {candies_total} {choice(message)}:  '))
            while step > max_candys_per_round or step > candies_total:
                step = int(input(f'\nМаксимум можно взять {max_candys_per_round} конфет {first_player}, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'На кону осталось {candies_total} \nПобедил {players[first_player%2]}')

player_vs_bot()