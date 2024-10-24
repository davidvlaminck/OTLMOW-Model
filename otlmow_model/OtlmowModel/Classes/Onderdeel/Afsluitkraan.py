# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkendElement import LinkendElement
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlAfsluitkraanMerk import KlAfsluitkraanMerk
from ...Datatypes.KlAfsluitkraanModelnaam import KlAfsluitkraanModelnaam
from ...Datatypes.KlAfsluitkraanType import KlAfsluitkraanType
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afsluitkraan(LinkendElement, PuntGeometrie):
    """Een manueel bedienbare inrichting om de stroming van vloeistoffen of gassen doorheen een bepaalde opening tegen te houden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluitkraan'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluitkraan.diameter',
                                      definition='De diameter van de vrije doorgang.',
                                      owner=self)

        self._isContinuRegelbaar = OTLAttribuut(field=BooleanField,
                                                naam='isContinuRegelbaar',
                                                label='is continu regelbaar',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluitkraan.isContinuRegelbaar',
                                                definition='Geeft aan of de doorstroming vloeiend regelbaar is tussen de geheel gesloten stand (geen stroming) en de volledig geopende stand (maximale stroming).',
                                                owner=self)

        self._merk = OTLAttribuut(field=KlAfsluitkraanMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluitkraan.merk',
                                  definition='Het merk van de afsluitkraan.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlAfsluitkraanModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluitkraan.modelnaam',
                                       definition='De modelnaam van de afsluitkraan.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlAfsluitkraanType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluitkraan.type',
                                  definition='Geeft aan op welk werkingsprincipe de afsluitkraan steunt.',
                                  owner=self)

    @property
    def diameter(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van de vrije doorgang."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def isContinuRegelbaar(self) -> bool:
        """Geeft aan of de doorstroming vloeiend regelbaar is tussen de geheel gesloten stand (geen stroming) en de volledig geopende stand (maximale stroming)."""
        return self._isContinuRegelbaar.get_waarde()

    @isContinuRegelbaar.setter
    def isContinuRegelbaar(self, value):
        self._isContinuRegelbaar.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de afsluitkraan."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de afsluitkraan."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Geeft aan op welk werkingsprincipe de afsluitkraan steunt."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
