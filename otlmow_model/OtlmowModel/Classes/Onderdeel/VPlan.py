# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...BaseClasses.StringField import StringField
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VPlan(AIMNaamObject, GeenGeometrie):
    """Beschrijving van de werking en sturing van een verkeersregelinstallatie, waarin de fasering, conflicten, prioriteiten en schakellogica van de verkeerslichten eenduidig worden vastgelegd, zodat de regeling correct kan worden geïmplementeerd, geconfigureerd en beheerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VPlan'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftVPlan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ITSapp', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftVPlan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._plannummer = OTLAttribuut(field=StringField,
                                        naam='plannummer',
                                        label='vplan nummer',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VPlan.plannummer',
                                        definition='Nummer van het Vplan.',
                                        owner=self)

    @property
    def plannummer(self) -> str:
        """Nummer van het Vplan."""
        return self._plannummer.get_waarde()

    @plannummer.setter
    def plannummer(self, value):
        self._plannummer.set_waarde(value, owner=self)
