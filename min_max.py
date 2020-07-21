# Find the smallest and largest numbers
# This allows the user to enter a list of numbers until the user types done or press enter then the prompt would stop
# Author: Impulse98



inputs = []                                   #empty array to store user input
smallest = None                               #None allows you to find the smallest value when relying on user input
largest = None                                #None allows you to find the largest value when relying on user input

print("When done adding numbers type 'done')

####################################################################################

while True:                                   #Infinite loop allowing the user to add as much input as they want
    sval = input("Enter a number: ")
    if sval == 'done' :                       #breaks loop when user types in 'done'
        break
    try:                                      #test to see if it is an interger or a float
        fval = float(sval)

    except:                                   #Prints 'Invalid input' if an integer is not added
        print('Invalid input')
        continue
    try:                                      #adds integer into the array
        inputs.append(int(sval))
    except:adds float to the array
        inputs.append(float(sval))
        
####################################################################################   

    for value in inputs:                      #loops through array
    
        if smallest is None:                  #checks to find the smallest value
            smallest = value
        elif value < smallest :
            smallest = value
  
        if largest is None:                   #checks to find the largest value in array
            largest = value
        elif value > largest:
            largest = value
            
####################################################################################  
            
                                              #Prints out the largest and smallest value
print("Smallest:", smallest)
print("Largest:", largest)

