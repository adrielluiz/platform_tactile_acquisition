import pandas as pd
import os

class Excel():
    def __init__(self):
        self.colX = []
        self.colZ = []
        self.colFSR = []
        self.filename = "./plataform_data.xlsx"

    def clean_data(self):    
        self.colX = []
        self.colZ = []
        self.colFSR = []

    def set_file_name(self, new_name):
        self.filename = new_name    

    def file_exists(self):
        return os.path.isfile(self.filename)    

    def get_unique_filename(self, file_name):
        name, ext = os.path.splitext(file_name)
        i = 0
        while os.path.exists(file_name):
            i += 1
            file_name = f"{name}[{i}]{ext}"
        return file_name

    def find_minimum_length(self, array1, array2, array3):
        lengths = [len(array1), len(array2), len(array3)]
        minimum_length = min(lengths)
        return minimum_length 
    
    def resize_arrays(self, array1, array2, array3):
        min_length = min(len(array1), len(array2), len(array3))
        array1 = array1[:min_length]
        array2 = array2[:min_length]
        array3 = array3[:min_length]
        return array1, array2, array3

    def save_file(self):
        d = dict(Pos_X = self.colX, Pos_Z = self.colZ, FSR = self.colFSR)
        df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in d.items() ]))
        self.filename = self.get_unique_filename(self.filename)
        df.to_excel(self.filename, index=False) 
        self.clean_data()

    def append_pos_x(self, pos_x):
        self.colX.append(pos_x)

    def append_pos_z(self, pos_z):
        self.colZ.append(pos_z)

    def append_fsr(self, fsr):
        self.colFSR.append(fsr)   
