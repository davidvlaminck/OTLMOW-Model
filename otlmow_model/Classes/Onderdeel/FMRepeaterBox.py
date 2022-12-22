# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.IPNetwerkToegangObject import IPNetwerkToegangObject
from otlmow_model.Classes.Abstracten.RHZModule import RHZModule
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlFMRepeaterBoxMerk import KlFMRepeaterBoxMerk
from otlmow_model.Datatypes.KlFMRepeaterBoxModelnaam import KlFMRepeaterBoxModelnaam
from otlmow_model.BaseClasses.NonNegIntegerField import NonNegIntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class FMRepeaterBox(IPNetwerkToegangObject, RHZModule, SerienummerObject, AIMNaamObject):
    """Een radio-ontvanger en -zender, die het FM-signaal ontvangt en weer doorgeeft om zo grotere afstanden te overbruggen en plaatsen te bereiken, waar de radiosignalen niet geraken, zoals in tunnels. De uitvoering is van het type 'box' waar aparte repeatermodules per frequentie of voor meerdere frequenties kunnen ingestoken worden, zoals in een vaste computer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FMRepeaterBox'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        IPNetwerkToegangObject.__init__(self)
        RHZModule.__init__(self)
        SerienummerObject.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')

        self._aantalFMRepeaters = OTLAttribuut(field=NonNegIntegerField,
                                               naam='aantalFMRepeaters',
                                               label='aantal FM kaarten',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FMRepeaterBox.aantalFMRepeaters',
                                               definition='Aantal FM kaarten die geplaatst zijn in de repeater box.',
                                               owner=self)

        self._aantalInstelbareFrequenties = OTLAttribuut(field=NonNegIntegerField,
                                                         naam='aantalInstelbareFrequenties',
                                                         label='aantal instelbare FM frequenties',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FMRepeaterBox.aantalInstelbareFrequenties',
                                                         definition='Het maximaal aantal FM frequenties dat door middel van het plaatsen van kaarten in de repeater box ontvangen kan worden.',
                                                         owner=self)

        self._aantalModulators = OTLAttribuut(field=NonNegIntegerField,
                                              naam='aantalModulators',
                                              label='aantal modulators',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FMRepeaterBox.aantalModulators',
                                              definition='Aantal modulatorkaarten die geplaatst zijn in de repeater box.',
                                              owner=self)

        self._aantalSwitches = OTLAttribuut(field=NonNegIntegerField,
                                            naam='aantalSwitches',
                                            label='aantal switches',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FMRepeaterBox.aantalSwitches',
                                            definition='Aantal switchkaarten die geplaatst zijn in de repeater box.',
                                            owner=self)

        self._merk = OTLAttribuut(field=KlFMRepeaterBoxMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FMRepeaterBox.merk',
                                  definition='Merknaam van de FM repeater box.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlFMRepeaterBoxModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FMRepeaterBox.modelnaam',
                                       definition='Modelnaam van de FM repeater box.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FMRepeaterBox.technischeFiche',
                                             definition='De technische fiche van de FM repeater box.',
                                             owner=self)

    @property
    def aantalFMRepeaters(self) -> int:
        """Aantal FM kaarten die geplaatst zijn in de repeater box."""
        return self._aantalFMRepeaters.get_waarde()

    @aantalFMRepeaters.setter
    def aantalFMRepeaters(self, value):
        self._aantalFMRepeaters.set_waarde(value, owner=self)

    @property
    def aantalInstelbareFrequenties(self) -> int:
        """Het maximaal aantal FM frequenties dat door middel van het plaatsen van kaarten in de repeater box ontvangen kan worden."""
        return self._aantalInstelbareFrequenties.get_waarde()

    @aantalInstelbareFrequenties.setter
    def aantalInstelbareFrequenties(self, value):
        self._aantalInstelbareFrequenties.set_waarde(value, owner=self)

    @property
    def aantalModulators(self) -> int:
        """Aantal modulatorkaarten die geplaatst zijn in de repeater box."""
        return self._aantalModulators.get_waarde()

    @aantalModulators.setter
    def aantalModulators(self, value):
        self._aantalModulators.set_waarde(value, owner=self)

    @property
    def aantalSwitches(self) -> int:
        """Aantal switchkaarten die geplaatst zijn in de repeater box."""
        return self._aantalSwitches.get_waarde()

    @aantalSwitches.setter
    def aantalSwitches(self, value):
        self._aantalSwitches.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van de FM repeater box."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de FM repeater box."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de FM repeater box."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
