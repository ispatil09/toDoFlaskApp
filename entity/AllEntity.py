# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:29:03 2022

@author: Ishwar
"""
import pickle

class ToDo:
    def __init__(self,sl_no,title,desc):
        self.sl_no=sl_no
        self.title=title
        self.desc=desc

    def __str__(self):
        #print('In str')
        return f"Sr {self.sl_no}- {self.title}:{self.desc}"
    
class SaveData:
    def __init__(self, lst):
       with open("ToDoData.dat","wb") as f:
           pickle.dump(lst, f)
           
class LoadData:
    def __init__(self):
        with open("ToDoData.dat", "rb") as f:
            self.lst = pickle.load(f)
    
    def getAll(self):
        return self.lst