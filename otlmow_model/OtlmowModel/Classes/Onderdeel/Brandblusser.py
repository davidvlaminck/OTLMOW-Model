# coding=utf-8
from datetime import date
from typing import ClassVar

from ...BaseClasses.DateField import DateField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlBrandblusserBlusmiddel import KlBrandblusserBlusmiddel
from ...Datatypes.KlBrandblusserGewicht import KlBrandblusserGewicht
from ...Datatypes.KlBrandblusserType import KlBrandblusserType
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brandblusser(NaampadObject, PuntGeometrie):
    """Een apparaat om het vuur van een kleine brand mee te doven. Het bestaat uit een cilinder waarin een beperkte hoeveelheid blusmiddel onder druk staat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Lokaal', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactpunt', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BrandblusserGroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtganginrichting', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._aankoopdatum = OTLAttribuut(field=DateField,
                                          naam='aankoopdatum',
                                          label='aankoopdatum',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.aankoopdatum',
                                          definition='Datum wordt het toestel is aangekocht.',
                                          owner=self)

        self._blusmiddel = OTLAttribuut(field=KlBrandblusserBlusmiddel,
                                        naam='blusmiddel',
                                        label='blusmiddel',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.blusmiddel',
                                        definition='Substantie waarmee het toestel gevuld is in functie van het blussen van vuur.',
                                        owner=self)

        self._gewicht = OTLAttribuut(field=KlBrandblusserGewicht,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.gewicht',
                                     definition='Totaal gewicht van het gevulde toestel.',
                                     owner=self)

        self._keuringsdatum = OTLAttribuut(field=DateField,
                                           naam='keuringsdatum',
                                           label='keuringsdatum',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.keuringsdatum',
                                           definition='Datum waarop het toestel laatst is gekeurd.',
                                           owner=self)

        self._type = OTLAttribuut(field=KlBrandblusserType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.type',
                                  definition='Het type van de brandblusser.',
                                  owner=self)

    @property
    def aankoopdatum(self) -> date:
        """Datum wordt het toestel is aangekocht."""
        return self._aankoopdatum.get_waarde()

    @aankoopdatum.setter
    def aankoopdatum(self, value):
        self._aankoopdatum.set_waarde(value, owner=self)

    @property
    def blusmiddel(self) -> str:
        """Substantie waarmee het toestel gevuld is in functie van het blussen van vuur."""
        return self._blusmiddel.get_waarde()

    @blusmiddel.setter
    def blusmiddel(self, value):
        self._blusmiddel.set_waarde(value, owner=self)

    @property
    def gewicht(self) -> str:
        """Totaal gewicht van het gevulde toestel."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def keuringsdatum(self) -> date:
        """Datum waarop het toestel laatst is gekeurd."""
        return self._keuringsdatum.get_waarde()

    @keuringsdatum.setter
    def keuringsdatum(self, value):
        self._keuringsdatum.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Het type van de brandblusser."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
