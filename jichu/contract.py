from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address
from contextlib import contextmanager


class ContractDeployer:


        
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

        # create our first private key pair
        entity1 = Entity()
        address1 = Address(entity1)

        # build the ledger API
        api = LedgerApi('127.0.0.1', 8000)

        # create wealth so that we have the funds to be able to create contracts on the network
        api.sync(api.tokens.wealth(entity1, 10000))

        # create the smart contract
        contract = Contract(sample_contract)

        with self.track_cost(api.tokens, entity1, "Cost of creation: "):
            api.sync(contract.create(api, entity1, 4000))


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
    cd = ContractDeployer()
    cd.main()