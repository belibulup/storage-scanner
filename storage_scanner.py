import shutil
import datetime
import os
from collections import defaultdict

def get_available_storage():
    disk_info = shutil.disk_usage("/")
    available_space = disk_info.free
    return available_space

if __name__ == '__main__':
    available_space = get_available_storage()
    available_space_gb = available_space / (1024**3)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry_1 = "{}: The available storage on your PC is {:.2f} GB\n".format(current_time, available_space_gb)


def get_folder_storage_usage(path='/'):
    folder_usage = defaultdict(int)

    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                folder_usage[root] += os.path.getsize(file_path)
            except OSError:
                pass

    sorted_folder_usage = sorted(folder_usage.items(), key=lambda x: x[1], reverse=True)
    return sorted_folder_usage[:20]

if __name__ == '__main__':
    top_20_folders = get_folder_storage_usage()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = "{}: Top 10 folders by storage usage: \n".format(current_time)
    for i, (folder, size) in enumerate(top_20_folders):
        log_entry += "{}. {} ({:.2f} GB)\n".format(i+1, folder, size / (1024**3))

    with open("storage_log.txt", "a") as file:
        file.write(log_entry_1 + "\n" + log_entry + "\n")

    print(log_entry)