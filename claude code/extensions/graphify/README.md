# Casing Graphify Extension For Claude Code

Using `graphify` project to reduce `claude code` tokens usage.

More about `graphify`:
* [Official home page](https://graphify.com/)
* [Gub repo](https://github.com/Graphify-Labs/graphify)
* [Installation page (pip)](https://pypi.org/project/graphifyy/)

## Prerequisites
Please refer to the `prerequisites` segment in `core/README.md`

## Build
Build docker image using this command
```bash
cd "claude code/extensions/graphify"
docker compose build --progress=plain
```

Validate your build (you should see `casing/graphify-claude:v1.0` image in the list)
```bash
docker image ls
```

## Run
Use the `docker compose` to start your `claude code` with `Casing`

```bash
cd "claude code/extensions/graphify"
docker compose up -d
```

## Verify
### Stratup
Check the logs of the extended container, using the following command:
```bash
docker compose logs -f
```
The first lines should indicate that an installation of `graphify` took place
```
installing graphify...
graphify installed
```
### Graphify Integration
From your `claude code` terminal, hit the `/graphify` command ans ensure it is recognized. For a full reference of commands, please check out the [reference section](https://pypi.org/project/graphifyy/) in the offical `github` repository.