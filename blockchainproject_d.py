# -*- coding: utf-8 -*-

#Project Starts:

"""we will be using "hash function " to create fingerprints for each transactions , the hash function will link each out block chain to other block . To make this easier to use, we’ll define a helper function to wrap the python hash function that we’re using"""

import hashlib,json,sys

def hashMe(msg=""):
    # For convenience, this is a helper function that wraps our hashing algorithm
    if type(msg)!=str:
        msg = json.dumps(msg,sort_keys=True)  # If we don't sort keys, we can't guarantee repeatability!
        
    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(msg).hexdigest(),'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()

"""Next, we want to create a function to generate exchanges between vinny and kinny. We’ll indicate withdrawals with negative numbers, and deposits with positive numbers. We’ll construct our transactions to always be between the two users of our system, and make sure that the deposit is the same magnitude as the withdrawal- i.e. that we’re neither creating nor destroying money."""

import random
random.seed(0)

def makeTransaction(maxValue=3):
    # This will create valid transactions in the range of (1,maxValue)
    sign      = int(random.getrandbits(1))*2 - 1   # This will randomly choose -1 or 1
    amount    = random.randint(1,maxValue)
    vinnyPays = sign * amount
    kinnyPays   = -1 * vinnyPays
    # By construction, this will always return transactions that respect the conservation of tokens.
    # However, note that we have not done anything to check whether these overdraft an account
    return {u'Vinny':vinnyPays,u'kinny':kinnyPays}

"""lets create transcations

"""

txnBuffer = [makeTransaction() for i in range(30)]



