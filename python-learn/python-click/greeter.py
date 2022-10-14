
from email.policy import default
import click

@click.command()
#The arguments are mandatorys and the opcions well are optionals :D 
@click.argument("name")
@click.option("-l",
            "--lang", 
            help="Specify language English (en) or Spanish (es)",
            default="en",
            type=click.Choice(["es","en"]))
@click.option("--say-it",
            type=int,
            default=1,
            help="Number of times to say greeting")
def greet(name, lang, say_it):
    """Display a greeting to the user."""
    greetings = "Hi" if lang == "en" else "Hola"
    for nums_greet in range(say_it):
        click.echo(f"{greetings} {name}")

if __name__ == '__main__':
    greet()