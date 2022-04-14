from brownie import (
    network,
    accounts,
    config,
)
from web3 import Web3

LOCAL_FORKED_ENVIORMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_DEPLOYMENT_ENVIORNMENTS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_DEPLOYMENT_ENVIORNMENTS
        or network.show_active() in LOCAL_FORKED_ENVIORMENTS
    ):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
