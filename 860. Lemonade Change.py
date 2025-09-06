bills = [10,10]
fives=0
tens=0

for bill in bills:
    if bill==5:
        fives+=1
    elif bill==10:
        if fives>=1:
            fives-=1
            tens+=1
    else:
        if tens>=1 and fives>=1:
            fives-=1
            tens-=1
        elif fives>=3:
            fives-=3
        else:
            False

print(True)