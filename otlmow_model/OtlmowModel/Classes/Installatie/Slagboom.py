# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Slagboom(NaampadObject, VlakGeometrie):
    """Een afsluitingsmechanisme met slagboomarmen dat dient om controle uit te kunnen oefenen over het gebruik van een doorgang of een toegang."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokerafsluiting', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#SlagboomGroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeOpslagplaats', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomarm', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slagboomkolom', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._isManueel = OTLAttribuut(field=BooleanField,
                                       naam='isManueel',
                                       label='is manueel',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom.isManueel',
                                       usagenote='Voor een manuele slagboom zijn geen instanties van de onderliggende onderdelen Slagboomkolom en Slagboomarm vereist.',
                                       definition='Geeft aan of de slagboom (uitsluitend) manueel bediend wordt of door een aangestuurde motor in de slagboomkolom.',
                                       owner=self)

    @property
    def isManueel(self) -> bool:
        """Geeft aan of de slagboom (uitsluitend) manueel bediend wordt of door een aangestuurde motor in de slagboomkolom."""
        return self._isManueel.get_waarde()

    @isManueel.setter
    def isManueel(self, value):
        self._isManueel.set_waarde(value, owner=self)
