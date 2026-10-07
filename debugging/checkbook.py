#!/usr/bin/python3
import random
import os

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def get_amount(prompt):
    """Get a valid positive number from the user."""
    while True:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("Please enter an amount greater than zero.")

            else:
                return amount

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    cb = Checkbook()

    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        ).strip().lower()

        if action == 'exit':
            print("Goodbye!")
            break

        elif action == 'deposit':
            amount = get_amount("Enter the amount to deposit: $")
            cb.deposit(amount)

        elif action == 'withdraw':
            amount = get_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
