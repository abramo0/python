#small and simple program that asks the user
# to enter the value of which he wants to calculate the percentage
# and the value of the percentage itself and returns the result


def percentage(val, perc):
    #percentage calculation
    result=val*perc/100
    return result


def inserisci_valore():
    #Asks the user to enter a value and a percentage.
    val=float(input("Write the value you want to calculate the percentage of: "))
    perc=float(input("Write the percentage: "))
    return val, perc


def main():
    val, perc=inserisci_valore()
    result=percentage(val, perc)
    print(f'{perc}% of {val} is worth {result}')

if __name__=="__main__":
    main()