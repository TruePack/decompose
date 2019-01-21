# Project Title 

Web Application, decomposes the number into prime factors. 

## Getting Started 


### Prerequisites 

For install web-app in containerization environment you need 
[Docker](https://www.docker.com/).

### Installing 
#### Build container
First you need to collect the docker-container with the help
Dockerfile. 
You can get this by executing the command from the directory with the
 Dockerfile.
```
docker build -t mathcalc .
``` 
#####Details: 
```
docker build
```
Build an image from a Dockerfile.\
Usage:	docker build [OPTIONS] PATH | URL | -

```
-t mathcalc
```
-t sets the name to the image.

```
.
```
Path to Dockerfile.

#### Run image

Then you need start your built image.
``` 
docker run --rm -it -p 8000:8000 mathcalc 
``` 

#####Details:

```
docker run
```
Run a command in a new container.\
Usage:	docker run [OPTIONS] IMAGE [COMMAND] [ARG...]


```
--rm
```
Automatically remove the container when it exits.


```
-t, --tty
```
Allocate a pseudo-terminal.


```
-p 8000:8000
```
Publish a container's port to the host.


```
mathcalc
```
Name of image which running.

#### Finally

And if everything ok, you will see the message in terminal:
```
Performing system checks...

System check identified no issues (0 silenced).
January 21, 2019 - 04:52:52
Django version 2.1.5, using settings 'mathcalc.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.

```

Now you can visit app on you local machine with browser on 
localhost:8000 (127.0.0.0:8000).


## Built With 

* [Django](https://www.djangoproject.com/) - The web framework used 
* [Docker](https://www.docker.com/) - Containerization system 

## Authors 

* **Anton Shnayder** - *Test work* - [TruePack](https://github.com/TruePack) 

