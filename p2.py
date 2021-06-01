import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files = []
    for item in os.listdir(path):
        item_path = path + "/" + item
        if os.path.isfile(item_path):
            if item.endswith(suffix):
                files.append(item_path)
        elif os.path.isdir(item_path):
            for file in find_files(suffix, item_path):
                files.append(file)

    return files

if __name__ == '__main__':
    print(find_files('.c', '.'))
