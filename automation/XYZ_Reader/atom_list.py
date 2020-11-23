import re

def atom_list(self):
    atom_list=re.findall("(?:\n)(\S[A-Z]*)(?=" ")", self.read)
    return atom_list
