# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from ...Classes.Abstracten.FirmwareObject import FirmwareObject
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlAansluitingskabel import KlAansluitingskabel
from ...Datatypes.KlBadgelezerMerk import KlBadgelezerMerk
from ...Datatypes.KlBadgelezerModelnaam import KlBadgelezerModelnaam
from ...Datatypes.KlBadgelezerProtocol import KlBadgelezerProtocol
from ...Datatypes.KlEncryptieType import KlEncryptieType
from otlmow_model.OtlmowModel.BaseClasses.NonNegIntegerField import NonNegIntegerField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Badgelezer(ElektrischComponentennummerObject, FirmwareObject, SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een inrichting voor automatische authenticatie op basis van een badge."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ZuilTGC', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zoutbijlaadplaats', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller', direction='u')  # u = unidirectional

        self._aansluitingskabel = OTLAttribuut(field=KlAansluitingskabel,
                                               naam='aansluitingskabel',
                                               label='aansluitingskabel',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer.aansluitingskabel',
                                               definition='Geeft aan of er een kabel / welk type kabel er gebruikt wordt om communicatie van en naar dit element mogelijk te maken.',
                                               owner=self)

        self._aantalDraden = OTLAttribuut(field=NonNegIntegerField,
                                          naam='aantalDraden',
                                          label='aantal draden',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer.aantalDraden',
                                          definition='Het aantal aders die door de kabel lopen.',
                                          owner=self)

        self._configuratiebestand = OTLAttribuut(field=DtcDocument,
                                                 naam='configuratiebestand',
                                                 label='configuratiebestand',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer.configuratiebestand',
                                                 usagenote='Attribuut uit gebruik sinds versie 2.8.0 ',
                                                 deprecated_version='2.8.0',
                                                 definition='Bestand dat de configuratie gegevens van de badgelezer bijhoudt.',
                                                 owner=self)

        self._encryptieType = OTLAttribuut(field=KlEncryptieType,
                                           naam='encryptieType',
                                           label='encryptie type',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer.encryptieType',
                                           definition='De type encryptie die de veiligheid van het dataverkeer tussen de badge en de badgelezer verzekert.',
                                           owner=self)

        self._heeftCodeklavier = OTLAttribuut(field=BooleanField,
                                              naam='heeftCodeklavier',
                                              label='heeft codeklavier',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer.heeftCodeklavier',
                                              definition='Geeft aan of de badgelezer een geïntegreerd codeklavier heeft.',
                                              owner=self)

        self._heeftExtraVandalismebescherming = OTLAttribuut(field=BooleanField,
                                                             naam='heeftExtraVandalismebescherming',
                                                             label='heeft extra vandalismebescherming',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer.heeftExtraVandalismebescherming',
                                                             definition='Geeft aan of de badgelezer voorzien is van additionele vandalismebescherming.',
                                                             owner=self)

        self._heeftQRCodelezer = OTLAttribuut(field=BooleanField,
                                              naam='heeftQRCodelezer',
                                              label='heeft QR codelezer',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer.heeftQRCodelezer',
                                              definition='Geeft aan of de badgelezer een inrichting heeft om QR codes te lezen die integraal deel uitmaakt van de badgelzer zelf.',
                                              owner=self)

        self._isBuiten = OTLAttribuut(field=BooleanField,
                                      naam='isBuiten',
                                      label='is buiten',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer.isBuiten',
                                      definition='Geeft aan of de badgelezer zich binnen of buiten bevindt.',
                                      owner=self)

        self._merk = OTLAttribuut(field=KlBadgelezerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer.merk',
                                  definition='Het merk van de badgelezer.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlBadgelezerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer.modelnaam',
                                       definition='De modelnaam van de badgelezer.',
                                       owner=self)

        self._protocol = OTLAttribuut(field=KlBadgelezerProtocol,
                                      naam='protocol',
                                      label='protocol',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer.protocol',
                                      definition='Het protocol gebruikt door de badgelezer om gegevens mee te sturen en ontvangen.',
                                      owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer.technischeFiche',
                                             definition='De technische fiche van een badgelezer.',
                                             owner=self)

    @property
    def aansluitingskabel(self) -> str:
        """Geeft aan of er een kabel / welk type kabel er gebruikt wordt om communicatie van en naar dit element mogelijk te maken."""
        return self._aansluitingskabel.get_waarde()

    @aansluitingskabel.setter
    def aansluitingskabel(self, value):
        self._aansluitingskabel.set_waarde(value, owner=self)

    @property
    def aantalDraden(self) -> int:
        """Het aantal aders die door de kabel lopen."""
        return self._aantalDraden.get_waarde()

    @aantalDraden.setter
    def aantalDraden(self, value):
        self._aantalDraden.set_waarde(value, owner=self)

    @property
    def configuratiebestand(self) -> DtcDocumentWaarden:
        """Bestand dat de configuratie gegevens van de badgelezer bijhoudt."""
        return self._configuratiebestand.get_waarde()

    @configuratiebestand.setter
    def configuratiebestand(self, value):
        self._configuratiebestand.set_waarde(value, owner=self)

    @property
    def encryptieType(self) -> str:
        """De type encryptie die de veiligheid van het dataverkeer tussen de badge en de badgelezer verzekert."""
        return self._encryptieType.get_waarde()

    @encryptieType.setter
    def encryptieType(self, value):
        self._encryptieType.set_waarde(value, owner=self)

    @property
    def heeftCodeklavier(self) -> bool:
        """Geeft aan of de badgelezer een geïntegreerd codeklavier heeft."""
        return self._heeftCodeklavier.get_waarde()

    @heeftCodeklavier.setter
    def heeftCodeklavier(self, value):
        self._heeftCodeklavier.set_waarde(value, owner=self)

    @property
    def heeftExtraVandalismebescherming(self) -> bool:
        """Geeft aan of de badgelezer voorzien is van additionele vandalismebescherming."""
        return self._heeftExtraVandalismebescherming.get_waarde()

    @heeftExtraVandalismebescherming.setter
    def heeftExtraVandalismebescherming(self, value):
        self._heeftExtraVandalismebescherming.set_waarde(value, owner=self)

    @property
    def heeftQRCodelezer(self) -> bool:
        """Geeft aan of de badgelezer een inrichting heeft om QR codes te lezen die integraal deel uitmaakt van de badgelzer zelf."""
        return self._heeftQRCodelezer.get_waarde()

    @heeftQRCodelezer.setter
    def heeftQRCodelezer(self, value):
        self._heeftQRCodelezer.set_waarde(value, owner=self)

    @property
    def isBuiten(self) -> bool:
        """Geeft aan of de badgelezer zich binnen of buiten bevindt."""
        return self._isBuiten.get_waarde()

    @isBuiten.setter
    def isBuiten(self, value):
        self._isBuiten.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de badgelezer."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de badgelezer."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def protocol(self) -> str:
        """Het protocol gebruikt door de badgelezer om gegevens mee te sturen en ontvangen."""
        return self._protocol.get_waarde()

    @protocol.setter
    def protocol(self, value):
        self._protocol.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van een badgelezer."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
