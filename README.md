# OTLMOW-Model
[![PyPI](https://img.shields.io/pypi/v/otlmow-model?label=latest%20release)](https://pypi.org/project/otlmow-model/)
[![otlmow-model-downloads](https://img.shields.io/pypi/dm/otlmow-model)](https://pypi.org/project/otlmow-model/)
[![Unittests](https://github.com/davidvlaminck/OTLMOW-Model/actions/workflows/unittest.yml/badge.svg)](https://github.com/davidvlaminck/OTLMOW-Model/actions/workflows/unittest.yml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/otlmow-model)
[![GitHub issues](https://img.shields.io/github/issues/davidvlaminck/OTLMOW-Model)](https://github.com/davidvlaminck/OTLMOW-Model/issues)

## Summary
The main use case of otlmow-model is to provide a class model, allowing instances of OTL compliant classes. The classes have data validation and automatic conversion for attributes and relations between objects.

## OTLMOW Project 
This project aims to implement the Flemish data standard OTL (https://wegenenverkeer.data.vlaanderen.be/) in Python.
It is split into different packages to reduce compatibility issues
- [otlmow_model](https://github.com/davidvlaminck/OTLMOW-Model) (you are currently looking at this package)
- [otlmow_modelbuilder](https://github.com/davidvlaminck/OTLMOW-ModelBuilder)
- [otlmow_converter](https://github.com/davidvlaminck/OTLMOW-Converter) 
- [otlmow_template](https://github.com/davidvlaminck/OTLMOW-Template) 
- [otlmow_postenmapping](https://github.com/davidvlaminck/OTLMOW-PostenMapping) 

## Installation and requirements
OTLMOW-Model has no dependencies other than the standard Python libraries. Currently, you need at least Python version 3.6 to use this library.
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
```
results in
```
<Camera> object
    typeURI : https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera
    isPtz : True
    naam : CAM0001
    opstelhoogte :
        waarde : 6.0
    toestand : in-gebruik
```
Access the metadata information by using the meta_info function. Pass in an object. Optionally you can use also pass an attribute to view the metadata of attributes itself
```
from otlmow_model.BaseClasses.MetaInfo import meta_info
print(meta_info(c, attribute='toestand'))
```
outputs
```  
Showing metadata of toestand:
typeURI: https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMToestand.toestand
definition: Geeft de actuele stand in de levenscyclus van het object.
valid values:
    geannuleerd
    gepland
    in-gebruik
    in-ontwerp
    in-opbouw
    overgedragen
    uit-gebruik
    verwijderd
```
The model also has access to all valid relations within the model. You can query the model to check if a relation of a 
given type is valid between two instances of objects within the model. Use the RelationValidator class and one of its functions.
```
from otlmow_model.Classes.Onderdeel.Camera import Camera
from otlmow_model.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.Classes.Onderdeel.Wegkantkast import Wegkantkast
from otlmow_model.Helpers.RelationValidator import RelationValidator

camera = Camera()
kast = Wegkantkast()

camera_kast_bevestiging = RelationValidator.is_valid_relation(source=camera, target=kast, relation_type=Bevestiging)
print(camera_kast_bevestiging)
```
After executing the code above, the output is "False".
