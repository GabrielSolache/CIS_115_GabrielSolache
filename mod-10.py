def validatecreditcatd(ccNum):
    #remove space form the input to handle number entered with space
    ccNum = ccNum.replace(" "," ")

    #check if the input contains only digits
    if not ccNum.isdigit():
        return False
    #covert each charater into an integer to create a list of digit
    digits = [int(d) for d in ccNum]
    #starting form the second-to-last digit,moving left,double evey other digit
    for i in range (len(digits)-2, -1, -2):
        doubled = digits[i] * 2

        #if doubling result in a number greater than 9,subtract 9 (same as adding the two digits)
        if doubled > 9:
            doubled -= 9
        
        #replace the original digit with the procesed value
        digits = sum(digits)

    #sum all the digits
    total = sum(digits)
    
    #if the total moudulo 10 is zero, the card is valid
    return total / 10 == 0
#loop untill a valid  credit card number is entered
while True:
    #prompt user to enter a credit card number
    ceNum = input("enter credit card number: ")

    #call the validation funtion
    if validatecreditcatd(ceNum):
        #if valid, print success message and exit loop
          print(f"The credit card number {ceNum} is valid!")
          break
    else:
        #if valid, print succese message and exit loop
        print(f"Invalid credit card entered, please try again.")