# OTLMOW-Model
## OTLMOW Project 
This project aims to implement the Flemish data standard OTL (https://wegenenverkeer.data.vlaanderen.be/) in Python.
It is split into different packages to reduce compatibility issues
- otlmow_model (you are currently looking at this package)
- otlmow_modelbuilder
- otlmow_converter

## Installation and requirements
OTLMOW-Model has no dependencies other than de standard Python libraries. Currently, you need at least Python version 3.8 to use this library.
To install the OTL MOW project into your Python project, use pip to install it:
``` 
pip install otlmow_model
```
To upgrade an existing installation use:
``` 
pip install otlmow_model --upgrade
``` 
## Creating the OTL datamodel using the OTL SQLite
With every OTL update, you can run main.py to allow the creation of an updated Python datamodel. The generated classes are not backwards compatible.