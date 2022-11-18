# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm, DtcAfmetingBxlxhInMmWaarden
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlSlagboomkolomMerk import KlSlagboomkolomMerk
from otlmow_model.Datatypes.KlSlagboomkolomModelnaam import KlSlagboomkolomModelnaam
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slagboomkolom(AIMObject, PuntGeometrie, VlakGeometrie):
    """De koker van een slagboominstallatie die de motor bevat en waaraan de slagboomarm bevestigd is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sokkel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom')

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom.afmetingen',
                                        definition='De afmetingen van de slagboomkolom.',
                                        owner=self)

        self._isPivoterend = OTLAttribuut(field=BooleanField,
                                          naam='isPivoterend',
                                          label='is pivoterend',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom.isPivoterend',
                                          definition='Attribuut waarmee kan aangegeven worden of de koker van de slagboominstallatie al dan niet pivoteert.',
                                          owner=self)

        self._merk = OTLAttribuut(field=KlSlagboomkolomMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom.merk',
                                  definition='Het merk van de slagboom installatie.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSlagboomkolomModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom.modelnaam',
                                       definition='Naam van het model van de slagboominstallatie.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom.technischeFiche',
                                             definition='Technische fiche van de slagboominstallatie.',
                                             owner=self)

    @property
    def afmetingen(self) -> DtcAfmetingBxlxhInMmWaarden:
        """De afmetingen van de slagboomkolom."""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)

    @property
    def isPivoterend(self) -> bool:
        """Attribuut waarmee kan aangegeven worden of de koker van de slagboominstallatie al dan niet pivoteert."""
        return self._isPivoterend.get_waarde()

    @isPivoterend.setter
    def isPivoterend(self, value):
        self._isPivoterend.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de slagboom installatie."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Naam van het model van de slagboominstallatie."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Technische fiche van de slagboominstallatie."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
