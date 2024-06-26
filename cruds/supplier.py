from sqlalchemy.orm import Session
from models import supplier as model_supplier
from schemas import supplier as schema_supplier
from typing import List


def create_supplier(db: Session, supplier: schema_supplier.SupplierCreate):
    db_supplier = model_supplier.Supplier(**supplier.model_dump())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def get_suppliers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_supplier.Supplier).offset(skip).limit(limit).all()

def get_supplier(db: Session, supplier_id: int):
    db_supplier = db.query(model_supplier.Supplier).filter(
        model_supplier.Supplier.id == supplier_id).first()
    if db_supplier is None:
        return None
    return db_supplier

def update_supplier(db: Session, supplier: schema_supplier.SupplierUpdate):
    db_supplier = db.query(model_supplier.Supplier).filter(
        model_supplier.Supplier.id == supplier.id).first()
    if db_supplier is None:
        return None
    for key, value in supplier.model_dump().items():
        setattr(db_supplier, key, value)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def delete_supplier(db: Session, supplier_id: int):
    db_supplier = db.query(model_supplier.Supplier).filter(
        model_supplier.Supplier.id == supplier_id).first()
    if db_supplier is None:
        return None
    db.delete(db_supplier)
    db.commit()
    return db_supplier

