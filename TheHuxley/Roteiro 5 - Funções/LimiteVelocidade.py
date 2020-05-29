def multa(num):
    if(50*1.1 >= num > 50 ):
        multa = 230.00
    elif(50*1.1 < num <= 50*1.2):
        multa = 340.00
    elif(num > 50*1.2):
        multa = 19.28*(num-50)
    else:
        multa = 0
    return multa
print("%.2f"%multa(int(input())))