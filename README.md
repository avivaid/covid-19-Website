# Covid -19 Website
  This was done for the final project of CSUChico CINS 465 class. 

## Developers

* [Aviral Vaid](https://github.com/avivaid)

## Getting started 
* [Install docker and docker-compose](https://docs.docker.com/get-docker/)
* Build the docker frontend contanier with the command 
``` docker-compose build web ```
* You can run the docker contanier as a bash shell with the command 
```docker-compose run contanier-name /bin/bash ``` or ```docker-compose run contanier-name bash ```
* Build the entire thing
```docker-compose up --build```
* You might have to run migratiuions. 
```docker-compose run web bash ```
```cd mysite ```
``` python manage.py makemigrations```
```python manage.py migrate ```
* You can bring up the container with the command 
```sudo docker-compose up ```



