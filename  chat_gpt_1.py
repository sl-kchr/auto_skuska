from pathlib import Path
p = Path('HW_2.txt')
p.write_text('60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5')

def get_cats_info(path):
    cats_info = {}
    cats_data = []
    path = Path(path)

    try:
        if path.exists():
            if path.stat().st_size != 0:
                path = path.read_text()
                lines = path.splitlines()
                for i in lines:
                    i = i.split(',')
                    cats_info.update({"id":(i[1]), "name":(i[1]), "age": (i[2])})
                    cats_data.append(cats_info)
                print( cats_data)
            else:
                print('Файл порожній')
        else:
            print('На жаль, файл не був знайдений')
    except FileNotFoundError:
        print('На жаль, файл не був знайдений')
get_cats_info('HW.txt')