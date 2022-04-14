from brownie import AndrazToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def deploy_andraz_token():
    my_account = get_account()
    andraz_token = AndrazToken.deploy(initial_supply, {"from": my_account})
    print(f"{andraz_token.name()} has been deployed as {andraz_token.symbol()} :)")


def main():
    deploy_andraz_token()
