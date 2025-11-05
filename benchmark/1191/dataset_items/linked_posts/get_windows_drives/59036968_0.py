>>> import os
>>> for drive_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if os.path.exists(f'{drive_letter}:'):
            print(f'{drive_letter}:')
        else:
            pass
