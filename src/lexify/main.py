import click
import re

def add_word_to_glossary(term, definition):
    # Read the existing glossary
    with open("GLOSSARY.md", "r") as file:
        glossary = file.readlines()

    # Find the position to insert the new term alphabetically
    index = 0
    for i, line in enumerate(glossary):
        if line.startswith("## Definitions"):
            index = i + 1
            break
        elif line > f"<a name='{term.lower()}'>\n":
            index = i
            break

    # Insert the new term and definition
    glossary.insert(index, f"<a name='{term.lower()}'></a>_{term}_: {definition}\n")

    # Rewrite the glossary file
    with open("GLOSSARY.md", "w") as file:
        file.writelines(glossary)

def remove_word_from_glossary(term):
    # Read the existing glossary
    with open("GLOSSARY.md", "r") as file:
        glossary = file.readlines()

    # Find and remove the term and its definition
    for i, line in enumerate(glossary):
        if f"<a name='{term.lower()}'>" in line:
            del glossary[i]
            break

    # Rewrite the glossary file
    with open("GLOSSARY.md", "w") as file:
        file.writelines(glossary)

def update_word_in_glossary(term, definition):
    remove_word_from_glossary(term)
    add_word_to_glossary(term, definition)

def create_links(description):
    glossary_words = re.findall(r'\b\w+\b', description)
    with open("GLOSSARY.md", "r") as file:
        glossary = file.read()

    for word in glossary_words:
        if f"<a name='{word.lower()}'>" in glossary:
            description = description.replace(word, f"[{word}](#{word.lower()})")

    return description

@click.group()
def cli():
    pass

@cli.command()
def init():
    with open("GLOSSARY.md", "w") as file:
        file.write("# Glossary\n\n## Index\n\n## Definitions\n")

@cli.command()
@click.argument('term_definition', nargs=1)
def add(term_definition):
    try:
        term, definition = term_definition.split('=')
        add_word_to_glossary(term, definition)
        click.echo(f"Added '{term}' to the glossary with definition: '{definition}'.")
    except ValueError:
        click.echo("Error: Please provide the term and definition in the format 'term=definition'.")

@cli.command()
@click.argument('term', nargs=1)
def remove(term):
    remove_word_from_glossary(term)
    click.echo(f"Removed '{term}' from the glossary.")

@cli.command()
@click.argument('term_definition', nargs=1)
def update(term_definition):
    try:
        term, definition = term_definition.split('=')
        update_word_in_glossary(term, definition)
        click.echo(f"Updated '{term}' in the glossary with definition: '{definition}'.")
    except ValueError:
        click.echo("Error: Please provide the term and definition in the format 'term=definition'.")

@cli.command()
@click.argument('description', nargs=1)
def linkify(description):
    click.echo(create_links(description))

