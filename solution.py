# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(n):
        
        
        sum = 0
        while(n > 0):
                m = n % 10
                sum = m **2
                n = n//10
        if(sum == n):
                return True
        else:
                return False

        # Your code goes here


