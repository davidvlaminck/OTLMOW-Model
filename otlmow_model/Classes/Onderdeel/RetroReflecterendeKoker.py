# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlRetroreflecterendeKokerFolieType import KlRetroreflecterendeKokerFolieType
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class RetroReflecterendeKoker(AIMObject, PuntGeometrie):
    """Een kunststoffen koker bevestigd rond een steun om de zichtbaarheid van verkeerseilanden te verhogen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroReflecterendeKoker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendeFolie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun')

        self._folieType = OTLAttribuut(field=KlRetroreflecterendeKokerFolieType,
                                       naam='folieType',
                                       label='folie type',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroReflecterendeKoker.folieType',
                                       definition='Een keuzelijst het folietype van reflecterende koker te bepalen.',
                                       owner=self)

    @property
    def folieType(self) -> str:
        """Een keuzelijst het folietype van reflecterende koker te bepalen."""
        return self._folieType.get_waarde()

    @folieType.setter
    def folieType(self, value):
        self._folieType.set_waarde(value, owner=self)
