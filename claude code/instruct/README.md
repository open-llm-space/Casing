# Casing Claude Instruct Suit

This folder contains extensions for `claude code`. This suit is designed to not be overriden by the end-user (only extended).

| | | | |
| :--- |  :--: | :--- | :--- |
| Casing Main Instructions    | 📄 | `CLAUDE.md`    | This file will be primarly used as context |
| Casing Custom Hooks         | 📁 | `./hooks`      | Every hook should be place inside a folder having the hook name<br/>Use `hook.py` as your main file for hook calls |
| Casing Custom Skills        | 📁 | `./skills`      | Every skill should be place inside a folder having the skill name<br/>Skill file MUST be `SKILL.md` - follow oficial documentation for more details |

> [!TIP]
> This `Read Me` file (as well as other `Read Me` files placed in this folder) may be removed or changed to suit your project requirements