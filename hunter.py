import random
import secrets
from web3 import Web3
from eth_keys import keys
from time import sleep
from datetime import datetime

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'

def log(txt):
    print('\n ' + colour_cyan + '  [TIMING]> [' + str(datetime.now()) + '] ----> ' + txt + '\n' + colour_reset)

count = 1

# Connect to a Binance Smart Chain node using RPC
w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org'))  # Example RPC endpoint, replace with your own

while True:
    ran = secrets.SystemRandom().randrange(1, 115792089237316195423570985008687907852837564279074904382605163141518161494336)
    myhex = "%064x" % ran
    private_key = myhex[:64]
    private_key_bytes = bytes.fromhex(private_key)
    public_key_hex = keys.PrivateKey(private_key_bytes).public_key
    public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
    bnbadd = keys.PublicKey(public_key_bytes).to_address()  # BNB address
    checksum_address = Web3.to_checksum_address(bnbadd)
    
    balance = w3.eth.get_balance(checksum_address)

    print("\n" + colour_cyan + "BNB Binance Smart Chain Scan : " + str(count) + colour_red +
          "\n""---DEVELOPER MR.K x MR.E---" + colour_cyan + 
          "\n""With Balance Checker" + colour_reset)  # Running Display Output
    print(colour_cyan + 'BNB Binance Smart Chain Address' + ' : ' + colour_red + checksum_address + colour_reset + "\n"'Balance = ' + str(balance))  # BNB Binance Smart Chain address display
    print(colour_cyan + 'PrivateKey' + ' : ' + colour_red + myhex + colour_reset + "\n""Date&Time: " + str(datetime.now()), '\n')  # Running Display Output

    if balance > 0:
        print("Matching Key ==== BNB Binance Smart Chain Address Found!!!\n PrivateKey: " + myhex)  # BNB Binance Smart Chain winner
        with open(u"winner.txt", "a") as f:
            f.write('\nPrivateKey (hex): ' + myhex)
            f.write('\n BNB Address: ' + checksum_address)
            f.write('\n==================================')

    count += 1
    sleep(0)# Add a delay to avoid hitting the API too frequently
