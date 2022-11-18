# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Buis import Buis
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlDraineerbuisMateriaal import KlDraineerbuisMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Draineerbuis(Buis):
    """Een buis voor het afvoeren van water uit de bodem over en door de grond,met als gevolg het verlagen van het grondwaterpeil."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._heeftDrainbrug = OTLAttribuut(field=BooleanField,
                                            naam='heeftDrainbrug',
                                            label='heeft drainbrug',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis.heeftDrainbrug',
                                            definition='Aanduiding of er al dan niet een profiel onderaan de draineerbuis aanwezig is om zettingen te vermijden.',
                                            owner=self)

        self._materiaal = OTLAttribuut(field=KlDraineerbuisMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis.materiaal',
                                       definition='Bepaalt het materiaal van de draineerbuis.',
                                       owner=self)

    @property
    def heeftDrainbrug(self) -> bool:
        """Aanduiding of er al dan niet een profiel onderaan de draineerbuis aanwezig is om zettingen te vermijden."""
        return self._heeftDrainbrug.get_waarde()

    @heeftDrainbrug.setter
    def heeftDrainbrug(self, value):
        self._heeftDrainbrug.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Bepaalt het materiaal van de draineerbuis."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
