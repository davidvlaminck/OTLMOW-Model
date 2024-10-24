# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcFrequentierange import DtcFrequentierange, DtcFrequentierangeWaarden
from ...Datatypes.KlZendontvangerMerk import KlZendontvangerMerk
from ...Datatypes.KlZendontvangerModelnaam import KlZendontvangerModelnaam
from ...Datatypes.KwantWrdInWatt import KwantWrdInWatt, KwantWrdInWattWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zendontvanger(AIMNaamObject, PuntGeometrie):
    """Een zendontvanger of transceiver is een elektronisch toestel dat radiogolven kan uitzenden en ontvangen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendontvanger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendmast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel', direction='u')  # u = unidirectional

        self._frequentierange = OTLAttribuut(field=DtcFrequentierange,
                                             naam='frequentierange',
                                             label='frequentierange',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendontvanger.frequentierange',
                                             definition='De frequentierange van de zendontvanger.',
                                             owner=self)

        self._merk = OTLAttribuut(field=KlZendontvangerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendontvanger.merk',
                                  definition='Het merk van de zendontvanger.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlZendontvangerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendontvanger.modelnaam',
                                       definition='De modelnaam van de zendontvanger.',
                                       owner=self)

        self._zendvermogen = OTLAttribuut(field=KwantWrdInWatt,
                                          naam='zendvermogen',
                                          label='zendvermogen',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendontvanger.zendvermogen',
                                          definition='Het zendvermogen van de zendontvanger.',
                                          owner=self)

    @property
    def frequentierange(self) -> DtcFrequentierangeWaarden:
        """De frequentierange van de zendontvanger."""
        return self._frequentierange.get_waarde()

    @frequentierange.setter
    def frequentierange(self, value):
        self._frequentierange.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de zendontvanger."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de zendontvanger."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def zendvermogen(self) -> KwantWrdInWattWaarden:
        """Het zendvermogen van de zendontvanger."""
        return self._zendvermogen.get_waarde()

    @zendvermogen.setter
    def zendvermogen(self, value):
        self._zendvermogen.set_waarde(value, owner=self)
