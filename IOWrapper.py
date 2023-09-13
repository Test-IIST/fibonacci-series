from io import StringIO 
class IOWrapper():
    def __init__(self):
        self.inBuffer=""
        self.outBuffer=""
    def input(self):
        return (StringIO(self.inBuffer)).read()
    def print(self,st):
         StringIO(self.outBuffer).write(st)
    def check(self,o):
        if (self.inBuffer==o.inBuffer) and (self.outBuffer==o.outBuffer):
            return True
        else :
            return False

    
