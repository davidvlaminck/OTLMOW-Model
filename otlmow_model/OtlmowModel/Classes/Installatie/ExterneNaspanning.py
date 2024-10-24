# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTypeExterneNaspanning import KlTypeExterneNaspanning
from ...Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton, KwantWrdInKiloNewtonWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ExterneNaspanning(AIMNaamObject, PuntGeometrie):
    """Nagespannen kabel of staaf die wordt geplaatst om de draagkracht van een structuur (bv. van een brug) te verhogen. Dit kan zowel in bestaande als in nieuwe structuren wordt toegepast."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ExterneNaspanning'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spankabel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanstaaf', direction='i')  # i = direction: incoming

        self._totaleNaspanning = OTLAttribuut(field=KwantWrdInKiloNewton,
                                              naam='totaleNaspanning',
                                              label='totale naspanning',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ExterneNaspanning.totaleNaspanning',
                                              definition='De totale naspanning, uitgedrukt in kiloNewton.',
                                              owner=self)

        self._type = OTLAttribuut(field=KlTypeExterneNaspanning,
                                  naam='type',
                                  label='type naspanning',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ExterneNaspanning.type',
                                  definition='Het type naspanning.',
                                  owner=self)

    @property
    def totaleNaspanning(self) -> KwantWrdInKiloNewtonWaarden:
        """De totale naspanning, uitgedrukt in kiloNewton."""
        return self._totaleNaspanning.get_waarde()

    @totaleNaspanning.setter
    def totaleNaspanning(self, value):
        self._totaleNaspanning.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type naspanning."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
