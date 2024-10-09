# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Buis import Buis
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlDraineerbuisMateriaal import KlDraineerbuisMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Draineerbuis(Buis):
    """Een buis voor het afvoeren van water uit de bodem over en door de grond,met als gevolg het verlagen van het grondwaterpeil."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerbuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i', deprecated='2.8.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

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
