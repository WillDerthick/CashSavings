#! /usr/bin/env python3

import pickle

CurrentBalance = pickle.load(open("Balance.dat", "rb"))

print("How much would you like to deposit?")
Deposit = int(input())

Goal = 950
TotalBalance = CurrentBalance + Deposit
X100 = TotalBalance / Goal
PercentageToGoal = X100 * 100

print("Your new balance is " + str(TotalBalance) + ".")
print("You are " + str(PercentageToGoal) + " percent of the way to your goal.")

pickle.dump(TotalBalance, open("Balance.dat", "wb"))






