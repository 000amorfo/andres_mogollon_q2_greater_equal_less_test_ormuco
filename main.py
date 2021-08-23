def analizeNumber(n1, n2):
    if(n1 > n2):
        return str(n1) + " is greater than " + str(n2)
    elif (n1 < n2):
        return str(n2) + " is greater than " + str(n2)
    else:
        return "they are equal"

def askForData():
    print("insert number 1")
    n1 = input()
    print("insert number 2")
    n2 = input()
    try:
        return float(n1), float(n2)
    except Exception as e:
        print("please do use just numbers")
        askForData()


if __name__=='__main__':
    n1, n2 = askForData()
    print(analizeNumber(n1,n2))
