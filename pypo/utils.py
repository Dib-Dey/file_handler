"""
module having all utility functions

    >>> from pypo import utils

"""
import os
import shutil
import re
import subprocess

def find_pip_pkg_dir(pkg_name = ""):
    """
        find the pip package from the p[ip list 
    """
out = subprocess.Popen(['python','-m','pip','list'],
                          stdout=subprocess.PIPE,
                          stderr = subprocess.STDOUT,
                          universal_newlines=True
                       )
    stdout, stderr = out.communicate()
    item_list = stdout.split("\n")
    for pip_pkg in item_list:
        if pkg_name in pip_pkg:
            try:
                if (len(pip_pkg.split()) ==3):
                    print(pip_pkg.split()[2])
            except:
                print("site-package")
    subprocess.Popen.terminate(out)

def file_mover(source='', destination= ''):
    """
    copy all files inside all directories in source directory and paste in destination directory

        >>> from pypo import utils
        >>> utils.file_mover(r"C:\Users\ddey\Downloads\photos_and_videos")

    :param source: string of source path
    :param destination: string of destination path
    :return: path where files have been copied
    """
    if not destination:
        destination = source
    for dir in os.listdir(source):
        files_dir = os.path.join(source, dir)
        try:
            total_files_in_files_directory = os.listdir(files_dir)
        except:
            total_files_in_files_directory = []
        if total_files_in_files_directory:
            for files in total_files_in_files_directory:
                path_each_file = os.path.join(files_dir, files)
                shutil.copy(path_each_file, destination)
    return("Please check the files have ben copied in ({})".format(destination))

def path_converter(input_string=''):
    """
    converts windows path to linux and vice versa

    >>> utils.path_converter("/nfs/pdx/ddey/mbev/mve_softev")
    >>> # \\nfs\pdx\ddey\mbev\mve_softev

    :param input_string:
    :return: converted_path
    """
    if '\\' in input_string:
        input_string = input_string.replace('\\','/')
        print(input_string)
    elif '/' in input_string:
        input_string = input_string.replace('/','\\')
        print (input_string)
    else:
        print (input_string)

def file_play(input_file = "", option = ""):
    """
    Method which takes input file for string parsing and option to decide how to do it

    :param input_file: raw input file path
    :param option: option how to parse it
    :return: print statement or return file
    """
    import codecs
    with codecs.open(input_file, 'r', encoding='ascii', errors='ignore') as in_file:
        if option == "email":
            _list = ""
            for line in in_file:
                m = re.search('[^\s]+@intel.com', line)
                if m:
                    _list = _list + m.group(0) + ";"
            print(_list)
        else:
            all_words = []
            for line in in_file:
                print(line.strip())
                if line.strip():
                   # print(line.strip())
                    pass
                line_words = line.split()  # split()function removes the white space
                for words in line_words:
                    all_words.append(words)
                    # print(words)
    #return all_words
import requests
def grep_intel_id(idsid ,column_name):
    try:
        r = requests.get(
            'http://phonebook.fm.intel.com/cgi-bin/phonebook?e=%5E{}%24&d=IDSID&c={}&p=y&q=y'.format(idsid, column_name))
        if r.text.startswith(column_name):
            return( r.text.split('\n')[1].strip())
    except:
        pass
    return('n/a')

def convert_user_email(path= "", wpath=""):
    """
    convert authors-transform.txt with IDs to a format with full name, email for better git history log visualization 

    :param path: path of given file
    :param wpath: path of saved new file

    """
    _file = open(path, "r")
    if wpath is not "":
        _wfile = open(wpath, "w+")
    for item in _file:
        _id = item.split("=")[0].strip()
        _email = grep_intel_id(_id, "DomainAddress")
        _name = grep_intel_id(_id, "BookName")
        #print("{} = {} <{}>".format(_id, _name, _email))
        _wfile.writelines("{} = {} <{}>\n".format(_id, _name, _email))
    print("PYPO - conversion is complete. Check the new file {}".format(wpath))

if __name__ == '__main__':
    convert_user_email(r"C:\ddey_documents\Att58C9.tmp.txt",r"C:\ddey_documents\authors-transform.new.txt")


