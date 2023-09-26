# coding=utf-8
from otlmow_model.Classes.Abstracten.HoutigeVegetatie import HoutigeVegetatie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Heestermassief(HoutigeVegetatie, VlakGeometrie):
    """Heestertype gekenmerkt door een gesloten, massieve structuur, waarbij de individuele heesters moeilijk te onderscheiden zijn tot 1 meter hoogte. Verzameling van meerdere soorten houtige planten die elk afzonderlijk worden beheerd of als één massief waarbij de uitstraling van het geheel primeert op het beheer van individuele plantensoorten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Heestermassief'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
