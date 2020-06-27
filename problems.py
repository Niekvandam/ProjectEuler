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


## TODO Fix some recursive exception
def problem18():
    global high
    triangle = open('problem18')
    contents = triangle.readlines()
    triangle = []
    for i in contents:
        array = i.split()
        result = map(int, array)
        triangle.append(list(result))
    triangle = triangle[::-1]
    def getHighestValues(newtriangle):
        global high
        for idx, row in enumerate(newtriangle[1:]):
            temp = []
            for idy, number in enumerate(row):
                value1 = number + triangle[idx][idy]
                value2 = number + triangle[idx][idy+1]
                temp.append(max(value1, value2))
            del triangle[idx]
            del triangle[idx]
            triangle.insert(0, temp)
            if len(triangle) == 1:
                high = triangle[0][0]
            getHighestValues(triangle)
    try:
        getHighestValues(triangle)
    # TODO fix indexerror, if thrown the algorithm is done
    except IndexError:
        return high

