import fileinput

class ResponseManager:
    def __init__(self):
        self.filename=''

    def getBlockedUSerPage(self):
        f=open('/Users/vaishnaviuttarkar/masterclass/PythonProjects/PythonProxyServer.py/blockedip.html','r') 
        str=f.read()
        return(str);
        # fname = "blockedip.html"
        # html_file = open(fname, 'r', encoding='utf-8')
        # source_code = html_file.read() 
        # print(source_code)   
        # 
    def getBlockedKeywordPage(self):
        f=open('/Users/vaishnaviuttarkar/masterclass/PythonProjects/PythonProxyServer.py/blockedKeyword.html','r') 
        str=f.read()
        return(str);

    def getBlockedWebsitePage(self):
        f=open('/Users/vaishnaviuttarkar/masterclass/PythonProjects/PythonProxyServer.py/blockedwebsite.html','r') 
        str=f.read()
        return(str);

    