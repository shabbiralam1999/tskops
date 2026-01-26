i = int(input("Enter Your Value: "))
for i in range(1,3000):
    if i // 3 == 0:
        print("Fizz")
    elif i // 5 == 0:
        print("Buzz")   
    else:
        print("Just Print The Number Itself.") 
    break