# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTypeTrekker import KlTypeTrekker
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Trekker(TechnischDocument, AIMNaamObject, LijnGeometrie):
    """Een lineair mechanisch element, dubbelzijdig scharnierend, dat beoogd is om hoofdzakelijk op trek te belasten. Het verbindt, bijvoorbeeld, enerzijds het (bewegend) brugdeel/ beweegbare waterkerende constructie met anderzijds de lastzijde van de balansarm/bovenrolwagen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AsLagerCombinatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Balans', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hefportiek', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Heftoren', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rolwagenchassis', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bovenrolwagen', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._heeftVerendElement = OTLAttribuut(field=BooleanField,
                                                naam='heeftVerendElement',
                                                label='heeft verend element',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker.heeftVerendElement',
                                                definition='Geeft aan de trekker een verend element heeft of niet.',
                                                owner=self)

        self._type = OTLAttribuut(field=KlTypeTrekker,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trekker.type',
                                  definition='Het type van de trekker.',
                                  owner=self)

    @property
    def heeftVerendElement(self) -> bool:
        """Geeft aan de trekker een verend element heeft of niet."""
        return self._heeftVerendElement.get_waarde()

    @heeftVerendElement.setter
    def heeftVerendElement(self, value):
        self._heeftVerendElement.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Het type van de trekker."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
