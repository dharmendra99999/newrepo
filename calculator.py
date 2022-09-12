def add(A,B):
    return A + B

def subtract(A,B):
    return A - B

def multiply(A,B):
    return A * B

def divide(A,B):
    return A/B

print("Please select the operation you want to perform")
print("1.add\n2.subtract\n3.multiply\n4.divide")

choice = input("Please enter the choice (1/2/3/4) :")

num_1 = int (input ("Please enter the first number: "))    
num_2 = int (input ("Please enter the second number: "))  

if choice == '1':
    print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
elif choice == '2':    
    print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
    
elif choice == '3':    
    print (num_1, " * ", num_2, " = ", multiply(num_1, num_2)) 
    
elif choice == '4':    
    print (num_1, " / ", num_2, " = ", divide(num_1, num_2))
    
else:    
    print ("This is an invalid input")  
