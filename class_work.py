class BankA :
    def __init__(self, fname, Lname):
        self.fname = fname
        self.Lname = Lname

    def get_fname(self):
        return self.fname

    def get_Lname(self):
        return self.Lname

    def set_fname(self, fname):
        self.fname = fname  
    
    def set_Lname(self, Lname):
        self.Lname = Lname

