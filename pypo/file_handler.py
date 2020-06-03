import os


class handler(object):
    def __init__(self, input_file = None, output_dir = None, output_file= None):
        self.input_file = input_file
        self.dest_file = None

    @property
    def input_dir(self):
        """creates input_dir variable outside attribute constructor"""
        return os.path.split(self.input_file)[0]

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

    def list_only_files(self):
        """
        function to list all files inside a directory
        :return: list of files only
        """
        _list = os.listdir(self.input_dir)
        for _item in _list:
            _file = os.path.join(self.input_dir,_item)
            if os.path.isfile(_file):
                print(_item)

if __name__ == '__main__':
    obj = handler(r"C:\ddey_documents\ELT-OR\example.txt")
    #x = os.path.split(r"C:\ddey_documents\GitHub_Python\pypo\__init__.py")[0]
    obj.list_only_dir()
   # obj.list_only_files()