# BankTransaction.py


"""
MIS 15-01

This program simulates bank transactions by
having deposits, withdrawals, and transfers
available to the user for their specified
amounts. Transactions that overdraw the
account balance are rejected.
"""


def main():  # define main

    # declare booleans for transaction options
    checking = False
    savings = False
    deposit = False
    withdraw = False
    transfer = False

    # declare amounts to 0 for future transaction reference
    c_amount = 0
    s_amount = 0
    d_amount = 0
    w_amount = 0
    t_amount = 0
    finalAmount = 0

    # account type to get either checking or saving, turns into into uppercase
    accType = input("Enter the type of account (C = Checking, "
                     + "S = Savings): ").upper()

    # conditionals to see if the account is a valid checking or saving, reject if not valid
    if accType != "S" and accType != "C":
        print("\nSorry, the account type is invalid\n"), main()

    elif accType == "S":
        savings = True
        if savings: s_amount = float(input("Enter the initial balance in the account: "))

    elif accType == "C":
        checking = True
        if checking: c_amount = float(input("Enter the initial balance in the account: "))

    # transaction type similar to account type, gets the type of transaction and makes it uppercase
    transaction_type = input("Enter the type of transaction (D = Deposit, "
                             + "W = Withdraw, T = Transfer): ").upper()

    # conditionals on how to treat each individual transaction type
    if transaction_type == "D":
        deposit = True
        if deposit: d_amount = float(input("Enter the amount to Deposit: "))

    elif transaction_type == "W":
        withdraw = True
        if withdraw: w_amount = float(input("Enter the amount to Withdraw: "))

    elif transaction_type == "T":
        transfer = True
        if transfer: t_amount = float(input("Enter the amount to Transfer: "))

    # conditionals for checking acct with formulas incorporated to handle each transaction type

    if accType == "C" and transaction_type == "D":
        finalAmount = (float(c_amount) + float(d_amount))
        print("\nYour checking balance after the transaction:", "%.2f" % float(finalAmount)), exit()

    elif accType == "C" and transaction_type == "W":
        finalAmount = (float(c_amount) - float(w_amount))
        if finalAmount >= 0:
            print("\nYour checking balance after the transaction:", "%.2f" % float(finalAmount)), exit()
        if finalAmount < 0:
            print("\nSorry, the amount to be withdrawn cannot" +
                  " be more than the balance"), exit()

    elif accType == "C" and transaction_type == "T":
        finalAmount = (float(c_amount) - float(t_amount))
        if finalAmount < 0 and accType == "C" and transaction_type == "T":
            print("\nSorry, the amount transferred cannot" +
                  " be more than the balance"), exit()
        if finalAmount >= 0 and accType == "C" and transaction_type == "T":
            print("\n%.2f" % float(t_amount), "has been transferred into your savings, your"
                  + " checking balance is now", "%.2f" % float(finalAmount)), exit()

    # savings conditionals
    if accType == "S" and transaction_type == "D":
        finalAmount = (float(s_amount) + float(d_amount))
        print("\nYour savings balance after the transaction:", "%.2f" % float(finalAmount)), exit()

    elif accType == "S" and transaction_type == "W":
        finalAmount = (float(s_amount) - float(w_amount))
        if finalAmount >= 0:
            print("\nYour savings balance after the transaction:", "%.2f" % float(finalAmount)), exit()
        if finalAmount < 0:
            print("\nSorry, the amount to be withdrawn cannot" +
                  " be more than the balance"), exit()

    elif accType == "S" and transaction_type == "T":
        finalAmount = (float(s_amount) - float(t_amount))
        if finalAmount < 0 and accType == "S" and transaction_type == "T":
            print("\nSorry, the amount transferred cannot" +
                  " be more than the balance"), exit()
        if finalAmount >= 0 and accType == "S" and transaction_type == "T":
            print("\n%.2f" % float(t_amount), "has been transferred into your checking, your"
                  + " savings balance is now", "%.2f" % float(finalAmount)), exit()
    else:
        print("Invalid input"), main()


main()  # call main
