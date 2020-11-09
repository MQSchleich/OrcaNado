import pandas as pd

def get_compounds_by_element(elements: set or str, data, excluding=False):
    """
    Filters a dataframe with xyz according to elements
    :param elements: list or set of elements
    :param data: dataframe with smiles
    :param excluding: parameter to control if elements get excluded or included
    :return: filtered dataframe
    """
    indices=[]
    if type(elements) == str:
        elements=[elements]
    for i, row in data.iterrows():
        types=[]
        xyz=row.xyz_pbe_relaxed.split("\n")
        na=xyz[0]
        for i in range(int(na)):
            al=xyz[i + 2]
            atom, x, y, z=al.split()
            types.append(atom)
        types=set(types)
        intersect=elements.intersection(types)
        if excluding == True:
            if len(intersect) == 0:
                indices.append(i)
        elif excluding == False:
            if types.issubset(elements):
                indices.append(i)
    data.drop(indices)
    return data


if __name__ == "__main__":
    data=pd.read_json("../databases/df_62k.json", orient="split")
    all_elements={'H', 'Li', 'B', 'C', 'N', 'O', 'F', 'Si', 'P', 'S', 'Cl', 'As', 'Se', 'Br', 'Te', 'I'}
    wanted_elements={"H", "B", "C", "N", "O", "F", "S", "Cl", "Si"}
    difference=all_elements - wanted_elements
    new_data=get_compounds_by_element(difference, data, excluding=True)
    new_data.to_json("filtered_62k.json")
