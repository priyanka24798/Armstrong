# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(n):
        
        num = n
        sum = 0
        while(n > 0):
                m = n % 10
                sum = sum + m **3
                n = n//10
        if(sum == num):
                return True
        else:
                return False

        # Your code goes here


