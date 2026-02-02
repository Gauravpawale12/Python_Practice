# Accept two numbers from user and
# Display first number in second number of times 
# input : 12    5
# output : 12   12  12  12  12

def Display(First_No,Second_No):
    while Second_No != 0:
        print(First_No,end="\t")
        Second_No -= 1
def main():
    FirstNum = int(input("Enter first number :"))
    SecondNum = int(input("Enter second number :"))

    Display(FirstNum,SecondNum)


if __name__ == "__main__":
    main()