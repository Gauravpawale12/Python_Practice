# Accept one number from user and check whether it is divisible by 5 

def CheckDivisible(No):
    if No % 5 == 0:
        return True
    else:
        return False

def main():

    No = 0
    print("Enter the number:")
    No = int(input())

    Ret = CheckDivisible(No)
    if Ret == True:
        print(No,"is divisible by 5")
    else:
        print(No,"is NOT divisible by 5")
if __name__ == "__main__":
    main()