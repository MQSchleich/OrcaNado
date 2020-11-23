from automation.XYZ_Reader import XYZ

class Input(XYZ):
    """
    Class to achieve the generation of Input files from a database.
    """
    from .calculate_orbwin import calculate_orbwin
    def __init__(self,
                 xyz_file_path,
                 atoms_bigger_c={"N", "O", "F", "S", "Cl", "Si", "P", "Al", "Na", "Mg"}
                 ):

        self.xyz_file_path = xyz_file_path
        self.read = open(self.xyz_file_path, "r").read()
        self.atoms = self.atom_list()
        self.atom_count = self.num_atoms()
        self.atoms_bigger_c = atoms_bigger_c
        self.atom_set = set(self.atoms)
        self.atoms_bigger=self.atom_set.intersection(self.atoms_bigger_c)


