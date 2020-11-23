import mendeleev as pse

def calculate_orbwin(
        self
):
    """

    :param atoms:
    :param atoms_bigger_than_c:
    :return: [orbwin_min, orbwin_max]
    """
    atoms_bigger_than_c = self.atoms_bigger
    num_c_atoms = self.atoms.count("C")
    orbwin_min = 0
    for atom in atoms_bigger_than_c:
            orbwin_min += 1*self.atoms.count(atom)

    orbwin_max = orbwin_min + num_c_atoms - 1
    return [orbwin_min, orbwin_max]