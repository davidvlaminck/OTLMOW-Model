# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTypeHanger import KlTypeHanger
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hanger(AIMNaamObject, PuntGeometrie):
    """Een hanger is een secundair constructieonderdeel van een hangbrug dat, meestal met talrijke andere hangers, een brugdeel ophangt aan een overspannende hoofddrager/hoofdkabel. Een moderne hanger bestaat meestal uit staalkabel, maar deze kan ook uit profielstaal, platstaal of rondstaal vervaardigd zijn of zelfs uit schakels bestaan."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hanger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', direction='o')  # o = direction: outgoing

        self._type = OTLAttribuut(field=KlTypeHanger,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hanger.type',
                                  definition='Het type van de trekker.',
                                  owner=self)

    @property
    def type(self) -> str:
        """Het type van de trekker."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
