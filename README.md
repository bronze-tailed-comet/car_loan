# Car loan

This repository aims to give an example and templates in order to predict if an applicant for a car loan is going to default.

It consists in:
- an airflow server to create a ML pipeline ;
- a PostgreSQL database and tables to store the training set and predictions ;
- an API that calls the model previously trained.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
git clone git@github.com:bronze-tailed-comet/car_loan.git
```

## Usage

```python
cd car_loan

# create an env file that contains the credentials of the API, add the following lines for ex.
# API_USERNAME=api_username
# API_PASSWORD=api_password
nano  .env

# run the containers
docker-compose up -d 
```
Wait until the service is up and you can open a page at [http://localhost:8080](http://localhost:8080).

The credentials to connect to the Airflow UI are in the entrypoint.sh script in the scripts folder.

When you are on the welcoming page of Aiflow, you can go to DAGs, and then run the DAG. It will run the pipeline.

When the pipeline is finished, you have normally the Postgres tables filled and can connect to the Postgres server to check:

```
sudo docker exec -it <container id> psql --username=<username>
\dt
select count(*) from car_loan_train ;

```
To run the tests:
```
sudo docker exec <container id> pytest

```

## License
[MIT](https://choosealicense.com/licenses/mit/)