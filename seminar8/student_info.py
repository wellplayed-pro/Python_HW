import pandas as pd

print('----'*30)
print('Табель учащихся в средней школе # 1252')

stud_card = {
        'ID': ['01','02','03','04','05'],
        'Имя' : ['Иван','Петр','Василий','Сидор','Аркадий'],
        'Фамилия': ['Иванов','Петров','Васильев','Сидоров','Аркадьев'],
        'Дата рождения' : ['07.12.2000','04.02.2003','01.05.1999','25.02.2002','06.03.2004'],
        'Успеваемость' : ['Троечник','Троечник','Отличник','Отличник','Хорошист']
}
    
sc = pd.DataFrame(data = stud_card)

with open('students.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{sc}')
        cl.write('\n')
    
print(sc)
