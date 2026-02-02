'''
write a program which accept number from user and print even factors
of that number 

'''
def EvenFactors(No):
    for icnt in range(1,No):
        if No % icnt == 0:
            if icnt % 2 == 0:
                print(icnt)
def main():
    No1 = int(input("Enter the number :"))
    EvenFactors(No1)
if __name__ == "__main__":
    main()