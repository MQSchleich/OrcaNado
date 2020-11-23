class XYZ():
    """
    Class to easily get useful information out of xyz files.
    Basically models xyz-files as an object
    """

    from .atom_list import atom_list
    from .num_atoms import num_atoms
    from .xyz_read import xyz_read

    def __init__(self,
                 xyz_file_path,
                 atoms_bigger_c={"N", "O", "F", "S", "Cl", "Si", "P", "Al", "Na", "Mg"}
                 ):


        self.xyz_file_path=xyz_file_path
        self.read=open(self.xyz_file_path, "r").read()
        self.atoms=self.atom_list()
        self.atom_count=self.num_atoms()
        self.atoms_bigger_c=atoms_bigger_c
        self.atom_set=set(self.atoms)
        self.atoms_bigger = self.atom_set.intersection(self.atoms_bigger_c)

