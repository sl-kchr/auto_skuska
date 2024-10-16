#  Замикання
def outer(x):
    def inner(y):
        print(f'{x} + {y} = {x+y}')
    return inner

def get_cach(cache=None):
    if cache is None:
        cache = {}
    def inner(n):
        print(cache)
        if n not in cache:
            cache[n] = sum([i for i in range(1, n+1)])
            print('hard work')
            return cache[n]
        else:
            print('Easy work')
            return cache[n]
    return inner

def main():
    data = {}
    calc = get_cach(data)
    print(calc(5))
    print(calc(5))
    print(calc(10))
    print(calc(5))
if __name__=='__main__':
    main()