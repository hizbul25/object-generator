
# Random Object Generator

Write a Web app using Flask (Python) to generate four (4) types of printable random objects and store them in a single file, each object will be separated by a ",".  These are the 4 objects: alphabetical strings, real numbers, integers, alphanumerics.
Sample extracted output:
```
hisadfnnasd, 126263, assfdgsga12348fas, 13123.123, 
lizierdjfklaasf, 123192u3kjwekhf, 89181811238,122, 
nmarcysfa900jkifh  , 3.781, 2.11, ....
```

 The output should be 2MB in size. Once file generation is done the output should be available as a link which can be then downloaded by clicking on it. Also, there should be a button on the page so by clicking on this button the total number of each random objects will be displayed.


## Getting Started

### Prerequisites

- Python 3.8 or higher
- Flask
- Docker

### Project setup

```sh
# clone the repo
$ git clone https://github.com/hizbul25/object-generator.git

# move to the project folder
$ cd object-generator
```
## Running the Docker Container

- We have the Dockerfile created in above section. Now, we will use the Dockerfile to create the image of the object_generator app and then start the object_generator app container.


```sh
$ docker-compose up --build

```

## Functional test
```sh
$ docker-compose exec app sh
$ python -m pytest

```

## API End Point

- To Generate random object please run following api endpoint in any api client. [POST] request.

```sh
 http://0.0.0.0:5000/api/v1/generate-object

```

- To get the report of random object please run following api endpoint in any api client: [GET] request.

```sh
 http://0.0.0.0:5000/api/v1/generate-report

```
