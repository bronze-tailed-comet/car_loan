CREATE TABLE IF NOT EXISTS car_loan_pred (
    customer_id SERIAL PRIMARY KEY,
    features JSON,
    pred NUMERIC,
    pred_proba NUMERIC
);