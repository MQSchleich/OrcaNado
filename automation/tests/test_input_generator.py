from automation.Input_Generator import Input

def test_input():
    """
    Test function for all parts of the Input class
    :return:
    """
    inp = Input("files/ABAFEQdb.xyz")
    orbwin_vals = [9, 26]
    test_calculate_orbwin(inp, orbwin_vals)

def test_calculate_orbwin(inp:Input, orbwin_vals:list):
    """

    :param inp:
    :param orbwin_vals: min max of orbwin values
    :return:
    """
    assert inp.calculate_orbwin() == orbwin_vals, ("The orbwin calculation does not match. Result from the method is ",
                                                   inp.calculate_orbwin(), "The true orbwin values are: ", orbwin_vals)

if __name__ == "__main__":
    test_input()