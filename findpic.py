import os

repo_path = "/Users/zipeng/Projects/apollo/"
valid_extensions = ['.jpeg','.png', '.jpg', '.bmp', '.gif']


def get_extension(path):
    """ Return the extension of the file targeted by path. """
    end = path.rfind('.')
    end = end if end != -1 else len(path)
    return path[end:]


def get_files(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for file in files:
            f_path = os.path.join(root, file)
            if get_extension(f_path) in valid_extensions:
                file_paths.append(f_path)
                print(f_path)
    print("total number of files: %s" % len(file_paths))
    return file_paths


if __name__ == "__main__":
    get_files(directory=repo_path)