
import click

@click.command()
@click.option("--username", promt=True)
@click.option("--password", 
            promt=True,
            hide_input=True, 
            confirmation_prompt=True)
def auth(username, password):
    """Provides user authentication"""
    click.echo("Loggin in {username}")

# authenticate.py


import click


@click.command()
def auth():
    """Provides user authenitcation."""
    username = click.prompt('username')
    password = click.prompt('password', hide_input=True, confirmation_prompt=True)

    if click.confirm('Are you and admin?'):
        admin_id = click.prompt('Admin ID', type=int, prompt_suffix='>')
        click.echo(f"Logging in admin {username} (ID = {admin_id})")
    else:
        click.echo(f"Logging in {username}")





if __name__ == '__main__':
    auth()

