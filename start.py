"""
PyPo File Handler

Usage:
    start.py rename <expr> <files> [--nono | -n] [--verbose | -v] [--force | -f]
    start.py ls [-la]
    start.py help
    start.py version

Options:
    -la             List details
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

def main(arg):
    _nono = False
    _verbose = False
    _force = False
    try:
        if arg['--nono'] or arg['-n']:
            _nono = True
        if arg['--verbose'] or arg['-v']:
            _verbose = True
        if  arg['--force'] or arg['-f']:
            _force = True
    except:
        pass

    obj = handler()
    if arg['version']:
        print(f'PyPo release version is : {__version__}')
    elif arg['ls']:
        obj.list_file_detail(arg["-la"])
    elif arg['rename']:
        obj.rename(arg['<expr>'],
                   arg['<files>'],
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