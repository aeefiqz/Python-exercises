def allSameValuesInSequence(numSeq):
    for x in range(0,len(numSeq)):
        if numSeq[x] == numSeq[x+1]:
            print(f"All numbers are the same in {numSeq}.")
        else:
            print(f"All numbers are different in {numSeq}")

def allDifferentValuesInSequence(numSeq):
    for x in range(0,len(numSeq)):
        if numSeq[x] != numSeq[x+1]:
            print(f"All numbers are different in {numSeq}")
        else:
            print(f"All numbers are the same in {numSeq}")

def readNumbers():
    numList = []
    while len(numList) < 2:        
        print("Please enter at least two numbers before ending input session")
        for _ in range(2):
            num = (input("Enter a number: "))
            if num == "":
                continue
            else:
                numList.append(int(num))
    return numList

def main():
    while True:
        print("Menu")
        print("1. Read another number sequence")
        print("2. Determine all numbers same")
        print("3. Determine all numbers different")
        print("0. Exit")
        numSeq = readNumbers()
        choice = int(input("Enter choice: "))
        if choice == 0:
            break
        elif choice == 1:
            numSeq = readNumbers() 
            print(numSeq)
        elif choice == 2:
            sameSeq = allSameValuesInSequence(numSeq)
            print(sameSeq)
        elif choice == 3:
            diffSeq = allDifferentValuesInSequence(numSeq)
            print(diffSeq)

    print("End program")
main()