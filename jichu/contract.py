from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address
from contextlib import contextmanager


class ContractDeployer:

    def __init__(self, address: str, port: int):
        self.api = LedgerApi('127.0.0.1', 8000)
        self.entity = Entity()
        # Create wealth so that we have the funds to be able to create contracts on the network
        self.api.sync(self.api.tokens.wealth(self.entity, 10000))

        
    def main(self):

        sample_contract = """
            persistent sharded balance : UInt64;
            @init
            function setup(owner : Address)
            use balance[owner];
            balance.set(owner, 1000000u64);
            endfunction
            @action
            function transfer(from: Address, to: Address, amount: UInt64)
            use balance[from, to];
            
            // Check if the sender has enough balance to proceed
            if (balance.get(from) >= amount)
                // update the account balances
                balance.set(from, balance.get(from) - amount);
                balance.set(to, balance.get(to, 0u64) + amount);
            endif
            endfunction
            @query
            function balance(address: Address) : UInt64
                use balance[address];
                return balance.get(address, 0u64);
            endfunction
        """

        contract = Contract(sample_contract)

        with self.track_cost(self.api.tokens, self.entity, "Cost of creation: "):
            self.api.sync(contract.create(self.api, self.entity, 4000))


    @contextmanager
    def track_cost(self, api: TokenApi, entity: Entity, message: str):
        """
        Context manager for recording the change in balance over a set of actions
        Will be inaccurate if other factors change an account balance
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
    cd = ContractDeployer('127.0.0.1', 8000)
    cd.main()