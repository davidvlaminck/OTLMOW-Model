# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlCADOMerk import KlCADOMerk
from ...Datatypes.KlCADOModelnaam import KlCADOModelnaam
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Calamiteitendoorsteek(NaampadObject, LijnGeometrie):
    """Een calamiteitendoorsteek,afgekort CADO,is een mechanische constructie voor het opklappen van een deel van de vangrail in de middenberm van een weg. Het primaire doel van de calamiteitendoorsteek is het doorlaten van hulpverleningsvoertuigen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityCable', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#CalamiteitendoorsteekGroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._isDubbelArmig = OTLAttribuut(field=BooleanField,
                                           naam='isDubbelArmig',
                                           label='is dubbelarmig',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.isDubbelArmig',
                                           definition='Aanduiding of de calamiteitendoorsteek dubbel armig is.',
                                           owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.lengte',
                                    definition='De totale lengte van de calamiteitendoorsteek constructie.',
                                    owner=self)

        self._merk = OTLAttribuut(field=KlCADOMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.merk',
                                  definition='Het merk van de calamiteitendoorsteek.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlCADOModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.modelnaam',
                                       definition='De modelnaam van de calamiteitendoorsteek.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.technischeFiche',
                                             definition='De technische fiche van de calamiteitendoorsteek.',
                                             owner=self)

    @property
    def isDubbelArmig(self) -> bool:
        """Aanduiding of de calamiteitendoorsteek dubbel armig is."""
        return self._isDubbelArmig.get_waarde()

    @isDubbelArmig.setter
    def isDubbelArmig(self, value):
        self._isDubbelArmig.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De totale lengte van de calamiteitendoorsteek constructie."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de calamiteitendoorsteek."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de calamiteitendoorsteek."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de calamiteitendoorsteek."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
