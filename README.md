# Lexify.md

_Let's agree on terminology_

Lexify.md is a tool for managing project vocabulary directly within your codebase: GLOSSARY.md in the root of your project.

It helps developers maintain consistency and clarity by easily adding, removing, updating, and linking glossary terms to their project and make it part of the code.

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
  --version  Show the version and exit.
  --help  Show this message and exit.

Commands:
  add    <key>=<definition> : Adds the <key> to the dictionary
  init                      : Creates a new empty GLOSARRY.md file following lexify format
  remove <key>              : Removes the <key> from dictionary 
  update <key>=<definition> : Updates the definition of <key>
  read   <key>              : reads the description of <key>
````