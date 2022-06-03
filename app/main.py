import os
import secrets
from pydantic import BaseModel
from fastapi import FastAPI, Depends, Request, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.encoders import jsonable_encoder

from app.predict import predict

app = FastAPI(title="FastAPI, Docker, and Traefik")

security = HTTPBasic()


class CarLoanData(BaseModel):
    customer_id : int
    main_account_loan_no : int
    main_account_active_loan_no : int
    main_account_overdue_no : int
    main_account_outstanding_loan : int
    main_account_sanction_loan : int
    main_account_disbursed_loan : int
    sub_account_loan_no : int
    sub_account_active_loan_no : int
    sub_account_overdue_no : int
    sub_account_outstanding_loan : int
    sub_account_sanction_loan : int
    sub_account_disbursed_loan : int
        
        
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):

    correct_username = secrets.compare_digest(credentials.username, os.getenv('API_USERNAME'))
    correct_password = secrets.compare_digest(credentials.password, os.getenv('API_PASSWORD'))
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.post("/car_loan")
async def getInformation(data: CarLoanData, username: str = Depends(get_current_username)):

    return predict(jsonable_encoder(data))