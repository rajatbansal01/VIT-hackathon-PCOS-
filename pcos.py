from pydantic import BaseModel
# class which contains the parameters of PCOS disease.
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