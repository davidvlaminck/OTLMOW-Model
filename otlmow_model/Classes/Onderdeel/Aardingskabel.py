# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.KabelAarding import KabelAarding
from otlmow_model.Classes.Abstracten.KabelAardingSamenstelling import KabelAardingSamenstelling
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aardingskabel(KabelAarding, KabelAardingSamenstelling, AIMNaamObject):
    """Een aardingskabel is een geleidende verbinding, typisch uit koper, die ervoor zorgt dat een ongewenste elektrische stroom (foutstroom) op een installatie naar de aarde kan afgeleid worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingskabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie')

        self._isGeisoleerd = OTLAttribuut(field=BooleanField,
                                          naam='isGeisoleerd',
                                          label='is geïsoleerd',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingskabel.isGeisoleerd',
                                          definition='Geeft expliciet aan of de aardingskabel al dan niet geïsoleerd is.',
                                          owner=self)

    @property
    def isGeisoleerd(self) -> bool:
        """Geeft expliciet aan of de aardingskabel al dan niet geïsoleerd is."""
        return self._isGeisoleerd.get_waarde()

    @isGeisoleerd.setter
    def isGeisoleerd(self, value):
        self._isGeisoleerd.set_waarde(value, owner=self)
