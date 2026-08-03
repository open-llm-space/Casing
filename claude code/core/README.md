# Casing Core For Claude Code

This project is designed to create a unified solution across team members when using `claude code`

## Prerequisites
This project is running `claude code` inside a `docker` container using `ollama` models. Therefore, you should validate the following requirements or change this project configuration before building. In addition, if your installation requires a direct setup (no virtualization layer such as `docker`) - please scroll to the last section for raw installation.

| **Docker** | [official docker download page](https://docs.docker.com/engine/install/) |
| :--- |  :--- |

```bash
docker --version
```
You may use other compatiable tools for building this project out of the bos (such as [Pod Man](https://podman.io/)).

| **Ollama** | [official ollama download page](https://ollama.com/download) |
| :--- |  :--- |
```bash
ollama --version
```
`Ollama` is only on provider for running `claude code` and may be replaced. If using `ollama` is not desired, edit the `settings.json` and `settings.vaidations.json` files beforehand.

This suit also uses 2 models:
* `gemma4` - for basic reasoning and validation
* `llama3.2` - as the main agent used by `claude code` (supports Anthropic's `tool calling` natively)
These are for demonstration purposes only and can be modified the setiings files accordingly. In any other case, fetch these models using the following commands:
```bash
ollama pull gemma4
ollama pull llama3.2:3b
```

## Build
Build docker image using this command
```bash
cd "claude code/core"
docker compose build --progress=plain
```

Validate your build (you should see `casing/core-claude:v1.0` image in the list)
```bash
docker image ls
```

> [!NOTE]
> The build command should be used whenever a change to a file is made. *For example:* when adding / changing configuration field inside `settings.json` file - a new build should be invoked in order to include the recent changes.

## Run
Use the `docker compose` to start your `claude code` with `Casing`

```bash
cd "claude code/core"
docker compose up -d
```

> [!TIP]
> Verify that existing instances are not running **BEFORE** running the `compose up` command
>
> `docker container rm --force $(docker container ls --all --filter 'label=llm.space=casing-claude-code' --format '{{.ID}}')`

## Test & Verify
If all went well, your `claude code` terminal is accessible locally via your `web browser` at `http://localhost:8080/`

All the following tests should be executed from within the `claude code` terminal (via your `web browser`)
### Home Directories
```bash
! ls
```
Will list all files in your project's folder (should reflect the files placed inside the `sandbox` folder)

```bash
! ls ~
```
Will list all files and directories in your home folder - these files are readonly and should not be edited or removed (can be viewed)
### CLAUDE.md
```bash
! cat ~/instruct/CLAUDE.md 
```
This command will print the main instructions file used by `claude code`. Verify that your modifications (if performed) are reflected properly. The default instruct file comes with a pre-set of instructions, regarding an imaginary project that uses `Node.JS` + `Express.js` + `Angular` as its technological stack.
### Custom Hooks
A hook named `force-prompt-validation` is integrated in this suit as well. It is wired to the user's prompt hook (supply by `claude code`) and verify the user request before handling it to the working agent.

Enter the following prompt to test it
```
write a python code that counts from 1 to 10
```

### Custom Skills
```bash
/emojify hello
```
A custom skill added to this suit, in order to test custom skills implementation

## Raw Installation
No virtualization? No problem! `Casing` project can (also) run directly on your machine. Just follow the instructions below, and you will be up and running in the next 5-10 minutes.

### Main Components
* `python` - this is the chosen programming language to write hooks and extend this suit (can be also replaced to `Node.JS`, `Go` or whatever suits you)
* `ttyd` - a light service that serves your terminal as a web service (in our case, `claude code` will be server via your `web browser`)
* `claude code` - the actual tool providing the service (`Casing` is only a wrapper)

### Python
Download and install from the [official python download page](https://www.python.org/downloads/)

Verify by running the following commands:
```bash
python --version
pip --version
```

### TTYD
This utility can be download as a binary for `linux` / `os` / `windows` users from the [official releases page](https://github.com/tsl0922/ttyd/releases). No installation is required but you should add this binary file to your machine `PATH` settings or copy the file to your working directory.

Verify by running:
```bash
ttyd --version
```

### Claude Code
Download `claude code` locally using the [official claude code docs](https://code.claude.com/docs/en/setup#native-install-recommended)

Verify by running:
```bash
claude --version
```

### Working Directory
The working directory is the place where it's all happening! Ensure to create:
1. `.claude` folder with the `settings` files
2. `instruct` folder (should be copied as-is)
3. `sandbox` folder and place your code there
Finally, copy the `ttyd` binary file to your working directory as well as `run.sh` script (or `run.ps1` for windows users). Below is a tree hierarchy, describing the desired configuration.

```text
working-directory/
├── .claude/
│   ├── settings.json
│   └── settings.validations.json
├── instruct/
├── sandbox/
├── run.ps1
├── run.sh
└── ttyd
```

### Hooks Modifications
Naturally, the hooks in this project are wired to the `docker container` shipped as default. However, each hook is using a special variable named `workdir` that can be easily modified. *For example:* the hook `force-prompt-validation` has its own `workdir` variable at the top section of the hook code file (`hook.py`)
```python
workdir = '/home/claudeusr'
```
Change the value of this variable to reflect you working directory path. Please use absolute path (and not a relative one) to ensure the hook will work when triggered by claude.

### Run
That's it! Open `terminal` (such as `bash`, `powershell`, etc.), enter your working directory and run the script
```bash
./run.sh -p 8080
```
Or, for `windows` users:
```powershell
.\run.ps1 -port 8080
```