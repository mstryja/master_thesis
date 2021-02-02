"""
Master Thesis 2021
Author: Mikolaj Stryja
Supervisor: Piotr Kijanka, PhD
Reviewer: Łukasz Pieczonka, PhD, Assistant Professor

Short description:
Right now, main file is using to the testing. In the future version in the
main file, the whole process will be concatenated.

"""

import numpy as np
import pydicom
import os
from os.path import join, isfile
import pandas as pd

"""
CODE NOTES:
In general at this model this is testing file. 
After prototyping here, the main file and whole program will be created. 
Right now a different approach to the problem are tested. 

Data interpretation organization:
dirs - list representing all directories under COVID_data directory
patients - list of paths to the patients directory under the dir. (dir is the one element of dirs)
treatments - list of paths to the treatments directory under given patient.
treatments_parameters - list of paths to the treatments parameters subdirectory. 
dicoms - list of dicoms files under the treatments_parameters directory
  
"""
# TODO:
#   1. List dicom files
#   2. Normalize the namespace. Consider how to keep data in the computer storage.
#       2.1. Must be as easy as possible
#       2.2. Must be well described
#       2.3. Must be easy to make operation by the ML mechanism


get = lambda string, l: [elem for elem in l if string in elem]


def feet_into_cm(value) -> float or None:
    """
    Convert given value in feet&inches format to the centimeters.
    result = feet*30,48 + inch*2.54
    :param value: value in the format: val1' val2"
    :return: value converted to the centimeters.
    """
    if type(value) == str:
        value = value.split("'")
        feet = float(value[0])
        inch = float(value[1].replace("\"", ""))
        value = round(feet * 30.48 + inch * 2.54, 2)
        return value
    else:
        return None


path = './data/COVID_data'

covid_files = [f for f in os.listdir(path) if isfile(join(path, f)) and join(path, f).endswith('.csv')]

csv_paths = [join(path, f) for f in covid_files]

imaging_studying = pd.read_csv(csv_paths[0], sep=';')
patient_data = pd.read_csv(csv_paths[1], sep=';', skiprows=1, index_col=False)

patient_data = patient_data.replace({'N': 0, 'Y': 1})
cols = patient_data.columns
print(cols)
col = get('HEIGHT', cols)
features = [cols[1], cols[2], cols[5], cols[8], cols[len(cols) - 5]]  # Features list
target = cols[len(cols) - 1]  # Target string
patient_data[col[0]] = patient_data[col[0]].apply(feet_into_cm)  # Apply the feet_into_cm function for specified column.

X = patient_data[features]
Y = patient_data[target]

print(X, Y)

print(patient_data[col[0]])
print(patient_data.head(10))

dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

# List all patients in the given dataset.
patients = []
for d in dirs:
    # Add to the patients list, lists of files under patient.
    patients.append([os.path.join(path, d, patient) for patient in os.listdir(os.path.join(path, d))])

# print(patients[0])
# print(patients)

# List all subfiles of the patient under given patient:
treatments = []
for patient in patients[0]:
    # Go through patients and list the all treatment under patient
    # print(patient)
    treatments.append([os.path.join(patient, treatment) for treatment in os.listdir(patient)])

# print(treatments)
# print(len(treatments))

# Treatment parameters directories listed
treatment_parameters = []
for patient_treatments in treatments:
    # Go through all treatments
    for treatment in patient_treatments:
        # Go through treatments under the patient
        treatment_parameters.append([os.path.join(treatment, params) for params in os.listdir(treatment)])

# print(treatment_parameters)
# print(len(treatment_parameters))

dicoms = []
for param in treatment_parameters:
    for prm in param:
        dicoms.append([os.path.join(prm, dcm) for dcm in os.listdir(prm)])

# print(dicoms)
full = 0
for dcm in dicoms:
    # print(len(dcm))
    full += len(dcm)

# print(f"Number: {full}")
