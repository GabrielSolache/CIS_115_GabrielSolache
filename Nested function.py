#Nested functions to demonstrat calling one functionform another
def print_message2():
#print a message indicating it was called form print_message1
print("i was called form print_message1")

def print_message1():
    #print a message and then call print_message2
    print ("I was called first")
    print_message2()