<p align="center">
    <img src="./img/jichu.png" width="170" />
    <br><br>
    <b>Jichu: Infura for Fetch.AI</b>
    <br><br>
    <a href="https://github.com/fetchai" alt="Fetch.AI">
        <img src="./img/fetch.svg" />
    </a>
    <a href="https://github.com/fetchai/ledger" alt="Mainnet">
        <img src="./img/net.svg" />
    </a>
    <a href="https://github.com/OutlierVentures" alt="Convergence">
        <img src="./img/convergence.svg" />
    </a>
    <br><br>
    'Jichu' means foundation in Mandarin Chinese.<br>
    <i>An app in the Convergence Stack.</i>
</p>


## Install

```Bash
pip3 install .
```

## Run

```Bash
cd jichu
python3 api.py
```

The UI is now hosted on port 5000.

Jichu can be pointed at a Fetch node in the UI. This works with the alphanet: try `diffusion.fetch.ai`. To point to a local deployment, spin up a node and point Jichu at `127.0.0.1`.

Get and spin up a node:

```Bash
./scripts/install.sh
./scripts/node.sh
```
