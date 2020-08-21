"""
PyPo File Handler

Usage:
    start.py ls [-l] [-a] [--la] [--dir <dir_name>]
    start.py rename <expr> <files> [--nono] [-n] [--verbose] [-v] [--force] [-f] [--dir <dir_name>]

Options:
    -l              List of file details
    -a              List of file and directory but no details
    --la            List of file and directory with details
    -h --help       Show the screen
    -e --expr       Expression to match in format 's/old_name/new_name/'
    -n  --nono      No action: Print name of the files to be re-named but don't rename
    -v  --verbose   Verbose: Print names of files successfully renamed.
    -f  --force     Force: Forcefully overwrite existing files.
    --version       Version: show version of the CLI package
    --dir           Input directory
"""
from docopt import docopt
from pypo.file_handler import handler

__version__ = "1.0.0"

def main(arg):
    obj = handler(arg['--dir'], arg['<dir_name>'])
    if arg['version']:
        print(f'PyPo release version is : {__version__}')
    elif arg['ls']:
        obj.list_file_detail(arg["-l"], arg["-a"], arg["--la"])
    elif arg['rename']:
        obj.rename(arg['<expr>'],
                   arg['<files>'],
                   arg['--nono'] or arg['-n'],
                   arg['--verbose'] or arg['-v'],
                   arg['--force'] or arg['-f']
                   )


if __name__ == '__main__':
    """
     running a package as a script with -m as above, Python executes the contents of the __main__.py file
    """
    arg = docopt(__doc__)
    #print(arg)
    main(arg)