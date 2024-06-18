# backend/cli/main.py

import click
from .commands import create_user, get_user, create_anime, get_anime

@click.group()
def cli():
    pass

cli.add_command(create_user)
cli.add_command(get_user)
cli.add_command(create_anime)
cli.add_command(get_anime)

if __name__ == "__main__":
    cli()
