basic_a = range(0,151)
for i in basic_a:
    print(i)

mult_of_five = range(0,1005,5)
for i in mult_of_five:
    print(i)

div_five = range(1,101)
for i in div_five:
    if i%10==0:
        print("Coding Dojo")
    elif i%5 ==0:
        print("Coding")
    else:
        print(i)

thats_huge = range(0,500000)
num = 0
for i in thats_huge:
    if i % 3 == 0:
        num += i
print(num)

#count down by 4
for i in range(2018,0,-4):
    print(i)

#Flexible Counter
def flexible_counter(lowNum, highNum, mult):
    for lowNum in range(1,highNum):
        if lowNum % mult == 0:
            print(lowNum)

flexible_counter(2, 10, 3)