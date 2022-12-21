# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Deur import Deur
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Toegangsdeur(Deur, AIMNaamObject, PuntGeometrie):
    """Element dat de doorgang naar een ruimte (in een gebouw) afsluit of er toegang toe verleent. De doorgang is minder breed dan die die afgesloten wordt door een toegangspoort."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsdeur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        Deur.__init__(self)
        PuntGeometrie.__init__(self)

        self._isBinnendraaiend = OTLAttribuut(field=BooleanField,
                                              naam='isBinnendraaiend',
                                              label='is binnendraaiend',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangsdeur.isBinnendraaiend',
                                              definition='Geeft aan of de deur in de af te sluiten ruimte draait of er weg van.',
                                              owner=self)

    @property
    def isBinnendraaiend(self) -> bool:
        """Geeft aan of de deur in de af te sluiten ruimte draait of er weg van."""
        return self._isBinnendraaiend.get_waarde()

    @isBinnendraaiend.setter
    def isBinnendraaiend(self, value):
        self._isBinnendraaiend.set_waarde(value, owner=self)
