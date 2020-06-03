import os


def main():
    """
    Entry to the package
    """
    dir_name = os.path.split(os.path.realpath(__file__))[0]
    command_path = os.path.join(dir_name, "file_handler.py")
    os.system(command_path)


if __name__ == '__main__':
    main()