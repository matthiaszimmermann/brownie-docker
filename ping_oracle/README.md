# experimenting with simple oracle

## start local ganache

check running containers
```bash
docker ps -a
```

if no container ganache is running start it as shown below
```bash
docker run -d -p 7545:7545 --name ganache brownie ganache-cli \
    --mnemonic "candy maple cake sugar pudding cream honey rich smooth crumble sweet treat" \
    --chainId 1234 \
    --port 7545 \
    -h "0.0.0.0"
```

## run the oracle api node

open a different shell and cd into the ping_oracle directory and start a brownie container.

```bash
cd ping_oracle
docker run -p 8000:8000 -it --rm -v $PWD:/projects brownie
```

in the brownie container start the oracle node

```bash
brownie networks add Local ganache host=http://host.docker.internal:7545 chainid=1234

export MNEMONIC="candy maple cake sugar pudding cream honey rich smooth crumble sweet treat"
uvicorn oracle.api:app --log-level info --host 0.0.0.0 --reload
```

the api is not available in the browser [http://localhost:8000/docs](http://localhost:8000/docs)


## use brownie console with local ganache

in the other shell start another brownie container

```bash
docker run -it --rm -v $PWD:/projects brownie
```

compile the player contract, add the ganche network and start a browine console

```bash
brownie compile --all

brownie networks add Local ganache host=http://host.docker.internal:7545 chainid=1234
brownie console --network ganache
```

## create setup

in the brownie console set up 2 player contracts
```bash
acc = accounts.from_mnemonic('candy maple cake sugar pudding cream honey rich smooth crumble sweet treat')

p1 = Player.deploy('#1', {'from': acc})
p2 = Player.deploy('#2', {'from': acc})

p1.setOpponent(p2)
p2.setOpponent(p1)

p1.address
p2.address
```

in browser api add the two player addresses [via POST players endpoint](http://localhost:8000/docs#/default/set_players_players_post)


start the "game"
```bash
p1.move(3)
```

in the oracle api shell window log messages with the observed on-chain event data should now have appeared.
```bash
INFO:root:id='(42,0,0)' address='0x9F544a3Fc3D1045e6ec49D4ecEF6dCD700457165' event='LogMove' args={'player': '#1', 'call': 3, 'moves': 9}
INFO:root:id='(42,0,1)' address='0xcfeD223fAb2A41b5a5a5F9AaAe2D1e882cb6Fe2D' event='LogMove' args={'player': '#2', 'call': 2, 'moves': 5}
INFO:root:id='(42,0,2)' address='0x9F544a3Fc3D1045e6ec49D4ecEF6dCD700457165' event='LogMove' args={'player': '#1', 'call': 1, 'moves': 10}
```

the same events should now be provided by the [GET events endpoint](http://localhost:8000/docs#/default/get_players_players_get)
