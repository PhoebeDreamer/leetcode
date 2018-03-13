# Design an in-memory file system to simulate the following functions:

# ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

# mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

# addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

# readContentFromFile: Given a file path, return its content in string format.

class FileSystem(object):

    def __init__(self):
        self.file_dic = {'/':[]}
        self.file_content = {}

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        if path not in self.file_dic:
            self.mkdir(path)
        return sorted(self.file_dic[path])
        

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        fp = ''
        prev = '/'
        path = list(filter(None, path.split('/')))
        for p in path:
            fp+='/'+p
            if p not in self.file_dic[prev]:
                self.file_dic[prev].append(p)
            if fp not in self.file_dic:
                self.file_dic.setdefault(fp,[])
            prev = fp
                

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        self.mkdir(filePath)
        path = list(filter(None, filePath.split('/')))
        if filePath not in self.file_content:
            self.file_content[filePath] = content
            self.file_dic[filePath].append(path[-1])
        else:
            self.file_content[filePath] += content
        

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return self.file_content[filePath]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)