import re

def atom_list(self):
    atom_list=re.findall("(?:\n)(\S[A-Z]*)(?=" ")", self.read, re.IGNORECASE)
    return atom_list
