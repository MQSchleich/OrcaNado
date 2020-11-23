class XYZ():
    """
    Class to easy get useful information out of xyz files.
    Basically models xyz-files as an object
    """

    def __init__(self,
                 xyz_file_path,
                 atoms_bigger_c={"N", "O", "F", "S", "Cl", "Si", "P", "Al", "Na", "Mg"}
                 ):
        from .atom_list import atom_list
        from .num_atoms import num_atoms
        from .xyz_read import xyz_read

        self.xyz_file_path=xyz_file_path
        self.read=open(self.xyz_file_path, "r").read()
        self.atoms=atom_list(self)
        self.atom_count=num_atoms(self)
        self.atoms_bigger_c=atoms_bigger_c
        self.atom_set=set(self.atoms)

