# coding=utf-8
from ...Classes.Abstracten.WaterloopRelatie import WaterloopRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Waterweg(WaterloopRelatie):
    """Een waterweg is, volgens het juridisch statuut, een bevaarbaar waterlichaam dat zorgt voor het transporteren van de horizontale afvloeiing van neerslag- en bronwater en zich typisch leent tot scheepvaart."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Waterweg'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
