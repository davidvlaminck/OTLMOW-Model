# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Kabel import Kabel
from ...Datatypes.KlSignaalkabelAdersEnSectie import KlSignaalkabelAdersEnSectie
from ...Datatypes.KlSignaalkabelType import KlSignaalkabelType
from ...Datatypes.KlSignaalkabelTypeSpecificatie import KlSignaalkabelTypeSpecificatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Signaalkabel(Kabel):
    """Kabel die primair zorgt voor het uitwisselen van digitale en analoge stuursignalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalkabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitspaal', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aswegersite', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitsgroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VRIBuiteninstallatie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VerlichteOversteekplaatsGroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Codeklavier', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordOpMaat', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TTSegment', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._aantalAdersEnSectie = OTLAttribuut(field=KlSignaalkabelAdersEnSectie,
                                                 naam='aantalAdersEnSectie',
                                                 label='aders specificatie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalkabel.aantalAdersEnSectie',
                                                 definition='Aantal en sectie van de ader(s) in de signalisatiekabel.',
                                                 owner=self)

        self._type = OTLAttribuut(field=KlSignaalkabelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalkabel.type',
                                  definition='Geeft aan wat voor stuurkabel gebruikt wordt.',
                                  owner=self)

        self._typeSpecificatie = OTLAttribuut(field=KlSignaalkabelTypeSpecificatie,
                                              naam='typeSpecificatie',
                                              label='type specificatie',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalkabel.typeSpecificatie',
                                              definition='Een verdere specificatie van het type van de signalisatiekabel volgens een vaste lijst om bv. de brandklasse mee te geven.',
                                              owner=self)

    @property
    def aantalAdersEnSectie(self) -> str:
        """Aantal en sectie van de ader(s) in de signalisatiekabel."""
        return self._aantalAdersEnSectie.get_waarde()

    @aantalAdersEnSectie.setter
    def aantalAdersEnSectie(self, value):
        self._aantalAdersEnSectie.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Geeft aan wat voor stuurkabel gebruikt wordt."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)

    @property
    def typeSpecificatie(self) -> str:
        """Een verdere specificatie van het type van de signalisatiekabel volgens een vaste lijst om bv. de brandklasse mee te geven."""
        return self._typeSpecificatie.get_waarde()

    @typeSpecificatie.setter
    def typeSpecificatie(self, value):
        self._typeSpecificatie.set_waarde(value, owner=self)
