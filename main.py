from fastapi import FastAPI
from database import SessionLocal
from models import Operation
from calculator import rpn_calculate
from typing import List
import csv
from fastapi.responses import StreamingResponse
from io import StringIO
from fastapi.middleware.cors import CORSMiddleware
#from database import init_db

#init_db()

app = FastAPI()
# Configurer les autorisations CORS pour autoriser les requêtes provenant de http://localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Autorise uniquement les requêtes venant du frontend React
    allow_credentials=True,
    allow_methods=["*"],  # Autorise toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autorise tous les en-têtes
)

@app.post("/calculate/")
async def calculate(expression: List[str]):
    result = rpn_calculate(expression)
    db = SessionLocal()
    db_operation = Operation(expression=" ".join(expression), result=result)
    db.add(db_operation)
    db.commit()
    db.refresh(db_operation)
    return {"result": result}

@app.get("/operations/csv/")
async def get_operations_csv():
    db = SessionLocal()
    operations = db.query(Operation).all()
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Expression", "Result"])
    for op in operations:
        writer.writerow([op.id, op.expression, op.result])
    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=operations.csv"})