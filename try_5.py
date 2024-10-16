

def hello_male(name):
    print(f'Mr. {name}')

def hello_female(name):
    print(f'Mrs. {name}')

def hello_pan(name):
    print(f'Pan {name}')

MODES = {
    'm':hello_male,
    'f':hello_female,
    'p':hello_pan
}

def greeting(mood):
    return MODES[mood]


def main():
    mr = greeting('m')
    mrs = greeting('f')
    pan = greeting('p')

    mrs('Slava')
if __name__ == '__main__':
    main()