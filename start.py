"""
PyPo File Handler

Usage:
    start.py help
    start.py version

Options:
    --version
"""
from docopt import docopt
from pypo.file_handler import handler

__version__ = "1.0.0"

def main(arguments):
    if arguments['version']:
        print(f'PyPo release version is : {__version__}')

if __name__ == '__main__':
    """
     running a package as a script with -m as above, Python executes the contents of the __main__.py file
    """
    arg = docopt(__doc__)
    main(arg)