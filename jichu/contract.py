from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address


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

        with track_cost(api.tokens, entity1, "Cost of creation: "):
            api.sync(contract.create(api, entity1, 4000))


if __name__ == '__main__':
    cd = ContractDeployer()
    cd.main()