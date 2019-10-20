from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address
from contextlib import contextmanager
import sys


class ContractDeployer:

    def __init__(self, address: str, port: int):
        self.api = LedgerApi(address, port)
        self.entity = Entity()
        # Create wealth so that we have the funds to be able to create contracts on the network
        self.api.sync(self.api.tokens.wealth(self.entity, 10000))
    
    def deploy(self, contract : str):
        """
        Deploy contract. Feeds back compilation errors.
        """
        try:
            contract = Contract(contract)
            with self.track_cost(self.api.tokens, self.entity, "Cost of creation: "):
                result = contract.create(self.api, self.entity, 4000)
                self.api.sync(result)
                return result
        except Exception as e:
            print(e)


    @contextmanager
    def track_cost(self, api: TokenApi, entity: Entity, message: str):
        """
        Context manager for recording the change in balance over a set of actions.
        Will be inaccurate if other factors change an account balance.
        """
        if isinstance(entity, Entity):
            entity = Address(entity)
        elif not isinstance(entity, Address):
            raise TypeError("Expecting Entity or Address")
        balance_before = api.balance(entity)
        yield
        if not message:
            message = "Actions cost: "
        print(message + "{} TOK".format(api.balance(entity) - balance_before))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 contract.py CONTRACT-STRING")
        exit(1)
    cd = ContractDeployer('127.0.0.1', 8000)
    cd.deploy(sys.argv[1])