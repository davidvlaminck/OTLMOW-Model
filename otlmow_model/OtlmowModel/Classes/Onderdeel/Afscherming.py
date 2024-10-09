# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlEcoAfschermingtype import KlEcoAfschermingtype
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afscherming(AIMObject, LijnGeometrie):
    """Schermen of wallen op de rand van het ecoduct die ervoor zorgen dat dieren op de brug niet afgeschrikt worden door de lichten van voorbijrijdende voertuigen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afscherming'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduct', direction='o')  # o = direction: outgoing

        self._type = OTLAttribuut(field=KlEcoAfschermingtype,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afscherming.type',
                                  definition='Het type van afscherming.',
                                  owner=self)

    @property
    def type(self) -> str:
        """Het type van afscherming."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
