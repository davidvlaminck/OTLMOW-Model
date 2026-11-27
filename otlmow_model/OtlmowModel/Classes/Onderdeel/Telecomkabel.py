# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Kabel import Kabel
from ...Datatypes.KlTelecomkabelAdersEnSectie import KlTelecomkabelAdersEnSectie
from ...Datatypes.KlTelecomkabelType import KlTelecomkabelType
from ...Datatypes.KlTelecomkabelTypeSpecificatie import KlTelecomkabelTypeSpecificatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Telecomkabel(Kabel):
    """Een aansluiting of reeks aansluitingen van een nutsvoorzieningennet voor het overbrengen van data van de ene locatie naar een andere."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Telecomkabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitsgroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VRIBuiteninstallatie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TTSegment', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._aantalAdersEnSectie = OTLAttribuut(field=KlTelecomkabelAdersEnSectie,
                                                 naam='aantalAdersEnSectie',
                                                 label='aantal aders en sectie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Telecomkabel.aantalAdersEnSectie',
                                                 definition='Aantal en sectie van de ader(s) van de kabel volgens een lijst van voorkomende types.',
                                                 owner=self)

        self._type = OTLAttribuut(field=KlTelecomkabelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Telecomkabel.type',
                                  definition='Indeling van een telecomkabel op basis van de gebruikte materialen volgens het Standaardbestek en de catalogusposten.',
                                  owner=self)

        self._typeSpecificatie = OTLAttribuut(field=KlTelecomkabelTypeSpecificatie,
                                              naam='typeSpecificatie',
                                              label='type specificatie',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Telecomkabel.typeSpecificatie',
                                              definition='Een verdere specificatie van het type van de telecomkabel volgens een vaste lijst om bv. de brandklasse mee te geven.',
                                              owner=self)

    @property
    def aantalAdersEnSectie(self) -> str:
        """Aantal en sectie van de ader(s) van de kabel volgens een lijst van voorkomende types."""
        return self._aantalAdersEnSectie.get_waarde()

    @aantalAdersEnSectie.setter
    def aantalAdersEnSectie(self, value):
        self._aantalAdersEnSectie.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Indeling van een telecomkabel op basis van de gebruikte materialen volgens het Standaardbestek en de catalogusposten."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)

    @property
    def typeSpecificatie(self) -> str:
        """Een verdere specificatie van het type van de telecomkabel volgens een vaste lijst om bv. de brandklasse mee te geven."""
        return self._typeSpecificatie.get_waarde()

    @typeSpecificatie.setter
    def typeSpecificatie(self, value):
        self._typeSpecificatie.set_waarde(value, owner=self)
