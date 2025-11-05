import click

with click.progressbar(length=total_size, label='Downloading files') as bar:
    for file in files:
        download(file)
        bar.update(file.size)
