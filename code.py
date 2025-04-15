import os
from datetime import datetime

file_path = 'dateRefresh.txt'

current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open(file_path, 'w') as file:
    file.write(current_date)

print(f"La date a été mise à jour dans {file_path}")
