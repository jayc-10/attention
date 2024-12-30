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
        
# work -> short-break -> work -> short-break -> work -> short-break -> work -> long-break
# 25:00 -> 5:00 -> 25:00 -> 5:00 -> 25:00 -> 5:00 -> 25:00 -> 15:00