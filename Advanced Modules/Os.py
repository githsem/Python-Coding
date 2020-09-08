import os
from datetime import datetime

print(os.getcwd())
print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime))
