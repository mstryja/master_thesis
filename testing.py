import pydicom
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def show_img_dir_one_by_one(data):
    """
    WARNING!!!
        This function from some reason does not work. I have to write a new version.
        As the instance of the class Test.

    Docstring...
    ConstPixelDims has the below structure:
    (int(dicom rows), int(dicom columns), int(value of all images in given directory))
    ConstPixelSpacing has the below structure:
    (float(dicom pixel spacing [0] value), float(dicom pixel spacing [1] value), int(value of all images in given directory))
    Now, because in given dataset all images has the pixelspacing in below formula:
    [0.48..., 0.48...]
    And the Rows and Columns are eqal 512 and 512, than after convert into matplotlib object to print, we achieve the size of 250 by 250.
    The output of below formula is the value of the x-size and y-size of dicom to matplotlib print object.
    512*0.488281 = 250 <=> ConstPixelDims[0]*ConstPixelSpacing[0]
    512*0.488281 = 250 <=> ConstPixelDims[1]*ConstPixelSpacing[1]
    Adding one in the formula for x and y, provide bigger value than 250. This is very important because of the numbers format.
    so the x has the given format:
    x = [0.0, 0.0 + ConstPixelSpacing[0], 0.0 + 2*ConstPixelSpacing[0] + ... + 0.0 + 513*ConstPixelSpacing[0]]
    y = [0.0, 0.0 + ConstPixelSpacing[1], 0.0 + 2*ConstPixelSpacing[1] + ... + 0.0 + 513*ConstPixelSpacing[1]]
    pcolormesh provide the fill "empty" spaces of x and y axis via the values of pixel from the ArrayDicom[:, :, index of temporary considered image].
    This is simillar to the process of coloring pages.
    Flipud function provides the possible best view of the dicom images.
    Due to the flipud function we can see the image from the same perspective which is in hospitals and clinical institutions
    """
    print(data)
    data = str(data)
    if len([data])==1:
        print("tu") # testing properties
        print(data)
        ds = pydicom.read_file(data)
        ConstPixelDims = (int(ds.Rows), int(ds.Columns), len(data))
        ConstPixelSpacing = (float(ds.PixelSpacing[0]), float(ds.PixelSpacing[1]), float(len(data)))
        ArrayDicom = np.zeros(ConstPixelDims, dtype=ds.pixel_array.dtype)
        ArrayDicom[:, :, data.index(data)] = ds.pixel_array
        x = np.arange(0.0, (ConstPixelDims[0] + 1) * ConstPixelSpacing[0], ConstPixelSpacing[0])
        y = np.arange(0.0, (ConstPixelDims[1] + 1) * ConstPixelSpacing[1], ConstPixelSpacing[1])
        plt.figure(f'Image: {ds.PatientID}', dpi=80)
        plt.axes().set_aspect('equal', 'datalim')
        plt.set_cmap(plt.gray())
        plt.pcolormesh(x, y, np.flipud(ArrayDicom[:, :, 0]))
        # numpy.flipud (https://numpy.org/doc/stable/reference/generated/numpy.flipud.html)
        plt.show()
    else:
        i = 0
        for filenameDCM in list(data):
            data = os.path.normpath(filenameDCM)
            print('nie bo tu') # testing properties
            print(filenameDCM)
            ds = pydicom.read_file(filenameDCM)
            ConstPixelDims = (int(ds.Rows), int(ds.Columns), len(data))
            ConstPixelSpacing = (float(ds.PixelSpacing[0]), float(ds.PixelSpacing[1]), float(len(data)))
            ArrayDicom = np.zeros(ConstPixelDims, dtype=ds.pixel_array.dtype)
            ArrayDicom[:, :, data.index(filenameDCM)] = ds.pixel_array
            x = np.arange(0.0, (ConstPixelDims[0] + 1) * ConstPixelSpacing[0], ConstPixelSpacing[0])
            y = np.arange(0.0, (ConstPixelDims[1] + 1) * ConstPixelSpacing[1], ConstPixelSpacing[1])
            plt.figure(f'Image: {ds.PatientID}', dpi=80)
            plt.axes().set_aspect('equal', 'datalim')
            plt.set_cmap(plt.gray())
            plt.pcolormesh(x, y, np.flipud(ArrayDicom[:, :, i]))
            plt.show()
            i += 1


def show_img_dir_one_by_one_2(data):

    ds = pydicom.read_file(data)
    ConstPixelDims = (int(ds.Rows), int(ds.Columns), len(data))
    ConstPixelSpacing = (float(ds.PixelSpacing[0]), float(ds.PixelSpacing[1]), float(len(data)))
    ArrayDicom = np.zeros(ConstPixelDims, dtype=ds.pixel_array.dtype)
    ArrayDicom[:, :, data.index(data)] = ds.pixel_array
    x = np.arange(0.0, (ConstPixelDims[0]+1)*ConstPixelSpacing[0], ConstPixelSpacing[0])
    y = np.arange(0.0, (ConstPixelDims[1]+1)*ConstPixelSpacing[1], ConstPixelSpacing[1])
    plt.figure(f'Image: {ds.PatientID}', dpi=80)
    plt.axes().set_aspect('equal', 'datalim')
    plt.set_cmap(plt.gray())
    plt.pcolormesh(x, y, np.flipud(ArrayDicom[:, :, 0]))
    plt.show()

def __to_numpy__(path) -> type(np.array):
    dcm = pydicom.read_file(path)
    ConstPixelDims = (int(dcm.Rows), int(dcm.Columns), 3)
    ConstPixelSpacing = (float(dcm.PixelSpacing[0]), float(dcm.PixelSpacing[1]))
    DataArray = np.zeros(ConstPixelDims, dtype=dcm.pixel_array.dtype)
    DataArray[:, :, 0] = dcm.pixel_array
    DataArray[:, :, 1] = dcm.pixel_array
    DataArray[:, :, 2] = dcm.pixel_array

    return DataArray


path = r'./data/Brain-Tumor-Progression/PGBM-007/12-29-1992-Mr Rcbv Sequence Fh-74352/11.000000-T1post-36303'

files = [os.path.join(path, f) for f in os.listdir(path)]
num_low = 4
num_up = 6
dcm = [pydicom.dcmread(f) for f in files[num_low:num_up]]

for i in range(0, num_up - num_low):
    print(f"Dicom number: {i}:\n{dcm[i]}")

show_img_dir_one_by_one_2(files[2])

rows, cols = dcm.Rows, dcm.Columns

print(rows, cols)

dcm_arr = np.array(dcm.PixelData)


# TODO:
#   1. Analyse the correlation between the numpy and png image. Find some information about methods to get more info
#   from computer tomography: contrasts, T1, T2 etc..
#   2. Write a method to read a dicom to numpy and locate it into dicom class, we need only a few infomation from
#   whole dicom file. We must develop what features are required.
#   3. Make a research about this data. What is located, how can be diagnosed, how people diagnose it right now,
#   what is the key feature of this kind of data. How to detect that something is wrong there.






