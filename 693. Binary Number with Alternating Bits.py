n = 7
bin_str = ""

while n > 0:
    x = str(n%2)
    bin_str+=x
    n = n//2

print(bin_str)

i=0
while i < len(bin_str):
    if bin_str[i]=="0" and bin_str[i+1]=="0":
        print(False)
    elif bin_str[i]=="1" and bin_str[i+1]=="1":
        print(False)
    i+=1
    
    
print(True)