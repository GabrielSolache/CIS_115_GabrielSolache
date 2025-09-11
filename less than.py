x = int (input("Enter a number"))
y = int (input("Enter second number"))
diff = x - y 
print(diff)
if diff < 0:
    print("Invalid! The value is less than 0")
else:
    print("The values entered were valid integers")