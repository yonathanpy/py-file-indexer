import os


def scan_directory(path):

    file_list = []

    for root, dirs, files in os.walk(path):

        for name in files:

            full = os.path.join(root, name)

            file_list.append(full)

    return file_list
