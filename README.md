# OTLMOW-Model
## OTLMOW Project 
This project aims to implement the Flemish data standard OTL (https://wegenenverkeer.data.vlaanderen.be/) in Python.
It is split into different packages to reduce compatibility issues
- otlmow_model (you are currently looking at this package)
- otlmow_modelbuilder
- otlmow_transformer

## Installation and requirements
To install the OTL MOW project into your python project, use pip to install it:
``` 
pip install otlmow_model
```
To upgrade an existing installation use:
``` 
pip install otlmow_model --upgrade
``` 
## Creating the OTL datamodel using the OTL SQLite
With every OTL update, you can run main.py to allow the creation of an updated Python datamodel. The generated classes are not backwards compatible.