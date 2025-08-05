
class MyMath:

    def __init__(self):
        self.pi = self.find_pi()

    def is_even(self, num):
        # Return True if num is even, otherwise, return False
        # x is boolean
        # Write your code here
        if num%2==0:
            return True
        return False

    def fac(self, num):
        # Return the factorial of the number (n!)
        # x is an integer
        # Write your code here
        if num==0 or num==1:
            return 1
        return num*self.fac(num-1)

    def is_prime(self, num):
        # Return True if num is a prime number, otherwise, return False
        # x is boolean
        # Write your code here
        for i in range(2,num//2):
            if num%i==0:
                return False
        return True

    def divide_by(self, num, k):
        # Return True if num is divisible by k, otherwise, return False
        # x is boolean
        # Write your code here
        if num%k==0:
            return True
        return False

    def ten_to_bi(self, num):
        # Return the binary presentation of the number
        # x is an integer or string
        # Write your code here
        res=""
        while num>0:
            res=str(num%2)+res
            num//=2
        
        return res

    def ten_to_oct(self, num):
        # Return the octal presentation of the number
        # x is an integer or string
        # Write your code here
        res=""
        while num>0:
            res=str(num%8)+res
            num//=8
        
        return res

    def ten_to_sixteen(self, num):
        res=""
        alphabet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while num>0:
            res=alphabet[num%16]+res
            num//=16
        return res

    def int_to_roman(self, num):
        # Return the roman numerical presentation of num
        # x is a string
        # Write your code here
        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400],["D", 500],["CM", 900],["M", 1000]]
        res=""
        for key,value in reversed(symList):
            if num//value:
                count=num//value
                res+=count*key
                num=num%value      
        return res

    def find_pi(self):
        # Return PI value using Nilkantha's series
        # x is a float
        # Write your code here
        res=3
        sign=1
        n=2
        for i in range(53):
            res+= (sign*(4/((n)*(n+1)*(n+2))))
            sign= sign*-1
            n+=2
            
        return res


# DO NOT SUBMIT THIS CODE, FOR PROGRAM TESTING ONLY

my_math = MyMath()
num = int(input("Please Enter Number : "))
k = int(input("Divide by? : "))

if my_math.is_even(num): print('This number is even number.')
else: print('This number is not even number.')

if num <= 20: print(f'factorial is {my_math.fac(num):,.0f}.')
else: print('factorial TOO LONG')

if my_math.is_prime(num): print('This number is a prime number.')
else: print('This number is not a prime number.')

if my_math.divide_by(num,k): print(f'{num} is divisible by {k}')
else: print(f'{num} is not divisible by {k}')

print(f'{num} is {my_math.ten_to_bi(num)} in base 2.')
print(f'{num} is {my_math.ten_to_oct(num)} in base 8.')
print(f'{num} is {my_math.ten_to_sixteen(num)} in base 16.')
print(f'{num} is {my_math.int_to_roman(num)} in roman numeral system.')
print(f'PI is {my_math.pi:.30f}')