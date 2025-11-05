    import pip

try:
    import imaplib
    import email
    import pandas as pd
    # for hiding password
    from pathlib import Path
    from dotenv import load_dotenv
    import os
    import requests
    # 
    from collections import defaultdict
    from itertools import permutations,combinations
except Exception as e:
    print(e)
    e = str(e).split(' ')[-1].replace("'","")
    pip.main(['install', e])
