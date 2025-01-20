def num2binary(num: int) -> str:
    if num == 0:
        return '0'


    num_binary = ''
    while num != 0:
        num_binary += str(num%2)
        num //= 2

    return  num_binary[::-1]


if __name__ == '__main__':
    print(num2binary(12))