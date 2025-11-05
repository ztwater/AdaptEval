import click

with click.progressbar(range(1000000)) as bar:
    for i in bar:
        pass 
