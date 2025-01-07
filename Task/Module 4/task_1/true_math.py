from math import inf

def true_divide(a,b):
    try:
        result = a / b
    except Exception:
        result = inf
    return result

def main():
    print(true_divide(6,0))
    print(true_divide(6,2))
    print(true_divide(6, inf))
if __name__ == '__main__':
    main()
