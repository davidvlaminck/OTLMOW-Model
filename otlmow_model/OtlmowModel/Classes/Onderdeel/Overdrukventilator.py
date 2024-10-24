# coding=utf-8
from ...Classes.Abstracten.Ventilatie import Ventilatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Overdrukventilator(Ventilatie):
    """Onderdeel dat tot doel heeft overdruk te creëren in een gesloten ruimte zodat bij het openen van de ruimte enkel lucht kan ontsnappen naar buiten en geen lucht, rook, partikels, ... naar binnen te laten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overdrukventilator'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtganginrichting', direction='o')  # o = direction: outgoing
