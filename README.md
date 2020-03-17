# IP INSPECTOR

## Description

 - Simple python web server that retrieve the IP of the client who accesses it.
 - This application can be very useful for debugging and testing

## Build

 - To build the application as docker image use:

```
docker build -t leonjalfon1/ip-inspector:latest
```

## Usage

 - To run the application as docker container use:
```
docker run -p 5000:5000 leonjalfon1/ip-inspector:latest
```

 - Then you will be able to access the application on port 5000
```
http://localhost:5000
```
