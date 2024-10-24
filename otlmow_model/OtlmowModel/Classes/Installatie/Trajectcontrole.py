# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlAlgRijrichting import KlAlgRijrichting
from ...Datatypes.KlAlgSnelheidsregime import KlAlgSnelheidsregime
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Trajectcontrole(NaampadObject, LijnGeometrie):
    """Trajectcontrole is een systeem waarbij de gemiddelde snelheid over een langere afstand wordt gemeten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trajectcontrole'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ANPRCamera', direction='i', deprecated='2.9.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', direction='i')  # i = direction: incoming

        self._attest = OTLAttribuut(field=DtcDocument,
                                    naam='attest',
                                    label='attest',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trajectcontrole.attest',
                                    usagenote='Bestanden van het type pdf.',
                                    definition='Het ijkingsattest van de trajectcontrole in zijn geheel.',
                                    owner=self)

        self._nTP = OTLAttribuut(field=BooleanField,
                                 naam='nTP',
                                 label='NTP',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trajectcontrole.nTP',
                                 definition='Aanduiding of het systeem voor zijn tijdsaanduiding gebruik maakt van NTP.',
                                 owner=self)

        self._rijrichting = OTLAttribuut(field=KlAlgRijrichting,
                                         naam='rijrichting',
                                         label='rijrichting',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trajectcontrole.rijrichting',
                                         definition='De rijrichting van de voertuigen die gecontroleerd worden.',
                                         owner=self)

        self._snelheidsregime = OTLAttribuut(field=KlAlgSnelheidsregime,
                                             naam='snelheidsregime',
                                             label='snelheidsregime',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trajectcontrole.snelheidsregime',
                                             definition='Het snelheidsregime waarop de voertuigen worden gecontroleerd.',
                                             owner=self)

    @property
    def attest(self) -> DtcDocumentWaarden:
        """Het ijkingsattest van de trajectcontrole in zijn geheel."""
        return self._attest.get_waarde()

    @attest.setter
    def attest(self, value):
        self._attest.set_waarde(value, owner=self)

    @property
    def nTP(self) -> bool:
        """Aanduiding of het systeem voor zijn tijdsaanduiding gebruik maakt van NTP."""
        return self._nTP.get_waarde()

    @nTP.setter
    def nTP(self, value):
        self._nTP.set_waarde(value, owner=self)

    @property
    def rijrichting(self) -> str:
        """De rijrichting van de voertuigen die gecontroleerd worden."""
        return self._rijrichting.get_waarde()

    @rijrichting.setter
    def rijrichting(self, value):
        self._rijrichting.set_waarde(value, owner=self)

    @property
    def snelheidsregime(self) -> str:
        """Het snelheidsregime waarop de voertuigen worden gecontroleerd."""
        return self._snelheidsregime.get_waarde()

    @snelheidsregime.setter
    def snelheidsregime(self, value):
        self._snelheidsregime.set_waarde(value, owner=self)
