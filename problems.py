from calculations import custom_pow


def problem16():
    result = 0
    target = custom_pow(2, 1000)
    nums = [int(i) for i in str(target)]
    for num in nums:
        print(num)
        result += num
    return result


def problem17():
    insertion = 'and'
    base = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    misc = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    decimals = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hundred = 'hundred'
    thousand = 'thousand'
    result = ''
    for i in range(1, 1001):
        array = [int(j) for j in str(i)]
        if len(array) == 1:
            result += str(base[i])
        if len(array) == 2:
            if array[0] == 1:
                result += str(misc[array[1]])
            else:
                result += str(decimals[array[0] - 2] + base[array[1]])
        if len(array) == 3:
            if array[1] == 0:
                if array[2] == 0:
                    result += str(base[array[0]] + hundred)
                else:
                    result += str(base[array[0]] + hundred + insertion + base[array[2]])
            elif array[1] == 1:
                result += str(base[array[0]] + hundred + insertion + misc[array[2]])
            else:
                result += str(base[array[0]] + hundred + insertion + decimals[array[1] - 2] + base[array[2]])
        if len(array) == 4:
            result += 'onethousand'
    print(len(result))


def problem18():
    triangle = open('problem18')
    contents = triangle.readlines()
    triangle = []
    for i in contents:
        array = i.split()
        result = map(int, array)
        triangle.append(list(result))
    for i in triangle:
        print(list(i))

    for
