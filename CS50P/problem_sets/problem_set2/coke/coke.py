# Prompt user to insert a coin, one at a time, inform user of amound due each time. Output change owed after atleast 50 cents is inserted

def main():
    amount_due = 50
    while amount_due > 0:
        # While an amount is due:
        print("Amount Due: ", amount_due)
        coin = (int(input("Instert Coin: ")))
        # if coin is valid
        if 25 >= coin > 0:
            amount_due = amount_due - coin
    # if amound due is less than or equal to zero
    if amount_due <= 0:
        # change is the absolute value of amount due
        change = int(amount_due / -1)
        # print change owed
        print("Change Owed: ", change)

main()