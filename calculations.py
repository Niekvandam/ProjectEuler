def custom_pow(num, pow):
    initialNum = num
    for i in range(pow - 1):
        num = num * initialNum
    return num