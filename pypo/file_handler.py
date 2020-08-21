import os
from os import system
from pypo import utils
import re

class handler(object):
    def __init__(self, dir_option = False, dir_input = None):
        self.dir_option = dir_option
        self.dir_input = dir_input

    @property
    def input_dir(self):
        """creates input_dir variable outside attribute constructor"""
        if self.dir_option:
            return self.dir_input
        else:
            return os.getcwd()

    def rename(self, do_expr = False, file_extn = False, no_action = False, do_verbose = False, do_force = False):
        """
        https://www.tecmint.com/rename-multiple-files-in-linux/
        :param do_expr:Expression to match in format `s/old_name/new_name/`
        :param files: to-be renamed
        :param no_action:Print name of the files to be re-named but don't rename
        :param do_verbose:Print names of files successfully renamed.
        :param do_force:Forcefully overwrite existing files.
        :return:
        """
        if no_action:
            self.list_only_files(file_extn)
            return
        #os.rename(r'file path\OLD file name.file type',r'file path\NEW file name.file type')
        if len(do_expr.split('/')) != 3:
            print(f"Your expression ({do_expr}) isn't in correct format (s/old_name/new_name)")
        else:
            if file_extn:
                file_extn = file_extn.split(".")[-1]
            list_files_to_replace = utils.check_dir_return_list_file_match_extn(self.input_dir,file_extn)
            old_str, new_str = do_expr.split('/')[1], do_expr.split('/')[2]
            for _item in list_files_to_replace:
                if old_str in _item:
                    new_file_name = re.sub(old_str,new_str,_item)
                    if do_verbose or no_action:
                        print(f"Info - old_file_name = {_item} replaced with new_file_name={new_file_name}")
                    if not no_action:
                        os.rename(os.path.join(self.input_dir,_item),os.path.join(self.input_dir,new_file_name))

    def list_only_dir(self):
        """
        function to list all files inside a directory
        :return: list of files only
        """
        _list = os.listdir(self.input_dir)
        for _item in _list:
            _dir = os.path.join(self.input_dir, _item)
            if os.path.isdir(_dir):
                print(_item)

    def list_file_detail(self, _l = False, _a= False, _la= False):
        if _l:
            os.system('ls -l'+ " \"" + self.input_dir +"\"")
        elif _a:
            os.system('ls -a'+ " \"" + self.input_dir +"\"")
        elif _la:
            os.system('ls -la' + " \"" + self.input_dir +"\"")
        else:
            os.system('ls' + " \"" + self.input_dir +"\"")

    def list_only_files(self, type_file):
        """
        function to list all files inside a directory
        :return: list of files only
        """
        if type_file:
            type_file = type_file.split(".")[-1]

        return_list = utils.check_dir_return_list_file_match_extn(self.input_dir, type_file)
        for _item in return_list:
            print(_item)

if __name__ == '__main__':
    obj = handler()
    #x = os.path.split(r"C:\ddey_documents\GitHub_Python\pypo\__init__.py")[0]
   # obj.rename("","*.py",True)
    obj.rename(" "," ",True)
   # obj.list_only_files()