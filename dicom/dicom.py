"""
Dicom module:

@Author: Mikołaj Stryja
@mail: mikolaj.stryja@artnovation.eu

Description:

"""
# Import
import pydicom
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image


class Dicom:
    def __init__(self, **kwargs):
        if not kwargs:
            self.detector = 0
            self.path = ""

        else:
            for key, value in kwargs.items():
                if key == "path":
                    # If keyword is path, create path argument.
                    self.path = value
                    self.dcm = pydicom.dcmread(self.path)

                elif key == "file":
                    # If keyword is file, already read dcm file is loaded to the class.
                    self.dcm = value
                    self.path = ""

    # Viewing methods
    def view(self):
        ds = self.dcm
        print(ds)
        img = self.to_png_simple()
        print(img.shape)
        # plt.figure(f'Image: {ds.PatientID}', dpi=80)
        # plt.axes().set_aspect('equal', 'datalim')
        # plt.imshow(img, cmap=plt.cm.bone)
        img = Image.fromarray(img)
        img.show()

    def to_png(self):
        ds = self.dcm
        const_pixel_dims = (int(ds.Rows), int(ds.Columns), 1)
        const_pixel_spacing = (float(ds.PixelSpacing[0]), float(ds.PixelSpacing[1]), 1)
        array_dcm = np.zeros(const_pixel_dims, dtype=ds.pixel_array.dtype)
        array_dcm[:, :, 0] = ds.pixel_array
        x = np.arange(0.0, (const_pixel_dims[0]) * const_pixel_spacing[0], const_pixel_spacing[0])
        y = np.arange(0.0, (const_pixel_dims[1]) * const_pixel_spacing[1], const_pixel_spacing[1])

        print(x.shape, y.shape, array_dcm.shape)

        return x, y, array_dcm

    def to_png_simple(self):
        ds = pydicom.read_file(self.path)  # read dicom image
        print(ds.pixel_array)
        return ds.pixel_array  # get image array


if __name__=="__main__":
    path = r'/Users/mikolajstryja/Documents/Studia/MasterThesis/master_thesis/data/COVID_data/COVID-19-AR/COVID-19-AR-16406488/01-08-2012-XR CHEST PA AND LATERAL-04866/2.000000-Lateral L-70577'
    file = [f for f in os.listdir(path)]
    dcm_path = os.path.join(path, file[0])

    dcm = Dicom(path=dcm_path)
    dcm.view()
