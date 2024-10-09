# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.DtcAfmetingBxlxhInCm import DtcAfmetingBxlxhInCm, DtcAfmetingBxlxhInCmWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerankeringsplaatMicropaal(AIMObject, PuntGeometrie):
    """Een stalen plaat gemonteerd op de micropaal, die aangespannen wordt en dient ter verankering van de micropaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerankeringsplaatMicropaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Micropaal', direction='u')  # u = unidirectional

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxlxhInCm,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerankeringsplaatMicropaal.afmetingen',
                                        definition='Afmetingen van de verankeringsplaat voor de breedte, lengte en hoogte, in centimeter.',
                                        owner=self)

    @property
    def afmetingen(self) -> DtcAfmetingBxlxhInCmWaarden:
        """Afmetingen van de verankeringsplaat voor de breedte, lengte en hoogte, in centimeter."""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)
