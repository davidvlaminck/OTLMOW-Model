# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Waarschuwingslantaarn import Waarschuwingslantaarn
from ...Datatypes.KlSeinlantaarnDiameter import KlSeinlantaarnDiameter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vooraankondiging(Waarschuwingslantaarn):
    """Geheel van één of meerdere knipperlantaarns,inclusief knipperdoos,bevestigd op een draagconstructie ter waarschuwing (ter benadering) van een verkeerslichtengeregeld kruispunt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vooraankondiging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming

        self._diameterLens = OTLAttribuut(field=KlSeinlantaarnDiameter,
                                          naam='diameterLens',
                                          label='diameter lens',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vooraankondiging.diameterLens',
                                          definition='De diameter van de lens van de verkeerslichten waaruit de vooraankondiging is samengesteld.',
                                          owner=self)

    @property
    def diameterLens(self) -> str:
        """De diameter van de lens van de verkeerslichten waaruit de vooraankondiging is samengesteld."""
        return self._diameterLens.get_waarde()

    @diameterLens.setter
    def diameterLens(self, value):
        self._diameterLens.set_waarde(value, owner=self)
