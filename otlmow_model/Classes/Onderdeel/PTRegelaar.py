# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlPTRegelaarMerk import KlPTRegelaarMerk
from otlmow_model.Datatypes.KlPTRegelaarModelnaam import KlPTRegelaarModelnaam
from otlmow_model.Datatypes.KlPtRegelaarCommunicatiewijze import KlPtRegelaarCommunicatiewijze
from otlmow_model.Datatypes.KlPtRegelaarProtocol import KlPtRegelaarProtocol
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTRegelaar(AIMNaamObject, PuntGeometrie):
    """Deze PT-module staat in voor het ontvangen en bewerken van telegrammen van voertuigen van het openbaar vervoer (bussen, trams)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTRegelaarModule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar')

        self._communicatiewijze = OTLAttribuut(field=KlPtRegelaarCommunicatiewijze,
                                               naam='communicatiewijze',
                                               label='communicatiewijze',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.communicatiewijze',
                                               definition='De manier waarop de PT-regelaar communiceert met de verkeersregelaar.',
                                               owner=self)

        self._lijnnummers = OTLAttribuut(field=DtcDocument,
                                         naam='lijnnummers',
                                         label='lijnnummers',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.lijnnummers',
                                         kardinaliteit_max='*',
                                         definition='Nummers van de PT lijnen die connecteren met de PT regelaar.',
                                         owner=self)

        self._merk = OTLAttribuut(field=KlPTRegelaarMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.merk',
                                  definition='Het merk van een PT regelaar.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlPTRegelaarModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.modelnaam',
                                       definition='De modelnaam/product range van een PT regelaar.',
                                       owner=self)

        self._protocol = OTLAttribuut(field=KlPtRegelaarProtocol,
                                      naam='protocol',
                                      label='protocol',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.protocol',
                                      definition='Naam van het protocol waarmee gecommuniceerd wordt tussen PT-regelaar en verkeersregelaar.',
                                      owner=self)

        self._voertuignummers = OTLAttribuut(field=StringField,
                                             naam='voertuignummers',
                                             label='voertuignummers',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.voertuignummers',
                                             kardinaliteit_max='*',
                                             definition='Nummers van de voertuigen die connecteren met de PT regelaar.',
                                             owner=self)

    @property
    def communicatiewijze(self) -> str:
        """De manier waarop de PT-regelaar communiceert met de verkeersregelaar."""
        return self._communicatiewijze.get_waarde()

    @communicatiewijze.setter
    def communicatiewijze(self, value):
        self._communicatiewijze.set_waarde(value, owner=self)

    @property
    def lijnnummers(self) -> List[DtcDocumentWaarden]:
        """Nummers van de PT lijnen die connecteren met de PT regelaar."""
        return self._lijnnummers.get_waarde()

    @lijnnummers.setter
    def lijnnummers(self, value):
        self._lijnnummers.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van een PT regelaar."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam/product range van een PT regelaar."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def protocol(self) -> str:
        """Naam van het protocol waarmee gecommuniceerd wordt tussen PT-regelaar en verkeersregelaar."""
        return self._protocol.get_waarde()

    @protocol.setter
    def protocol(self, value):
        self._protocol.set_waarde(value, owner=self)

    @property
    def voertuignummers(self) -> List[str]:
        """Nummers van de voertuigen die connecteren met de PT regelaar."""
        return self._voertuignummers.get_waarde()

    @voertuignummers.setter
    def voertuignummers(self, value):
        self._voertuignummers.set_waarde(value, owner=self)
