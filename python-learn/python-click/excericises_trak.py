"""import click

@click.command()
#The arguments are mandatorys and the opcions well are optionals :D 
@click.argument("name")
@click.option("--lang", 
            help="Specify language English (en) or Spanish (es)",
            default="en")
def greet(name, lang):
    """Display a greeting to the user."""
    if lang =="es":
        greetings = "Hola"
    elif lang == "en":
        greetings = "Hi"
    else:
        raise click.BadArgumentUsage("lang","Unsupported .")
    #Why does this example use echo() instead of the regular print() function? The answer to this question is that Click attempts to support different environments consistently and to be very robust even when the environment is misconfigured. Click wants to be functional at least on a basic level even if everything is completely broken.
    click.echo(f"{greetings} {name}")

if __name__ == '__main__':
    greet()
"""
    

###################################################################################
"""

import click

@click.command()
#The arguments are mandatorys and the opcions well are optionals :D 
@click.argument("name")
@click.option("-l",
            "--lang", 
            help="Specify language English (en) or Spanish (es)",
            default="en")
def greet(name, lang):
    """Display a greeting to the user."""
    greetings = "Hi" if lang == "en" else "Hola"
    #Why does this example use echo() instead of the regular print() function? The answer to this question is that Click attempts to support different environments consistently and to be very robust even when the environment is misconfigured. Click wants to be functional at least on a basic level even if everything is completely broken.
    click.echo(f"{greetings} {name}")
    

if __name__ == '__main__':
    greet()
"""



"""
import click

@click.command()
@click.argument("xs", type=int, nargs=-1)# -1 means unlimited number of arguments is accepted.
@click.option("-v", "--verbose", help="Show additional output.", is_flag=True)
def add(xs, verbose):
    """Add numbers"""
    if verbose:
        click.echo(f"{' + '.join(str(x) for x in xs)} = {sum(xs)}") ##Cuando usar "" y ''????
    else:
        click.echo(sum(xs))

@click.command()
@click.argument("xs", type=int, nargs=-1) # -1 means unlimited number of arguments is accepted.
@click.option("-v", "--verbose", help="Show additional output.", is_flag=True)
def subtract(xs, verbose):
    """subtract numbers"""
    result = xs[0]
    for x in xs[1:]:
        result -= x

    if verbose:
        click.echo(f"{' - ' .join(str(x) for x in xs)} = {result}")
    else:
        click.echo(result)
"""