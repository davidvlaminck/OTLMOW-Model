# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TerreinDeel import TerreinDeel
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlWegbermBIO import KlWegbermBIO
from ...Datatypes.KlWegbermType import KlWegbermType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegberm(TerreinDeel, NaampadObject):
    """Gedeelte van het wegplatform dat buiten de rijbanen ligt. Een wegberm kan sloten en bijzonder ingerichte onderdelen bevatten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wegberm'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', 'u', '2.11.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', 'i', '2.11.0'),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', 'i', '2.11.0'),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._bijzonderIngerichteOnderdelen = OTLAttribuut(field=KlWegbermBIO,
                                                           naam='bijzonderIngerichteOnderdelen',
                                                           label='bijzonder ingerichte onderdelen van de wegberm',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wegberm.bijzonderIngerichteOnderdelen',
                                                           usagenote='Attribuut uit gebruik sinds versie 2.11.0 ',
                                                           deprecated_version='2.11.0',
                                                           definition='De bijzonder ingerichte onderdelen van de wegberm.',
                                                           owner=self)

        self._type = OTLAttribuut(field=KlWegbermType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wegberm.type',
                                  definition='Het type van wegberm.',
                                  owner=self)

    @property
    def bijzonderIngerichteOnderdelen(self) -> str:
        """De bijzonder ingerichte onderdelen van de wegberm."""
        return self._bijzonderIngerichteOnderdelen.get_waarde()

    @bijzonderIngerichteOnderdelen.setter
    def bijzonderIngerichteOnderdelen(self, value):
        self._bijzonderIngerichteOnderdelen.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Het type van wegberm."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
