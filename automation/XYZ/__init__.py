class XYZ():
    """
    Class to easy get useful information out of xyz files.
    Basically models xyz-files as an object
    """

    def __init__(self, xyz_file_path, atoms_bigger_c={"N", "O", "F", "S", "Cl", "Si", "P", "Al", "Na", "Mg"}):
        self.xyz_file_path=xyz_file_path
        self.xyz=open(self.xyz_file_path, "r").read()
        self.atom_count=self.num_atoms()
        self.atoms=self.atom_list()
        self.atoms_bigger_c=atoms_bigger_c
        self.atom_set=set(atoms)