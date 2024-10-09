# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlEcoLooprichelType import KlEcoLooprichelType
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecoduiker(AIMObject, LijnGeometrie, VlakGeometrie):
    """Buis- of tunnelvormige doorgang voor water onder een weg, die is voorzien van een oeverstrook of van looprichels zodat kleinere diersoorten beschermd voor het verkeer kunnen doorsteken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduiker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._typeLooprichel = OTLAttribuut(field=KlEcoLooprichelType,
                                            naam='typeLooprichel',
                                            label='type looprichel',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduiker.typeLooprichel',
                                            definition='Type van looprichel in de ecoduiker.',
                                            owner=self)

    @property
    def typeLooprichel(self) -> str:
        """Type van looprichel in de ecoduiker."""
        return self._typeLooprichel.get_waarde()

    @typeLooprichel.setter
    def typeLooprichel(self, value):
        self._typeLooprichel.set_waarde(value, owner=self)
