def FloatToInt(num):
    if num % 1 == 0:
        return int(num)
    else:
        return num
print(FloatToInt(float(input())))