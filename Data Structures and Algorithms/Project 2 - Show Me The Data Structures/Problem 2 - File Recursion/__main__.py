import os

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    print(find_files('.c', path))

def find_files(suffix: str, path: str) -> list[str]:
    """Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.

    Parameters:
      suffix (str): suffix if the file name to be found
      path (str): path of the file system

    Returns:
       list[str]: a list of paths
    """
    paths = []
    elements = [os.path.join(path, element) for element in os.listdir(path)]
    for element in elements:
        if os.path.isdir(element):
            paths += find_files(suffix, element)
        elif os.path.isfile(element):
            if element.endswith(suffix):
                paths.append(element)
    return paths

if __name__ == "__main__":
    main()
