from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import supplier as model_supplier
from cruds import supplier as crud_supplier
from schemas import supplier as schema_supplier

router = APIRouter()
tags = ["Supplier"]

@router.post("/supplier", response_model=schema_supplier.Supplier, tags=tags)
def create_supplier(supplier: schema_supplier.SupplierCreate, db: Session = Depends(get_db)):
    return crud_supplier.create_supplier(db, supplier)

@router.get("/supplier/{supplier_id}", response_model=schema_supplier.Supplier, tags=tags)
def read_supplier(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = crud_supplier.get_supplier(db, supplier_id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

@router.get("/suppliers", response_model=schema_supplier.Suppliers, tags=tags)
def read_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    suppliers = crud_supplier.get_suppliers(db, skip=skip, limit=limit)
    total_count = db.query(model_supplier.Supplier).count()
    return {
        "suppliers": suppliers,
        "total_count": total_count
    }

@router.put("/suppliers", response_model=schema_supplier.Supplier, tags=tags)
def update_supplier(supplier: schema_supplier.SupplierUpdate, db: Session = Depends(get_db)):
    db_supplier = crud_supplier.get_supplier(db, supplier.id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    db_supplier = crud_supplier.update_supplier(db, supplier)
    return db_supplier

@router.delete("/supplier/{supplier_id}", tags=tags)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = crud_supplier.get_supplier(db, supplier_id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return crud_supplier.delete_supplier(db, supplier_id)
