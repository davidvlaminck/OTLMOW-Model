# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class EquipotentiaalVerbinding(AIMNaamObject, LijnGeometrie):
    """Een equipotentiaal verbinding, ook wel equipotentiaalgeleider genoemd, voorziet de galvanische verbinding van een metalen object, dat in normale toestand niet stroomvoerend is, met het aardingsstelsel. Deze verbinding mag als aardingsgeleider derhalve nooit verbroken worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EquipotentiaalVerbinding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie', direction='o')  # o = direction: outgoing

        self._isGeisoleerd = OTLAttribuut(field=BooleanField,
                                          naam='isGeisoleerd',
                                          label='is geïsoleerd',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EquipotentiaalVerbinding.isGeisoleerd',
                                          definition='Geeft expliciet aan of de aardingskabel al dan niet geïsoleerd is.',
                                          owner=self)

    @property
    def isGeisoleerd(self) -> bool:
        """Geeft expliciet aan of de aardingskabel al dan niet geïsoleerd is."""
        return self._isGeisoleerd.get_waarde()

    @isGeisoleerd.setter
    def isGeisoleerd(self, value):
        self._isGeisoleerd.set_waarde(value, owner=self)
