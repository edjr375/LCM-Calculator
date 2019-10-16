print("LCM Calculator")

num1 = int(input("what is the first number? "))
num2 = int(input("what is the second number? "))

#creates lists of multiples for numbers 1 and 2
multi1 = [num1*x for x in range(1,21)]
multi2 = [num2*x for x in range(1,21)]
lcm = 0    
#compare multiples list for numbers 1 and 2, break the loop once 2 multiple match
for element in multi1:
    for ele in multi2:
        if ele == element:
         lcm = ele
         break
    if lcm > 0:
        break

#print ("multiples of " + str(num1) + "\n" + str(multi1))
#print ("multiples of " + str(num2) + "\n" + str(multi2)) 
print ("the LCM of " + str(num1) + " and " + str(num2) + " is " + str(lcm))
