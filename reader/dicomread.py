"""
GENERAL INFORMATION:

AUTHORS:
    Mikołaj Stryja: mikolaj.stryja@artnovation.eu
    Piotr Kijanka, PhD:

"""
# TODO:
#   1. Analyse the correlation between the numpy and png image. Find some information about methods to get more info
#   from computer tomography: contrasts, T1, T2 etc..
#   2. Write a method to read a dicom to numpy and locate it into dicom class, we need only a few infomation from
#   whole dicom file. We must develop what features are required.
#   3. Make a research about this data. What is located, how can be diagnosed, how people diagnose it right now,
#   what is the key feature of this kind of data. How to detect that something is wrong there.

import numpy as np
import pydicom as dcm
import os

class Test:
    """

    """
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        self.name = args[0]
        self.images = [f for f in os.listdir(self.name) if f.endswith('.dcm')]

class Sequence:
    """

    """
    def __init__(self, path, *args):

        pass

class Patient:
    """
    Patient class.
    Representing one Patient from Dataset. Does contain all information and also keeps every
    images about patient.
    """
    def __init__(self, path, *args):
        self.sequences = os.listdir(path)



    pass



def read_dcm(path) -> type(np.array):
    ds = dcm.dcmread(path)
    return np.array(ds.PixelData, type=float)


## Testing:
if __name__=="__main__":
    data = '../data'


    pass
