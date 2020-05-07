## Installation / Usage places API

#### Dependencies
* You need create a virtual environment and install the requirements.txt with pip:
    ```
    $ pip install -r requirements.txt
    ```

#### Running API in your localhost
* Make sure that you are in solution/PlanD_API. Create the database and runserver:
    * You need to have a PostgreSQL database named 'places' running on port 5432 with user and password 'postgres'
    ```
    $ python manage.py migrate
    ```
    ```
    $ python manage.py runserver
    ```
    ```
    $ python manage.py createsuperuser
    ```

#### Running tests
* Make sure that you are in solution/PlanD_API and run:
    ```
    $ python manage.py test
    ```
#### Endpoints

* **You can use heroku or your local endpoint**

* Base endpoint:
    
        https://pland-api-lucasgsouza03.herokuapp.com/
        http://localhost:8000/
        http://127.0.0.1:8000/
    

* Before you must define the requequest:
         
        import requests
        from requests.auth import HTTPBasicAuth  

        url = 'https://$url-to-api/place/'
        

* Request Syntax to create a place:
        
        data={
            "name": "String",
            "slug": "String",
            "city": "String",
            "state": "String"
        }
        
        response = requests.post(url, data, auth=('user_created', 'password_created'))
        

* Request Syntax to update a place:
        
        url = url + '<slug>/'
        data={
            "name": "String",
            "slug": "String",
            "city": "String",
            "state": "String"
        }
        response = requests.put(url, data, auth=('user_created', 'password_created'))
        

* Request Syntax to get all places:
          
        response = requests.get(url, auth=('user_created', 'password_created'))

* Request Syntax to get a specific place:

        url = url + '<slug>/'
        response = requests.get(url, auth=('user_created', 'password_created'))

* Request Syntax to delete a place:
        
        url = url + '<slug>/'
        response = requests.put(url, auth=('user_created', 'password_created'))

* Response Syntax to create, update and get a specific place:
    
        {
            "id": Int,
            "name": String,
            "slug": "String",
            "city": "String",
            "state": "String",
            "created_at": "String"
            "updated_at": "String"
        }

* Response Syntax to list places:
    
        [
            {
                "id": Int,
                "name": String,
                "slug": "Slug",
                "city": "String",
                "state": "String",
                "created_at": "String"
                "updated_at": "String"
            }
        ]

* Delete a place returns 204 status only.
    * Delete without passing slug is considered not allowed for safety

#### Status table

| Code | Status |
|:-------:|:---------:|
| 200   | OK |
| 201   | CREATED |
| 204   | NO_CONTENT |
| 400   | BAD_REQUEST |
| 404   | NOT_FOUND |
| 405   | METHOD_NOT_ALLOWED |
