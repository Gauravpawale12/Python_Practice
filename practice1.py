# Write a code to divide two numbers

def DivideNumber(No1,No2):
        try:
            return No1 / No2
            
            
        except ZeroDivisionError:
            print("Cannot divide by 0")
            return None
            

def main():
    No1 = 0
    No2 = 0

    print("Enter First number :")
    No1 = int(input())

    print("Enter Second Number :")
    No2 = int(input())

    Ret = DivideNumber(No1,No2)
    print("Division is : ",Ret)
if __name__ == "__main__":
    main()