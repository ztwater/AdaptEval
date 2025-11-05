import os
sum(os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f))
