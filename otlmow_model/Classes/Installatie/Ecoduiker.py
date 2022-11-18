# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.Datatypes.KlEcoLooprichelType import KlEcoLooprichelType
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecoduiker(AIMObject, VlakGeometrie):
    """Buis- of tunnelvormige doorgang voor water onder een weg, die is voorzien van een oeverstrook of van looprichels zodat kleinere diersoorten beschermd voor het verkeer kunnen doorsteken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduiker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        VlakGeometrie.__init__(self)

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
