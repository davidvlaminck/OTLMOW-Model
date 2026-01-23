# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...BaseClasses.StringField import StringField
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ArtikelnummerObject(PuntGeometrie):
    """Abstracte klasse voor een artikelnummer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ArtikelnummerObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._artikelnummer = OTLAttribuut(field=StringField,
                                           naam='artikelnummer',
                                           label='artikelnummer',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ArtikelnummerObject.artikelnummer',
                                           definition='een identificatienummer dat een product of producttype aanduidt en dat wordt gebruikt als referentie voor de bijbehorende samenstelling en configuratie.',
                                           owner=self)

    @property
    def artikelnummer(self) -> str:
        """een identificatienummer dat een product of producttype aanduidt en dat wordt gebruikt als referentie voor de bijbehorende samenstelling en configuratie."""
        return self._artikelnummer.get_waarde()

    @artikelnummer.setter
    def artikelnummer(self, value):
        self._artikelnummer.set_waarde(value, owner=self)
