'''
Calculate sum and multiplication of two numnbers

'''
def DisplaySum(No1,No2):
    Sum = No1 + No2
    return Sum

def DisplayMult(No1,No2):
    Mult = No1 * No2
    return Mult

def main():
    No1 = int(input("Enter the first number :"))
    No2 = int(input("Enter the second number :"))

    sRet = DisplaySum(No1,No2)
    print("Sum is ",sRet)

    mRet = DisplayMult(No1,No2)
    print("Sum is ",mRet)
if __name__ == "__main__":
    main()