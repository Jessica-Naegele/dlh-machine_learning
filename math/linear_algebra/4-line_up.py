"""This function adds two arrays elementwise when they have the same shape"""


def add_arrays(arr1, arr2):
    """Function to add two arrays element wise"""
    new_l = []
    size1 = []
    current_layer = arr1
    while isinstance(current_layer, list):
        size1.append(len(current_layer))
        current_layer = current_layer[0]
    size2 = []
    current_layer = arr1
    while isinstance(current_layer, list):
        size2.append(len(current_layer))
        current_layer = current_layer[0]
    if size1 == size2:
        for i in range(0, size1-1):
            new_l.append(arr1[i]+arr2[i])
        return new_l
    else:
        return None


