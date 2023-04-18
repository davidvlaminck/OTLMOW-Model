# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.SelNietSelLus import SelNietSelLus
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlSelLusSoort import KlSelLusSoort
from otlmow_model.Datatypes.KlSelLusVerbinding import KlSelLusVerbinding


# Generated with OTLClassCreator. To modify: extend, do not edit
class SelectieveDetectielus(SelNietSelLus):
    """De selectieve detectielussen moeten bepaalde voertuigen toelaten het kruispunt prioritair te dwarsen. Daarvoor zijn die prioritaire voertuigen uitgerust met een zendtoestel dat gecodeerd informatie doorstuurt naar een datalus in het wegdek. Deze lus is verbonden met een demodulator die de informatie decodeert en doorstuurt naar de verkeersregelaar van het te dwarsen kruispunt"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar')

        self._heeftMeerdereKruisingen = OTLAttribuut(field=BooleanField,
                                                     naam='heeftMeerdereKruisingen',
                                                     label='heeft meerdere kruisingen',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus.heeftMeerdereKruisingen',
                                                     definition='Aanduiding of de lus voor meerdere kruispunten wordt gebruikt.',
                                                     owner=self)

        self._soortLus = OTLAttribuut(field=KlSelLusSoort,
                                      naam='soortLus',
                                      label='soort lus',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus.soortLus',
                                      kardinaliteit_max='*',
                                      definition='Type detectielus vb bus, tram,...',
                                      owner=self)

        self._verbinding = OTLAttribuut(field=KlSelLusVerbinding,
                                        naam='verbinding',
                                        label='verbinding',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus.verbinding',
                                        definition='Soort verbinding (serieel of contact).',
                                        owner=self)

    @property
    def heeftMeerdereKruisingen(self) -> bool:
        """Aanduiding of de lus voor meerdere kruispunten wordt gebruikt."""
        return self._heeftMeerdereKruisingen.get_waarde()

    @heeftMeerdereKruisingen.setter
    def heeftMeerdereKruisingen(self, value):
        self._heeftMeerdereKruisingen.set_waarde(value, owner=self)

    @property
    def soortLus(self) -> List[str]:
        """Type detectielus vb bus, tram,..."""
        return self._soortLus.get_waarde()

    @soortLus.setter
    def soortLus(self, value):
        self._soortLus.set_waarde(value, owner=self)

    @property
    def verbinding(self) -> str:
        """Soort verbinding (serieel of contact)."""
        return self._verbinding.get_waarde()

    @verbinding.setter
    def verbinding(self, value):
        self._verbinding.set_waarde(value, owner=self)
