# Casing Extension For Claude Code

Like to exetnd the basic implementation of `claude code` with `Casing`? Use this project as a template

## Prerequisites
Please refer to the `prerequisites` segment in `core/README.md`

## Build
Build docker image using this command
```bash
cd "claude code/extensions/base"
docker compose build --progress=plain
```

Validate your build (you should see `casing/extend-claude:v1.0` image in the list)
```bash
docker image ls
```

## Run
Use the `docker compose` to start your `claude code` with `Casing`

```bash
cd "claude code/extensions/base"
docker compose up -d
```

## Verify
### Stratup
Check the logs of the extended container, using the following command:
```bash
docker compose logs -f
```
The first lines should indicate that a `pre-load` hook logic is triggered
```
pre-load hook start
REPLACE THIS WITH YOU CUSTOM LOGIC...
pre-load hook complete
```
### Environment
From your `claude code` terminal, type the following shell command:
```bash
! echo $ANTHROPIC_AUTH_TOKEN
```
Which will result with the value you've placed inside `docker-compose.yaml` file (default value is `MY_PERSONAL_TOKEN`)