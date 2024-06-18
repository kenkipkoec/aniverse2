# backend/cli/commands.py

import click
import requests

API_URL = "https://jsonplaceholder.typicode.com"

@click.command()
@click.option('--email', prompt='Email', help='The email of the user.')
@click.option('--password', prompt='Password', hide_input=True, confirmation_prompt=True, help='The password of the user.')
def create_user(email, password):
    response = requests.post(f"{API_URL}/users/", json={"email": email, "password": password})
    if response.status_code == 201:
        click.echo("User created successfully!")
    else:
        click.echo("Error creating user.")

@click.command()
@click.argument('user_id')
def get_user(user_id):
    response = requests.get(f"{API_URL}/users/{user_id}")
    if response.status_code == 200:
        click.echo(response.json())
    else:
        click.echo("User not found.")

@click.command()
@click.option('--title', prompt='Title', help='The title of the anime.')
@click.option('--description', prompt='Description', help='The description of the anime.')
@click.option('--rating', prompt='Rating', type=int, help='The rating of the anime.')
def create_anime(title, description, rating):
    response = requests.post(f"{API_URL}/posts/", json={"title": title, "body": description, "userId": rating})
    if response.status_code == 201:
        click.echo("Anime created successfully!")
    else:
        click.echo("Error creating anime.")

@click.command()
@click.argument('anime_id')
def get_anime(anime_id):
    response = requests.get(f"{API_URL}/posts/{anime_id}")
    if response.status_code == 200:
        click.echo(response.json())
    else:
        click.echo("Anime not found.")
