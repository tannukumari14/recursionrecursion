def powers(number):
    if number==1:
        return 1
    return 2 * powers(number-1)
i=1
while(i<5):
    print(powers(i))
    i+=1