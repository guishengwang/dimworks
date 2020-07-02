import pandas as pd
import numpy as np

def get_pp( data_1d: pd.Series, USL: float, LSL: float):
    
    std=data_1d.std()

    if std>0 :
        pp = (USL - LSL) / 6 * data_1d.std()
    else:
        pp=0
        
    return pp

    
def get_ppk():

    ppk=2
    return ppk
   
def get_cp():
    cp=3
    return cp

def get_cpk():
    cpk=4
    return cpk
    
def get_xbar():
    xbar=4
    return xbar
    