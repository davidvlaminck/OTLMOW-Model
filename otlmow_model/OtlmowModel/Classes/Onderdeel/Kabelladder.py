# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Kabelgeleiding import Kabelgeleiding
from ...Datatypes.KwantWrdInKilogramPerMeter import KwantWrdInKilogramPerMeter, KwantWrdInKilogramPerMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelladder(Kabelgeleiding):
    """Een inrichting die ervoor zorgt dat een kabel beschermd is tegen beschadiging en/of op een gecontroleerde plaats blijft hangen of liggen. De kabelladder is een gerasterde constructie die doet denken aan een ladder, die toelaat om de kabels langs alle kanten te zien. Slechts langs één kant is de toegang tot de kabels fysiek onbelet."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelladder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabelgeleiding', direction='i')  # i = direction: incoming

        self._draagvermogen = OTLAttribuut(field=KwantWrdInKilogramPerMeter,
                                           naam='draagvermogen',
                                           label='draagvermogen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelladder.draagvermogen',
                                           definition='Het draagvermogen per meter om kabels te ondersteunen.',
                                           owner=self)

    @property
    def draagvermogen(self) -> KwantWrdInKilogramPerMeterWaarden:
        """Het draagvermogen per meter om kabels te ondersteunen."""
        return self._draagvermogen.get_waarde()

    @draagvermogen.setter
    def draagvermogen(self, value):
        self._draagvermogen.set_waarde(value, owner=self)
