"""
PyPo File Handler

Usage:
    start.py rename <expr> <files> [--nono | -n] [--verbose | -v] [--force | -f]
    start.py help
    start.py version

Options:
    -h --help       Show the screen
    -e --expr       Expression to match in format 's/old_name/new_name/'
    -n --nono       No action: Print name of the files to be re-named but don't rename
    -v --verbose    Verbose: Print names of files successfully renamed.
    -f --force      Force: Forcefully overwrite existing files.
    --version       Version: show version of the CLI package
"""
from docopt import docopt
from pypo.file_handler import handler

__version__ = "1.0.0"

def main(arguments):
    _nono = False
    _verbose = False
    _force = False
    try:
        if arguments['--nono'] or arguments['-n']:
            _nono = True
        if arguments['--verbose'] or arguments['-v']:
            _verbose = True
        if  arguments['--force'] or arguments['-f']:
            _force = True
    except:
        pass

    obj = handler()
    if arguments['version']:
        print(f'PyPo release version is : {__version__}')
    elif arguments['rename']:
        obj.rename(arguments['<expr>'],
                   arguments['<files>'],
                   _nono,
                   _verbose,
                   _force
                   )


if __name__ == '__main__':
    """
     running a package as a script with -m as above, Python executes the contents of the __main__.py file
    """
    arg = docopt(__doc__)
    main(arg)