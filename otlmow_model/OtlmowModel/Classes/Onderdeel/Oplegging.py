# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlBewegingsvrijheidInVlakBijOplegging import (
    KlBewegingsvrijheidInVlakBijOplegging,
)
from ...Datatypes.KlOverigeFunctiesOplegging import KlOverigeFunctiesOplegging
from ...Datatypes.KlTypeOplegging import KlTypeOplegging
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Oplegging(AIMNaamObject, PuntGeometrie):
    """Een oplegging of steunpunt is een element dat is vastgemaakt aan de vaste ondergrond (vb. aan het landhoofd) of aan een ander constructiedeel. Een oplegging beperkt hier de beweging van het bewegend lichaam (vb. van de brugklap). Een oplegging kan ook een dempend effect hebben bij het sluiten van een bewegend lichaam."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AsLagerCombinatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rolwagenchassis', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelveerhuis', 'o', '2.21.0'),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegmechanisme', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegrij', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugligger', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DraagstructuurBWCTWC', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderlandhoofd', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._bewegingsvrijheidInHetVlak = OTLAttribuut(field=KlBewegingsvrijheidInVlakBijOplegging,
                                                        naam='bewegingsvrijheidInHetVlak',
                                                        label='bewegingsvrijheid in het vlak',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging.bewegingsvrijheidInHetVlak',
                                                        kardinaliteit_max='*',
                                                        definition='De bewegingsvrijheid in het vlak. Er kunnen meerdere mogelijkheden zijn.',
                                                        owner=self)

        self._overigeFuncties = OTLAttribuut(field=KlOverigeFunctiesOplegging,
                                             naam='overigeFuncties',
                                             label='overige functies',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging.overigeFuncties',
                                             kardinaliteit_max='3',
                                             definition='De overige functies van de oplegging.',
                                             owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging.technischeFiche',
                                             definition='Verwijzing naar de technische fiche met de productspecifieke eigenschappen en technische specificaties van de oplegging.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlTypeOplegging,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging.type',
                                  definition='De soort oplegging.',
                                  owner=self)

        self._zijnNegatieveSteunpuntreactiesAanwezig = OTLAttribuut(field=BooleanField,
                                                                    naam='zijnNegatieveSteunpuntreactiesAanwezig',
                                                                    label='zijn negatieve steunpuntreacties aanwezig',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging.zijnNegatieveSteunpuntreactiesAanwezig',
                                                                    definition='Geeft aan of er negatieve steunpuntreacties aanwezig zijn, al dan niet.',
                                                                    owner=self)

    @property
    def bewegingsvrijheidInHetVlak(self) -> list[str]:
        """De bewegingsvrijheid in het vlak. Er kunnen meerdere mogelijkheden zijn."""
        return self._bewegingsvrijheidInHetVlak.get_waarde()

    @bewegingsvrijheidInHetVlak.setter
    def bewegingsvrijheidInHetVlak(self, value):
        self._bewegingsvrijheidInHetVlak.set_waarde(value, owner=self)

    @property
    def overigeFuncties(self) -> list[str]:
        """De overige functies van de oplegging."""
        return self._overigeFuncties.get_waarde()

    @overigeFuncties.setter
    def overigeFuncties(self, value):
        self._overigeFuncties.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Verwijzing naar de technische fiche met de productspecifieke eigenschappen en technische specificaties van de oplegging."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """De soort oplegging."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)

    @property
    def zijnNegatieveSteunpuntreactiesAanwezig(self) -> bool:
        """Geeft aan of er negatieve steunpuntreacties aanwezig zijn, al dan niet."""
        return self._zijnNegatieveSteunpuntreactiesAanwezig.get_waarde()

    @zijnNegatieveSteunpuntreactiesAanwezig.setter
    def zijnNegatieveSteunpuntreactiesAanwezig(self, value):
        self._zijnNegatieveSteunpuntreactiesAanwezig.set_waarde(value, owner=self)
