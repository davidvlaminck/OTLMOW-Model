# OTLMOW-Model
## Summary
The main use case of otlmow-model is to provide a class model, allowing instances of OTL compliant classes. The classes have data validation and automatic conversion for attributes and relations between objects.

## OTLMOW Project 
This project aims to implement the Flemish data standard OTL (https://wegenenverkeer.data.vlaanderen.be/) in Python.
It is split into different packages to reduce compatibility issues
- otlmow-model (you are currently looking at this package)
- otlmow-modelbuilder
- otlmow_converter
- otlmow_template

## Installation and requirements
OTLMOW-Model has no dependencies other than the standard Python libraries. Currently, you need at least Python version 3.8 to use this library.
To install the OTL MOW project into your Python project, use pip to install it:
``` 
pip install otlmow-model
```
To upgrade an existing installation use:
``` 
pip install otlmow-model --upgrade
```
## Usage and code examples
To use any of the classes in the class model, instantiate a class after importing it. In this example the Camera class is used.
```
from otlmow_model.Classes.Onderdeel.Camera import Camera
c = Camera()
```
Now, this Camera instance can be edited by accessing its properties.
```
c.toestand = 'in-gebruik'
c.naam = 'CAM0001'
c.opstelhoogte.waarde = 6.0
```
Validation or conversion happens behind the scenes.
You'll also get warnings for using deprecated classes or attributes.
```
c.isPtz = 'True'  # this raises a warning, as the value can be interpreted but is not the correct type
c.isPtz = 20  # raises a CouldNotConvertToCorrectTypeError
```
Inspect the object by printing it.
```
print(c)
# results in #
<Camera> object
    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera
    isPtz : True
    naam : CAM0001
    opstelhoogte :
        waarde : 6.0
    toestand : in-gebruik
```


