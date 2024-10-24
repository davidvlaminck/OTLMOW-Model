# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bodembescherming(AIMNaamObject, VlakGeometrie):
    """Een constructieve maatregel om de onderwaterbodem te beschermen tegen erosie en andere vormen van schade."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bodembescherming'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Fuik', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolkvloer', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Asfaltmat', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Betonmat', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Betonmatras', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wiepenmat', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen', direction='i')  # i = direction: incoming

        self._dikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bodembescherming.dikte',
                                   definition='De dikte van de bodembescherming uitgedrukt in cm',
                                   owner=self)

        self._heeftVoegen = OTLAttribuut(field=BooleanField,
                                         naam='heeftVoegen',
                                         label='heeft voegen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bodembescherming.heeftVoegen',
                                         definition='Geeft aan of de bodembescherming al dan niet voegen heeft',
                                         owner=self)

        self._isWaterdoorlatend = OTLAttribuut(field=BooleanField,
                                               naam='isWaterdoorlatend',
                                               label='is waterdoorlatend',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bodembescherming.isWaterdoorlatend',
                                               definition='Geeft aan of de bodembescherming al dan niet waterdoorlatend is.',
                                               owner=self)

    @property
    def dikte(self) -> KwantWrdInCentimeterWaarden:
        """De dikte van de bodembescherming uitgedrukt in cm"""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def heeftVoegen(self) -> bool:
        """Geeft aan of de bodembescherming al dan niet voegen heeft"""
        return self._heeftVoegen.get_waarde()

    @heeftVoegen.setter
    def heeftVoegen(self, value):
        self._heeftVoegen.set_waarde(value, owner=self)

    @property
    def isWaterdoorlatend(self) -> bool:
        """Geeft aan of de bodembescherming al dan niet waterdoorlatend is."""
        return self._isWaterdoorlatend.get_waarde()

    @isWaterdoorlatend.setter
    def isWaterdoorlatend(self, value):
        self._isWaterdoorlatend.set_waarde(value, owner=self)
