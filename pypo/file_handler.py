import os
from os import system

class handler(object):
    @property
    def input_dir(self):
        """creates input_dir variable outside attribute constructor"""
        return os.getcwd()

    def rename(self, do_expr = False, files = False, no_action = False, do_verbose = False, do_force = False):
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
            self.list_only_files(files)

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

    def list_file_detail(self, file_detail = False):
        if file_detail:
            os.system('ls -la')
        else:
            os.system('ls')

    def list_only_files(self, type_file):
        """
        function to list all files inside a directory
        :return: list of files only
        """
        if type_file:
            _file_exten = type_file.split(".")[-1]
        else:
            _file_exten = ""
        _list = os.listdir(self.input_dir)
        for _item in _list:
            _file = os.path.join(self.input_dir,_item)
            if os.path.isfile(_file) and _file.endswith(_file_exten):
                print(_item)

if __name__ == '__main__':
    obj = handler()
    #x = os.path.split(r"C:\ddey_documents\GitHub_Python\pypo\__init__.py")[0]
   # obj.rename("","*.py",True)
    obj.rename(" "," ",True)
   # obj.list_only_files()