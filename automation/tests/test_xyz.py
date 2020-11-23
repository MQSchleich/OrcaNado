from automation import XYZ_Reader

def test_xyz():
    """
    Function to test xyz
    :return:
    """
    xyz = XYZ_Reader.XYZ("files/ABAFEQdb.xyz")
    atoms = ['O', 'S', 'O', 'C', 'H', 'C', 'C', 'C', 'H', 'C', 'C', 'H', 'C', 'H', 'C', 'H', 'H', 'H', 'C', 'C', 'C',
             'C', 'H', 'C', 'H', 'N', 'C', 'H', 'C', 'H', 'H', 'S', 'O', 'C', 'N', 'N', 'C', 'H', 'H', 'C',
             'H', 'H', 'H', 'C', 'H']
    num_atoms = 45
    true_read = "45\n\nO      39.55724515      33.75271314      38.40917207 \nS      40.85906611      34.05164612      " \
           "38.96498639 \nO      42.08066828      33.95284000      38.19595313 \nC      42.32571194      32.73322762  " \
           "    40.89834532 \nH      43.19968501      32.99032401      40.30295436 \nCl      45.20041227      " \
           "29.36338131      46.43043646 \nC      41.05184934      33.09086636      40.45377016 \nC      42.45668317 " \
           "     32.04677947      42.10437138 \nH      43.45084814      31.76806349      42.45397500 \nC      " \
           "41.33623713      31.70625411      42.87422993 \nC      40.06720668      32.07018496      42.39744704 \nH" \
           "      39.18097405      31.80058002      42.97364913 \nC      39.91665528      32.75758494      41.19816166" \
           " \nH      38.92751728      33.01994634      40.82523353 \nC      41.48361320      30.98558291     " \
           " 44.18381422 \nH      42.41118162      30.40352859      44.22479339 \nH      40.63985814     " \
           " 30.30766109      44.36544785 \nH      41.51361125      31.70368231      45.01623603 \nC      " \
           "43.58355603      33.58567170      46.05760995 \nC      44.50879591      33.09126273      45.12712202 \nC" \
           "      44.58735767      30.98663420      46.29469212 \nC      43.67416047      31.45779258      " \
           "47.23763178 \nH      43.35738436      30.81675118      48.05804802 \nC      43.18004488      32.75463873" \
           "      47.11100991 \nH      42.46723835      33.12401865      47.85020035 \nN      40.75043902" \
           "      35.65259391      39.44466891 \nC      41.91357542      36.39938024      39.92718967 \nH" \
           "      42.74053298      36.18343665      39.23786748 \nC      41.59554654      37.90036812" \
           "      39.88819883 \nH      41.31036592      38.18979620      38.87024230 \nH      42.47497764" \
           "      38.47941767      40.19408535 \nS      41.54380622      35.14894837      44.87226222 \nO" \
           "      41.49789017      35.80019430      42.30624954 \nC      42.31697189      35.46623386      " \
           "43.35107789 \nN      43.58095681      35.45930024      43.02499490 \nN      43.62739090      " \
           "35.79899291      41.66869043 \nC      42.40412200      35.98540807      41.28539389 \nH      " \
           "39.87281191      35.84000620      39.92875742 \nH      40.76971134      38.14771790      " \
           "40.56964680 \nC      43.04236454      34.98075809      45.94353203 \nH      43.78224526      " \
           "35.68390108      45.54521868 \nH      42.69364229      35.35046375      46.91564229 \nH      " \
           "44.82329787      33.72815772      44.30050633 \nC      45.01169104      31.79751710      45.24114695 \nH" \
           "      45.73147637      31.41638123      44.51869652 \n"
    true_atom_set = {'C', 'S', 'N', 'O', 'H'}
    test_xyz_atom_list(xyz, atoms, num_atoms)
    test_xyz_num_atoms(xyz, num_atoms)
    test_xyz_read(xyz, true_read)
    test_attributes(xyz, true_atom_set)


def test_xyz_atom_list(xyz:XYZ_Reader, atoms, num_atoms):
    """

    :param xyz: Instance of xyz
    :param atoms: true atom_list
    :return:
    """
    assert len(xyz.atoms) == num_atoms, "The length of the element list does not match the true number of atoms"
    assert xyz.atoms == atoms, "The element list does not match the true element list."

def test_xyz_num_atoms(xyz:XYZ_Reader, num_atoms):
    assert xyz.atom_count == num_atoms, "The counting method for atoms did not work"

def test_xyz_read(xyz:XYZ_Reader, true_read):
    """

    :param xyz: Instance of xyz
    :param true_read:
    :return:
    """
    assert xyz.read == true_read, "The file read is perfect"

def test_attributes(xyz:XYZ_Reader,
                    true_atom_set
                    ):
    """

    :param xyz: Instance of xyz-file
    :param true_atom_set:
    :return:
    """
    assert xyz.atom_set == true_atom_set, "The set of elements is not correct."


if __name__ == "__main__":
    test_xyz()