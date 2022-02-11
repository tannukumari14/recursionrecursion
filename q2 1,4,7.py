def pattern(number):
    if number == 1:
        return 1
    else:
        return pattern(number-1) + 3
i=1
while i<10:
    print(pattern(i))
    i=i+1