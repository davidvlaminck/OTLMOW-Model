# OTLMOW-Model
[![PyPI](https://img.shields.io/pypi/v/otlmow-model?label=latest%20release)](https://pypi.org/project/otlmow-model/)
[![otlmow-model-downloads](https://img.shields.io/pypi/dm/otlmow-model)](https://pypi.org/project/otlmow-model/)
[![Unittests](https://github.com/davidvlaminck/OTLMOW-Model/actions/workflows/unittest.yml/badge.svg)](https://github.com/davidvlaminck/OTLMOW-Model/actions/workflows/unittest.yml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/otlmow-model)
[![GitHub issues](https://img.shields.io/github/issues/davidvlaminck/OTLMOW-Model)](https://github.com/davidvlaminck/OTLMOW-Model/issues)
[![coverage](https://github.com/davidvlaminck/OTLMOW-Model/blob/master/UnitTests/coverage.svg)](https://htmlpreview.github.io/?https://github.com/davidvlaminck/OTLMOW-Model/blob/master/UnitTests/htmlcov/index.html)


## Summary
The main use case of otlmow-model is to provide a class model, allowing instances of OTL compliant classes. The classes have data validation and automatic conversion for attributes. Helper classes assist you to create relations between objects.

## Code examples and usage
See the [Readme notebook](https://github.com/davidvlaminck/OTLMOW-Model/blob/master/Readme.ipynb). This notebook contains examples on how to use the OTL classes and how to create relations between objects.

## Project overview 
This project aims to implement the Flemish data standard OTL (https://wegenenverkeer.data.vlaanderen.be/) in Python.
It is split into different packages to reduce compatibility issues.
- [otlmow_model](https://github.com/davidvlaminck/OTLMOW-Model) (you are currently looking at this package)
- [otlmow_modelbuilder](https://github.com/davidvlaminck/OTLMOW-ModelBuilder)
- [otlmow_converter](https://github.com/davidvlaminck/OTLMOW-Converter)
- [otlmow_template](https://github.com/davidvlaminck/OTLMOW-Template)
- [otlmow_postenmapping](https://github.com/davidvlaminck/OTLMOW-PostenMapping)
- [otlmow_davie](https://github.com/davidvlaminck/OTLMOW-DAVIE)
- [otlmow_visuals](https://github.com/davidvlaminck/OTLMOW-Visuals)
- [otlmow_gui](https://github.com/davidvlaminck/OTLMOW-GUI)

The **otlmow-model** project is a Python implementation model of the OTL standard. This is a collection of OTL compliant classes, which can be used to create instances of OTL objects. When assigning data to the attributes of the classes, the data is validated and converted to the correct type (if incorrect). There is support for conversion from and to Python dictionaries.

A few times during a year a new version of the OTL standard is released. The **otlmow-modelbuilder** project takes an OTL SQLite as input and generates the classes for the new version of the OTL standard. The otlmow-model project is then updated with the new classes. This way the otlmow-model project is always up to date with the latest version of the OTL standard.

In the **otlmow-converter** project, the instantiated classes can be converted to and from DAVIE compliant file formats (such as CSV, Excel, ...). There is also support for json-ld files. The objects can also be converted to dotnotation dictionaries or loaded into or from a pandas Dataframe. Because of all these possibilities, the converter has multiple dependencies on other Python packages.

The **otlmow-template** project produces a CSV or Excel template, based on a subset of the OTL. The created template can then be used to input data and upload into the DAVIE platform of AWV.

The **otlmow-postenmapping** project implements the mapping artifact and allow the creation or modification of OTL objects.

The **otlmow-davie** project has a REST client to the DAVIE platform to allow automation of deliveries.

The **otlmow-visuals** project provides a way to visualize OTL objects and their relations. The result is an interactive HTML file that can be opened in any browser.

The **otlmow-gui** project is a deployable local application that allows the user to create templates, edit, visualize and export data.
