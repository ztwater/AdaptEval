# Program to convert degree to Degree, Minutes and Seconds
# Using try and except for int data validations
try:

    # Requesting input degree from user
    print ("degree to Degree Minutes seconds converter ". upper ())
    degree = float(input ("\nEnter Degree: "))
    
    # Casting input from float to int 
    degree_d = int(degree)
    
    # Working on minutes
    minute =60 * (degree - degree_d)
    minutes = int(minute)
    
    # Working on seconds
    second = 60 * (minute - minutes)
    # Rounding seconds to whole number 
    seconds= round(second)
    
    # print 
    print (f"\nThe Answer In Degree-Minutes-Seconds are: \n{degree_d}°{minutes}'{seconds}\"  ✓\n ") 


#Except

except ValueError:
    print ("Wrong Input ")
