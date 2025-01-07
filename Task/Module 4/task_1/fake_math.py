def fake_divide(a,b):
    try:
        result = a / b
    except Exception as ex:
        result = f"Ошибка, {ex}"
    return result

def main():
    print(fake_divide(6,2))
    print(fake_divide(6,0))
if __name__ == '__main__':
    main()