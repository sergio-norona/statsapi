# statsapi

Python RESTful api  with docker for dna mutant sequence validation statistics for Magneto recruitments.

## Local environment Requirements

- Python 3.x
- Docker
- Mysql - xampp

## Cloud environment Requirements

- AWS ElasticBeanStalk environment with Docker running on 64bit Amazon Linux 2/3.1.0
- Mysql RDS

## Tools and Installs

- docker
- python
- mysql - xampp
- jmeter - for load tests
- postman - for testing rest request


# Setup

## Local environment Python only - without docker

```bash
$ pip install -r requirements.txt
```
- Install xampp and setup up a new mysql instance
- Start apache and mysql services from xampp console
- If database is not exist yet, use emptydatabasescript/mutants.sql for importing an empty database structure to mysql
- Create a user and credentials for the new database
- Configure your 127.0.0.0:3306 as your default mysql host at db.yaml file or your own mysql host, port and credentials.
- Replace config.yaml with config-local-env-without-docker.yaml content

```bash
$ python run.py
```

## Local environment with docker

- Start apache and mysql services from xampp console
- Configure your local ip in db.yaml running ipconfig on cmd console
- Replace config.yaml with config-local-env-without-docker.yaml content

```bash
$ docker-compose build
$ docker-compose up
```



# Usage

## statsapi urls

- Amazon AWS: http://magnetostats.us-east-2.elasticbeanstalk.com
- Local environment docker: http://127.0.0.1:5000 (use a different port in docker-compose.yml if you are running two or more services at the same time)
- Local environment without docker: http://127.0.0.1:8080

## Example request


GET → /stats/    


## Example response

Response Code   
200-OK  

Response Body 
```json
{
"count_mutant_dna": 40,
"count_human_dna": 100,
"ratio": 0.4
} 
```



## Code Coverage

```bash
$ coverage run test_mutantvalidation.py

$ coverage report

Name                Stmts   Miss  Cover
---------------------------------------
stats\__init__.py      49      3    94%
test_statsapi.py       32      0   100%
---------------------------------------
TOTAL                  81      3    96%
```

## Unit tests

```bash
$ python test_statsapi.py

...
----------------------------------------------------------------------
Ran 3 tests in 5.526s

OK
```



## Performance Tests

Jmeter setup

- pending to complete

Local Jmeter load test

- pending to complete

## mutantapi

Service for mutant dna sequence validation for Magneto recruitments

[statsapi github repository url](https://github.com/sergion2010/mutantapi)

## Contributing

Pull requests are welcome. For major changes, please open an issue first, or contact me at ... to discuss what you would like to change.

Please make sure to update tests as appropriate.
