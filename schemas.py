from pydantic import BaseModel
from typing import Optional, List

# --- USER ---
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        from_attributes = True

# --- TRAFO ---
class TrafoBase(BaseModel):
    group_id: int
    name: str
    type: str
    brand: str
    kapasitas: int
    voltase: int
    current: int
    phasa: str
    longitude: float
    latitude: float

class TrafoCreate(TrafoBase):
    pass

class Trafo(TrafoBase):
    id: int
    class Config:
        from_attributes = True
        
# --- GROUP TRAFO ---
class GroupTrafoBase(BaseModel):
    name: str
    kodegrup: str

class GroupTrafoCreate(GroupTrafoBase):
    pass

class GroupTrafo(GroupTrafoBase):
    id: int
    class Config:
        from_attributes = True
        
# --- HASIL KALKULASI ---
class HasilKalkulasiBase(BaseModel):
    vr: float
    vs: float
    vt: float
    ir: float
    is_: float
    it: float
    cosphi: float
    kvar: float
    kvas: float
    kvat: float
    kwr: float
    kws: float
    kwt: float
    kvar_r: float
    kvar_s: float
    kvar_t: float
    total_kva: float
    total_kw: float
    total_kvar: float
    sisa_kapasitas: float
    tanggal: str
    idtrafo: int

class HasilKalkulasiCreate(HasilKalkulasiBase):
    pass

class HasilKalkulasi(HasilKalkulasiBase):
    id: int
    class Config:
        from_attributes = True

# --- Combobox ---
class Combobox(BaseModel):
    id: int
    name: str
