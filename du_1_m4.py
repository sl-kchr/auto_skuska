
from pathlib import Path
path = Path('HW_4.txt')
path.write_text('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000')

with open('txt.txt', 'w') as fh:
    # Виконання операцій з файлом
    fh.write('')



def total_salary(path):
    salary = []
    sum_salary = 0
    num_of_w = 0
    avarege_salary = 0
    
    path = Path(path)
    read_path = path.read_text()
    line_path = read_path.splitlines()

    for i in line_path:
        num_of_w +=1
        j = i.split(',')
        if len(j) > 1:
            salary.append(j[1])
    for k in salary:
        sum_salary += int(k)
    
    avarege_salary =sum_salary/num_of_w

    print(f"Загальна сума заробітної плати: {sum_salary}, Середня заробітна плата: {avarege_salary}")

total_salary(path)
