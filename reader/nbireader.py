import nibabel
import numpy as np
from os import listdir
import os
from os.path import join
import cv2
import PIL
from PIL import Image
import time
from scipy import spatial
import matplotlib.pyplot as plt
import imageio


class NiiImage:
    """
    NiiImage class
    Class representing the .nii image.

    """

    def __init__(self, path):
        self.nii_file = nibabel.load(path)
        self.data_array = self.get_data()

    def get_data(self):
        return self.nii_file.get_fdata()


def read_nii(path):
    return nibabel.load(path)


def filter_img(img, t_down=-1000, t_up=1000) -> type(np.array):
    """

    :param img:
    :param t_down:
    :param t_up:
    :return:
    """
    img[img < t_down] = t_down
    img[img > t_up] = t_up
    return img


def increase_contrast(img, down_threshold=40, up_threshold=200) -> type(np.array):
    """
    Unused - to delete in the future version
    :param img:
    :param down_threshold:
    :param up_threshold:
    :return:
    """
    img[img > up_threshold] = 255
    img[img < down_threshold] = 0
    return img


def print_images(file, number=0, all_imgs=False):
    if not all_imgs:
        data = file.get_fdata()
        img = Image.fromarray(data[:, :, number])
        img.show()

    else:
        data = file.get_fdata()
        images = data.shape[2]
        for i in range(images):
            img = Image.fromarray(data[:, :, i])
            img.show()
            time.sleep(0.5)


def get_patient_id(f_name) -> str:
    """
    TODO
    :param f_name:
    :return:
    """
    idx_start = f_name.index('A')
    idx_stop = f_name.index('.')
    return f_name[idx_start:idx_stop]


def create_png_dataset(nii_path, png_path):
    try:
        if os.path.isdir(png_path):
            print(f"{png_path} directory already exist.")
            pass
        else:
            os.mkdir(png_path)
    except OSError:
        print(f"Creation of directory {png_path} is failed!")

    # TODO: Add here the exception handling in order to provide good functionality - catch if given path does not exist.
    files = [f for f in os.listdir(nii_path) if f.endswith('.nii')]
    for file in files:
        patient_path = os.path.join(png_path, get_patient_id(os.path.basename(file)))
        os.mkdir(patient_path)
        img = nibabel.load(os.path.join(nii_path, file))
        data = filter_img(img.get_fdata())
        for i in range(data.shape[2]):
            data_path = os.path.join(patient_path, get_patient_id(file) + str('-') + str(i) + '.png')
            imageio.imsave(data_path, data[:, :, i])


def create_3d_object(f, save=False):
    """
    Generating the 3D model from given nii file.
    :param f: path to the file
    :param save: optional param - if True, model is saved
    :return: print 3D model and save if chose.
    """
    # TODO:
    #   1. Implement it ;)


if __name__ == "__main__":
    # Paths
    test_path = r'../testing_data'
    png_path = r'../testing_data/pngs'
    png_path_filtred = r'../testing_data/fpngs'
    tmp_path = r'../temp'

    # Files listing
    files = [f for f in os.listdir(test_path) if f.endswith('.nii')]

    print("IDS\n")
    print(get_patient_id(files[0]))
    create_png_dataset(test_path, png_path_filtred)
    """
    imgs = []
    for file in files:
        imgs.append(nibabel.load(join(test_path, file)))

    print(imgs[0])
    data = imgs[0].get_fdata()
    nifti = imgs[0]
    print(nifti.header['bitpix'])
    # create_png_dataset(test_path, png_path)
    count = 20
    img = Image.fromarray(data[:, :, count])
    img.show()
    img_name_f = rf'{tmp_path}/{get_patient_id(files[0])}-{count}-filtred.png'
    img_name_uf = rf'{tmp_path}/{get_patient_id(files[0])}-{count}-unfiltred.png'
    imageio.imwrite(img_name_uf, data[:, :, count])
    imageio.imwrite(img_name_f, filter_img(data[:, :, count]))
    # img.show()
    # img.save('/Users/mikolajstryja/Documents/Studia/MasterThesis/master_thesis/temp/img1.png')
    """