# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020
@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class PCOS(BaseModel):
    Age: int 
    Weight: float 
    Height: float 
    Cycle: int
    Cyclelength: int
    Fsh: float
    Lh: float
    Frl: float
    Tsh: float
    Amh: float
    Rbs: float
    Weightgain: int
    Hairgrowth: int
    Skindarkening: int
    Hairloss: int
    Pimples: int
    Fastfood: float
    Regexercise: int
    FollicleR: int
    FolliclL: int