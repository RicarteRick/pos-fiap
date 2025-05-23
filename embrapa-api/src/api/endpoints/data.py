from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.engine import Connection
from src.config.database import get_db
from src.core.services.data_service import insert_all_data, get_data_by_module

router = APIRouter()

@router.post("/import-all")
def import_all_data(db: Connection = Depends(get_db)):
    try:
        insert_all_data(db)
        return {"message": "All data imported successfully."}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get("/product")
def get_product_data(db: Connection = Depends(get_db)):
    try:
        data = get_data_by_module("product", db)
        return {"module": "product", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get("/process")
def get_process_data(db: Connection = Depends(get_db)):
    try:
        data = get_data_by_module("process", db)
        return {"module": "process", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get("/sales")
def get_sales_data(db: Connection = Depends(get_db)):
    try:
        data = get_data_by_module("sales", db)
        return {"module": "sales", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get("/import")
def get_import_data(db: Connection = Depends(get_db)):
    try:
        data = get_data_by_module("import", db)
        return {"module": "import", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@router.get("/export")
def get_export_data(db: Connection = Depends(get_db)):
    try:
        data = get_data_by_module("export", db)
        return {"module": "export", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")