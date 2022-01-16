# Get dollar amount

def getAmount():
    while True:
        try:
            amount = float(input("Enter a monetary amount. "))
            return amount
        except ValueError:
            print("Please enter a proper monetary amount!")
            continue


def findCoinTypes(coinTypes, amount):
    dollarAmount = amount[0]
    decimalAmount = amount[1]
    wholeNumCoins = [i for i in coinTypes if coinTypes[i] % 1 == 0]
    nonWholeNumCoins = [i for i in coinTypes if coinTypes[i] % 1 != 0]
    totalCounts = {}
    for coin in wholeNumCoins:
        if dollarAmount != 0:
            coinCalculations = []
            coinValue = coinTypes[coin]
            coinCalculations.append(int(dollarAmount / coinValue))
            valueOfCoins = coinCalculations[0] * coinValue
            coinCalculations.append(valueOfCoins)
            dollarAmount -= valueOfCoins
            totalCounts[coin] = coinCalculations
        else:
            totalCounts[coin] = [0, 0]
    """ for coin in coinTypes:
        coinCalculations = []
        coinValue = coinTypes[coin]
        coinNum.append(int(manipulatedAmount / coinValue))
        valueOfCoins = coinNum[0] * coinValue
        coinNum.append(valueOfCoins)
        manipulatedAmount -= valueOfCoins
        print(coinNum) """
    return totalCounts


def main():
    amount = [int(i) for i in str(getAmount()).split(".")]
    print(amount)
    types = {"Dollar": 1.00, "Quarter": 0.25, "Dime": 0.10, "Nickel": 0.05, "Penny": 0.01}
    print(findCoinTypes(types, amount))


if __name__ == "__main__":
    main()
