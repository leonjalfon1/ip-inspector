# IP INSPECTOR

## Description

This application can be used to get the source IP of an specific client (very useful for debugging and testing)

## Build

To build the application as docker image use:

```
docker build -t leonjalfon1/ip-inspector:latest
```

## Usage

To run the application as docker container use:
```
docker run -p 5000:5000 leonjalfon1/ip-inspector:latest
```

Then you will be able to access the application in port 5000
```
http://localhost:5000
```