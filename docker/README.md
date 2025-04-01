# FastAPI Tutorial: Dockerization

[Back](../README.md)

- [FastAPI Tutorial: Dockerization](#fastapi-tutorial-dockerization)

```sh
docker build -t myimage .
docker rmi myimage

docker run -d --name mycontainer -p 8080:8080 myimage
docker rm mycontainer
docker container stop mycontainer
```
