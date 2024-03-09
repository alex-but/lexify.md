import click
from lexify import term_definition
from lexify.glossary_parser import generate_glossary, parse_glossary

from lexify.term_definition import TermDefinition, validate_term_definition
from lexify import crud


def add_word_to_glossary(term, definition):
    term_definition = TermDefinition(term=term, definition=definition)
    validate_term_definition(term_definition=term_definition)

    # Read the existing glossary
    with open("GLOSSARY.md", "r") as file:
        glossary_str = file.read()
        glossary: list[TermDefinition] = parse_glossary(glossary_str)

    # Rewrite the glossary file
    with open("GLOSSARY.md", "w") as file:
        new_glossary = crud.create(term_definition=term_definition, lexicon=glossary)
        file.write(generate_glossary(new_glossary))


def remove_word_from_glossary(term):
    # Read the existing glossary
    with open("GLOSSARY.md", "r") as file:
        glossary_str = file.read()
        glossary: list[TermDefinition] = parse_glossary(glossary_str)

    # Rewrite the glossary file
    with open("GLOSSARY.md", "w") as file:
        new_glossary = crud.delete(term=term, lexicon=glossary)
        file.write(generate_glossary(new_glossary))


def read_word_from_glossary(term):
    # Read the existing glossary
    with open("GLOSSARY.md", "r") as file:
        glossary_str = file.read()
        glossary: list[TermDefinition] = parse_glossary(glossary_str)

    definition = crud.read(term=term, lexicon=glossary)
    return definition


def update_word_in_glossary(term, definition):
    term_definition = TermDefinition(term=term, definition=definition)
    validate_term_definition(term_definition=term_definition)
    remove_word_from_glossary(term)
    add_word_to_glossary(term, definition)


@click.group()
def cli():
    pass


@cli.command()
def init():
    """: Creates a new empty GLOSARRY.md"""
    with open("GLOSSARY.md", "w") as file:
        file.write("# Glossary\n\n## Index\n\n## Definitions\n")


@cli.command()
@click.argument("term_definition", nargs=1)
def add(term_definition):
    """<key>=<definition> : Adds the <key> to the dictionary"""
    term, definition = term_definition.split("=")
    add_word_to_glossary(term, definition)
    click.echo(f"Added '{term}' to the glossary with definition: '{definition}'.")


@cli.command()
@click.argument("term", nargs=1)
def remove(term):
    """<key> : Removes the <key> from dictionary"""
    remove_word_from_glossary(term)
    click.echo(f"Removed '{term}' from the glossary.")


@cli.command()
@click.argument("term", nargs=1)
def read(term):
    """<key>: reads the description of <key>"""
    definition = read_word_from_glossary(term=term)
    click.echo(definition)


@cli.command()
@click.argument("term_definition", nargs=1)
def update(term_definition):
    """<key>=<definition> : Updates the definition of <key>"""
    term, definition = term_definition.split("=")
    update_word_in_glossary(term, definition)
    click.echo(f"Updated '{term}' in the glossary with definition: '{definition}'.")
