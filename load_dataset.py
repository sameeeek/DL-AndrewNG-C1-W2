import numpy as np
import h5py

def load_data() :
    train_data = h5py.File('train_catvnoncat.h5', "r")

    train_set_x_orig = np.array(train_data["train_set_x"][:])
    train_set_y_orig = np.array(train_data["train_set_y"][:])

    test_data = h5py.File('test_catvnoncat.h5', "r")

    test_set_x_orig = np.array(test_data["test_set_x"][:])
    test_set_y_orig = np.array(test_data["test_set_y"][:])

    classes = np.array(test_data["list_classes"][:])


    train_set_y_orig = train_set_y_orig.reshape(1, train_set_y_orig.shape[0])
    test_set_y_orig = test_set_y_orig.reshape(1, test_set_y_orig.shape[0])

    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes
