# Lexify.md

Lexify.md is a Python tool for managing project vocabulary directly within your codebase. It helps developers maintain consistency and clarity by easily adding, removing, updating, and linking glossary terms to their project documentation.

## Features

- Add new terms with their definitions to the glossary.
- Remove existing terms from the glossary.
- Update definitions of existing terms in the glossary.
- Automatically create links to glossary terms within project documentation.

## Install and Usage

Install pipx if not available: https://pipx.pypa.io/stable/installation/

```sh
pipx install git+https://github.com/alex-but/lexify.md
```

```
Usage: lexify [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add
  init
  linkify
  remove
  update

```