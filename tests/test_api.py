import pytest
import os

@pytest.mark.asyncio
async def test_post(test_app):
    
    payload = {
                'customer_id':200,
                'main_account_loan_no':4,
                'main_account_active_loan_no':10,
                'main_account_overdue_no':15,
                'main_account_outstanding_loan':1203,
                'main_account_sanction_loan':100,
                'main_account_disbursed_loan':100,
                'sub_account_loan_no':10,
                'sub_account_active_loan_no':100,
                'sub_account_overdue_no':100,
                'sub_account_outstanding_loan':100,
                'sub_account_sanction_loan':100,
                'sub_account_disbursed_loan':100
              }
    response = test_app.post("/car_loan", json=payload, auth=(os.getenv('API_USERNAME'),os.getenv('API_PASSWORD')))
    assert response.status_code == 200
    
@pytest.mark.asyncio
async def test_wrong_payload(test_app):
    
    for payload in [
    {
            'customer_id':"string",  # wrong type here
            'main_account_loan_no':4,
            'main_account_active_loan_no':10,
            'main_account_overdue_no':15,
            'main_account_outstanding_loan':1203,
            'main_account_sanction_loan':100,
            'main_account_disbursed_loan':100,
            'sub_account_loan_no':10,
            'sub_account_active_loan_no':100,
            'sub_account_overdue_no':100,
            'sub_account_outstanding_loan':100,
            'sub_account_sanction_loan':100,
            'sub_account_disbursed_loan':100
    },

    {
            # missing data : customer_id
            'main_account_loan_no':4,
            'main_account_active_loan_no':10,
            'main_account_overdue_no':15,
            'main_account_outstanding_loan':1203,
            'main_account_sanction_loan':100,
            'main_account_disbursed_loan':100,
            'sub_account_loan_no':10,
            'sub_account_active_loan_no':100,
            'sub_account_overdue_no':100,
            'sub_account_outstanding_loan':100,
            'sub_account_sanction_loan':100,
            'sub_account_disbursed_loan':100
    }]:
    
        response = test_app.post("/car_loan", json=payload, auth=(os.getenv('API_USERNAME'),os.getenv('API_PASSWORD')))
        assert response.status_code == 422