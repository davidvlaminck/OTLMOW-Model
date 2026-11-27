# coding=utf-8
from datetime import date
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.DateField import DateField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Onderdeel.Cabine import Cabine
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlCabineLokaalKlasse import KlCabineLokaalKlasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class HSCabine(Cabine):
    """Een behuizing bestemd voor het beschermen van elektrisch hoogspanningsmateriaal en optioneel het daarbij horende laagspanningsmateriaal en elektromechanische technieken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Toegangselement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBHoogspanning', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSAankomstDNB', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSAankomstKlant', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSAutonomeVoeding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscelTransfo', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSVertrekDNB', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSVertrekKlant', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftKeuring', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ElektrischeKeuring', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WegverlichtingGroep', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._elektrischSchema = OTLAttribuut(field=DtcDocument,
                                              naam='elektrischSchema',
                                              label='elektrisch schema',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine.elektrischSchema',
                                              kardinaliteit_max='*',
                                              definition='Elektrisch aansluitschema van de HS cabine.',
                                              owner=self)

        self._heeftAfstandssturing = OTLAttribuut(field=BooleanField,
                                                  naam='heeftAfstandssturing',
                                                  label='heeft afstandssturing',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine.heeftAfstandssturing',
                                                  definition='Geeft aan of de HS-cabine aangesloten is op een extern afstandsbedieningssysteem (bv. van de netbeheerder zoals Fluvius), waarmee operationele schakelingen vanop afstand kunnen worden uitgevoerd.',
                                                  owner=self)

        self._isKopcabine = OTLAttribuut(field=BooleanField,
                                         naam='isKopcabine',
                                         label='is kopcabine',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine.isKopcabine',
                                         definition='Duidt aan of de HSCabine toegankelijk moet zijn de distributienetbeheerder.',
                                         owner=self)

        self._lokaalKlasse = OTLAttribuut(field=KlCabineLokaalKlasse,
                                          naam='lokaalKlasse',
                                          label='lokaal klasse',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine.lokaalKlasse',
                                          definition='Classificatie van de hoogspanningscabine als lokaal volgens Synergrid.',
                                          owner=self)

        self._vervaldatumVeiligheidshandschoenen = OTLAttribuut(field=DateField,
                                                                naam='vervaldatumVeiligheidshandschoenen',
                                                                label='vervaldatum veiligheidshandschoenen',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine.vervaldatumVeiligheidshandschoenen',
                                                                definition='De datum waarop de huidige veiligheidshandschoenen in de hoogspanningscabine vervallen.',
                                                                owner=self)

    @property
    def elektrischSchema(self) -> list[DtcDocumentWaarden]:
        """Elektrisch aansluitschema van de HS cabine."""
        return self._elektrischSchema.get_waarde()

    @elektrischSchema.setter
    def elektrischSchema(self, value):
        self._elektrischSchema.set_waarde(value, owner=self)

    @property
    def heeftAfstandssturing(self) -> bool:
        """Geeft aan of de HS-cabine aangesloten is op een extern afstandsbedieningssysteem (bv. van de netbeheerder zoals Fluvius), waarmee operationele schakelingen vanop afstand kunnen worden uitgevoerd."""
        return self._heeftAfstandssturing.get_waarde()

    @heeftAfstandssturing.setter
    def heeftAfstandssturing(self, value):
        self._heeftAfstandssturing.set_waarde(value, owner=self)

    @property
    def isKopcabine(self) -> bool:
        """Duidt aan of de HSCabine toegankelijk moet zijn de distributienetbeheerder."""
        return self._isKopcabine.get_waarde()

    @isKopcabine.setter
    def isKopcabine(self, value):
        self._isKopcabine.set_waarde(value, owner=self)

    @property
    def lokaalKlasse(self) -> str:
        """Classificatie van de hoogspanningscabine als lokaal volgens Synergrid."""
        return self._lokaalKlasse.get_waarde()

    @lokaalKlasse.setter
    def lokaalKlasse(self, value):
        self._lokaalKlasse.set_waarde(value, owner=self)

    @property
    def vervaldatumVeiligheidshandschoenen(self) -> date:
        """De datum waarop de huidige veiligheidshandschoenen in de hoogspanningscabine vervallen."""
        return self._vervaldatumVeiligheidshandschoenen.get_waarde()

    @vervaldatumVeiligheidshandschoenen.setter
    def vervaldatumVeiligheidshandschoenen(self, value):
        self._vervaldatumVeiligheidshandschoenen.set_waarde(value, owner=self)
