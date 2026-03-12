import os


def file_size(path):

    return os.path.getsize(path)


def file_exists(path):

    return os.path.exists(path)
