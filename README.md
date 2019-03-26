# serverless-mxnet

An attempt to get mxnet 1.4.0 running on lambda with gluon 0.3.0

This project uses serverless-python-requirements to install mxnet and gluon and spit the requirements into a layer to overcome lambda size limits.

```hadler.py``` import both libraries and then returns a string message.

Currently the imports fail

```Unable to import module 'handler': /opt/python/PIL/_imaging.cpython-36m-x86_64-linux-gnu.so: ELF load command address/offset not properly aligned```