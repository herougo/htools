import os
import csv
import pickle
import json

def lines_to_file(l, file_path):
    with open(file_path, 'w') as f:
        f.write("\n".join(l))

def file_to_lines(file_path):
    if len(file_path) == 0:
        return []
    with open(file_path) as f:
        lines = list(f.read().splitlines())
    return lines

def file_first_line(file_path):
    with open(file_path, 'r') as f:
        first_line = f.readline()
    return first_line

def file_first_n_lines(file_path, n):
    result = []
    with open(file_path, 'r') as f:
        result.append(f.readline())
    return result

def get_folder_paths(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, f))]

def get_file_paths_recursively(directory):
    result = []
    for paths, subdirs, files in os.walk(directory):
        for file in files:
            #print(name, paths)
            pure_path = os.path.join(paths, file)
            result.append(pure_path)
    return result
            

def get_file_paths(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))]


def string_to_file(text, file_name):
    with open(file_name, 'w') as f:
        target.write(text)

def file_to_string(filename):
    with open(filename) as f:
        return str(f.read())

def mat_to_csv(mat, file_name):
    with open(file_name, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(mat)

def csv_to_mat(file_name):
    result = None
    with open(file_name, 'rb') as f:
        reader = csv.reader(f)
        result = list(reader)
    return list(result)

def remove_file(path):
    os.remove(path)

def file_exists(path):
    os.path.isfile(path)

def folder_exists(path):
    return os.path.exists(path)

# also creates ancestor folders if they don't exist
def create_folder(path):
    os.makedirs(path)

def file_to_size(file_path):
    """
    :param file_path: str
    :return: human readable str of the file's size (e.g. "44 KB")
    """
    size = os.path.getsize(file_path)
    size_names = ['B', 'KB', 'MB', 'GB', 'TB']
    for i, name in enumerate(size_names):
        if size < 1000:
            return f'{int(size)} {size_names[i]}'
            break
        size /= 1000
    raise BaseException(f"File is too big: {size} PB")

def dir_to_size(dir_path):
    """
    :param dir_path: str of directory to recusively count the size
    :return: human readable str of the folder's size (e.g. "44 KB")
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    size_names = ['B', 'KB', 'MB', 'GB', 'TB']
    for i, name in enumerate(size_names):
        if total_size < 1000:
            return f'{int(total_size)} {size_names[i]}'
            break
        total_size /= 1000
    raise BaseException(f"Directory is too big: {total_size} PB")

def pickle_load(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

def pickle_dump(obj, file_path):
    assert isinstance(file_path, str)
    with open(file_path, 'wb') as f:
        return pickle.dump(obj, f)

def file_path_to_file_name(path):
    return os.path.basename(path)

def parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))

