CREATE TABLE IF NOT EXISTS car_loan_serving (
    customer_id SERIAL PRIMARY KEY,
    features JSON,
    pred NUMERIC,
    pred_proba NUMERIC
);