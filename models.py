from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    items = relationship("Item", back_populates="owner")
    trafo = relationship("Trafo", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Trafo(Base):
    __tablename__ = "trafo"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    kapasitas = Column(Integer, nullable=False)
    voltase = Column(Integer, nullable=False)
    current = Column(Integer, nullable=False)
    phasa = Column(String, nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    group_id = Column(Integer, ForeignKey("group_trafo.id"), nullable=True)

    owner = relationship("User", back_populates="trafo")
    group = relationship("GroupTrafo", back_populates="trafo")

class GroupTrafo(Base):
    __tablename__ = "group_trafo"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    kodegrup = Column(String, nullable=False)
    
    trafo = relationship("Trafo", back_populates="group")
 
class HasilKalkulasi(Base):
    __tablename__ = "hasil_kalkulasi"

    id = Column(Integer, primary_key=True, index=True)
    vr = Column(Float, nullable=False)
    vs = Column(Float, nullable=False)
    vt = Column(Float, nullable=False)
    ir = Column(Float, nullable=False)
    is_ = Column(Float, nullable=False)
    it = Column(Float, nullable=False)
    cosphi = Column(Float, nullable=False)
    kvar = Column(Float, nullable=False)
    kvas = Column(Float, nullable=False)
    kvat = Column(Float, nullable=False)
    kwr = Column(Float, nullable=False)
    kws = Column(Float, nullable=False)
    kwt = Column(Float, nullable=False)
    kvar_r = Column(Float, nullable=False)
    kvar_s = Column(Float, nullable=False)
    kvar_t = Column(Float, nullable=False)
    total_kva = Column(Float, nullable=False)
    total_kw = Column(Float, nullable=False)
    total_kvar = Column(Float, nullable=False)
    sisa_kapasitas = Column(Float, nullable=False)
    tanggal = Column(String, nullable=False)
    idtrafo = Column(Integer, ForeignKey("trafo.id"), nullable=False)
    
    trafo = relationship("Trafo", back_populates="hasil_kalkulasi")
    
