import argparse
from argparse import RawDescriptionHelpFormatter

# call with: python test.py -h

class SmartDescriptionFormatter(argparse.RawDescriptionHelpFormatter):
  #def _split_lines(self, text, width): # RawTextHelpFormatter, although function name might change depending on Python
  def _fill_text(self, text, width, indent): # RawDescriptionHelpFormatter, although function name might change depending on Python
    #print("splot",text)
    if text.startswith('R|'):
      paragraphs = text[2:].splitlines()
      rebroken = [argparse._textwrap.wrap(tpar, width) for tpar in paragraphs]
      #print(rebroken)
      rebrokenstr = []
      for tlinearr in rebroken:
        if (len(tlinearr) == 0):
          rebrokenstr.append("")
        else:
          for tlinepiece in tlinearr:
            rebrokenstr.append(tlinepiece)
      #print(rebrokenstr)
      return '\n'.join(rebrokenstr) #(argparse._textwrap.wrap(text[2:], width))
    # this is the RawTextHelpFormatter._split_lines
    #return argparse.HelpFormatter._split_lines(self, text, width)
    return argparse.RawDescriptionHelpFormatter._fill_text(self, text, width, indent)

parser = argparse.ArgumentParser(formatter_class=SmartDescriptionFormatter, description="""R|Blahbla bla blah blahh/blahbla (bla blah-blabla) a blahblah bl a blaha-blah .blah blah

Blah blah bla blahblah, bla blahblah blah blah bl blblah bl blahb; blah bl blah bl bl a blah, bla blahb bl:

  blah blahblah blah bl blah blahblah""")

options = parser.parse_args()
