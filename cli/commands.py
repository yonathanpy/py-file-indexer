import click
from indexer.engine import IndexEngine

engine = IndexEngine()


@click.group()
def cli():
    pass


@cli.command()
@click.argument("path")
def index(path):

    engine.index_directory(path)

    print("Indexing completed")


@cli.command()
@click.argument("term")
def search(term):

    results = engine.search(term)

    for r in results:

        print(r[0])
