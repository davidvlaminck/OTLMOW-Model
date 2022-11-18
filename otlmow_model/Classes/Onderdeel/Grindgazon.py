# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.BegroeidVoorkomen import BegroeidVoorkomen
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grindgazon(BegroeidVoorkomen, VlakGeometrie):
    """Gazontype specifiek op een gestabiliseerde ondergrond. Het is een substraat ontwikkeld om voertuigen sporadisch toe te laten op gazons zonder dat er spoorvorming optreedt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grindgazon'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        BegroeidVoorkomen.__init__(self)
        VlakGeometrie.__init__(self)

        self._isTweelaags = OTLAttribuut(field=BooleanField,
                                         naam='isTweelaags',
                                         label='is tweelaags',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grindgazon.isTweelaags',
                                         definition='Geeft aan of het grindgazon tweelaags of éénlaags is.',
                                         owner=self)

    @property
    def isTweelaags(self) -> bool:
        """Geeft aan of het grindgazon tweelaags of éénlaags is."""
        return self._isTweelaags.get_waarde()

    @isTweelaags.setter
    def isTweelaags(self, value):
        self._isTweelaags.set_waarde(value, owner=self)
