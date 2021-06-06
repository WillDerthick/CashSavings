#! /usr/bin/env python3

import pickle

CurrentBalance = 0

pickle.dump(CurrentBalance, open("Balance.dat", "wb"))
