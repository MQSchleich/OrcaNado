import re

def num_atoms(self):
    num_atoms=re.findall("([0-9]*)(?=\n\n)", self.xyz)
    return num_atoms[0]