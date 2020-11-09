import re


class Output:
    """
    The class is a datastructure to model easy analysis of the ORCA output
    """
    def __init__(self, file_path):
        self.file_path=file_path
        self.read=open(self.file_path, "r").read()

    def get_orbital_energies(self):
        orbitals=re.findall(r"\n----------------\nORBITAL ENERGIES\n----------------\n\n(.*?)\n------------------\n",
                            self.read, re.DOTALL)
        return orbitals

    def count_mos(self):
        orbitals=re.findall(r"\n----------------\nORBITAL ENERGIES\n----------------\n\n(.*?)\n------------------\n",
                            self.read, re.DOTALL)
        num_orbitals=re.findall(r"\n", orbitals[0])
        return len(num_orbitals)

    def get_mo_distribution(self):
        table=re.findall(r"ORBITALS.*MULLIKEN", self.read, re.DOTALL)
        return table

    def get_num_atoms(self):
        """

        :return: Number of atoms of the molecule
        """
        xyz=re.findall(
            r"\n---------------------------------\nCARTESIAN COORDINATES \(ANGSTROEM\)\n------------------------------"
            r"---\n(.*?)\n\n-",
            self.read, re.DOTALL)
        num=re.findall(r"\n", xyz[0])
        return len(num) + 1

    def return_string(self):
        return self.read

    def read_string(self):
        file=open(self.file_path, "r")
        self.read=file.read()

    def get_run_time(self):
        print(self.file.readlines()[-1])

if __name__ == "__main__":
    file_1=Output("TestMOs/ABAFEQ/ABAFEQ_fast_RJ.out")
    num_atoms=file_1.get_num_atoms()
    orbitals=file_1.get_orbital_energies()
    num_orbitals=file_1.count_mos()
    print(num_orbitals)
    print(num_atoms)