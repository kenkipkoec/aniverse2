# backend/cli/commands.py

import click
from ..app import crud, schemas

@click.command()
@click.option('--email', prompt='Email', help='The email of the user.')
@click.option('--password', prompt='Password', hide_input=True, confirmation_prompt=True, help='The password of the user.')
def create_user(email, password):
    user = schemas.UserCreate(email=email, password=password)
    created_user = crud.create_user(None, user)  # Pass None for db session in API case
    if created_user:
        click.echo(f"User created successfully! User ID: {created_user['id']}")
    else:
        click.echo("Error creating user.")

@click.command()
@click.argument('user_id')
def get_user(user_id):
    user = crud.get_user(None, user_id)  # Pass None for db session in API case
    if user:
        click.echo(f"User found: {user}")
    else:
        click.echo("User not found.")

@click.command()
@click.option('--title', prompt='Title', help='The title of the anime.')
@click.option('--description', prompt='Description', help='The description of the anime.')
@click.option('--rating', prompt='Rating', type=int, help='The rating of the anime.')
def create_anime(title, description, rating):
    anime = schemas.AnimeCreate(title=title, description=description, rating=rating)
    created_anime = crud.create_anime(None, anime)  # Pass None for db session in API case
    if created_anime:
        click.echo("Anime created successfully!")
    else:
        click.echo("Error creating anime.")

@click.command()
@click.argument('anime_id')
def get_anime(anime_id):
    anime = crud.get_anime(None, anime_id)  # Pass None for db session in API case
    if anime:
        click.echo(f"Anime found: {anime}")
    else:
        click.echo("Anime not found.")
