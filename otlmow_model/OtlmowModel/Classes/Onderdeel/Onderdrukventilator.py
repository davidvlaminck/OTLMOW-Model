# coding=utf-8
from ...Classes.Abstracten.Ventilatie import Ventilatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderdrukventilator(Ventilatie):
    """Onderdeel dat tot doel heeft onderdruk te creëren in een gesloten ruimte zodat bij het openen van de ruimte geen lucht kan ontsnappen naar de omgeving en dus om lucht,rook,partikels,... in de ruimte te houden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdrukventilator'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
