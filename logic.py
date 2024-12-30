loop = 1

def work():
    return('25:00')

def short():
    return('5:00')
    
def long():
    return('15:00')
    

while True:
    print(work())
    if loop == 4:
        print(long())
        break
    else:
        print(short())
        loop += 1