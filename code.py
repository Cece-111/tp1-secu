import os
from datetime import datetime

def update_date_file(file_path):
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file_path, 'w') as file:
        file.write(current_date)
    return current_date

if __name__ == "__main__":
    file_path = 'dateRefresh.txt'
    update_date_file(file_path)
    print(f"La date a été mise à jour dans {file_path}")
