import click, sys

with click.progressbar(range(100000), file=sys.stderr, show_pos=True, width=70, bar_template='(_(_)=%(bar)sD(_(_| %(info)s', fill_char='=', empty_char=' ') as bar:
    for i in bar:
        pass
