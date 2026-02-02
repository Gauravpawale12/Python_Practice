'''
Accept a number from user and check whether the 
number is even or odd 
'''

def CheckEvenOdd(Num):
    if Num % 2 == 0:
        return True
    else:
        return False
def main():
    Num = int(input("Enter the number :"))

    Ret = CheckEvenOdd(Num)
    if Ret == True:
        print("Number is Even")
    else:
        print("Number is Odd")
if __name__ == "__main__":
    main()