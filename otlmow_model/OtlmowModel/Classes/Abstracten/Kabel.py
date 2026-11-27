# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlKabelFabrikant import KlKabelFabrikant
from ...Datatypes.KlKabelLeidingBescherming import KlKabelLeidingBescherming
from ...Datatypes.KlKabelmantelKleur import KlKabelmantelKleur
from ...Datatypes.KwantWrdInKilogramPerMeter import (
    KwantWrdInKilogramPerMeter,
    KwantWrdInKilogramPerMeterWaarden,
)
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabel(AIMNaamObject, LijnGeometrie):
    """Abstracte voor attributen en relaties van allerlei types kabels."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doorverbinddoos', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdoorboring', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buitenkast', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#CameraGroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DynBordGroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVModule', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meteostation', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#WegverlichtingGroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRSS', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IndoorKast', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lockerkast', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._buitenmantelDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                                  naam='buitenmantelDiameter',
                                                  label='buitenmantel diameter',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel.buitenmantelDiameter',
                                                  definition='De buitenste afmeting van de kabel in millimeter.',
                                                  owner=self)

        self._buitenmantelKleur = OTLAttribuut(field=KlKabelmantelKleur,
                                               naam='buitenmantelKleur',
                                               label='buitenmantel kleur',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel.buitenmantelKleur',
                                               definition='De hoofdkleur(en) die voor een waarnemer onmiddellijk zichtbaar is (zijn) zonder de kabel te ontmantelen, de kleur van de markeringen op die buitenste mantel buiten beschouwing gelaten.',
                                               owner=self)

        self._fabrikant = OTLAttribuut(field=KlKabelFabrikant,
                                       naam='fabrikant',
                                       label='fabrikant',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel.fabrikant',
                                       definition='De naam van de producent van de kabel.',
                                       owner=self)

        self._gewicht = OTLAttribuut(field=KwantWrdInKilogramPerMeter,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel.gewicht',
                                     definition='Het gewicht van de kabel per meter.',
                                     owner=self)

        self._typeBescherming = OTLAttribuut(field=KlKabelLeidingBescherming,
                                             naam='typeBescherming',
                                             label='type bescherming',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel.typeBescherming',
                                             definition='Geeft aan of en hoe de leiding bijkomend mechanisch beschermd is.',
                                             owner=self)

    @property
    def buitenmantelDiameter(self) -> KwantWrdInMillimeterWaarden:
        """De buitenste afmeting van de kabel in millimeter."""
        return self._buitenmantelDiameter.get_waarde()

    @buitenmantelDiameter.setter
    def buitenmantelDiameter(self, value):
        self._buitenmantelDiameter.set_waarde(value, owner=self)

    @property
    def buitenmantelKleur(self) -> str:
        """De hoofdkleur(en) die voor een waarnemer onmiddellijk zichtbaar is (zijn) zonder de kabel te ontmantelen, de kleur van de markeringen op die buitenste mantel buiten beschouwing gelaten."""
        return self._buitenmantelKleur.get_waarde()

    @buitenmantelKleur.setter
    def buitenmantelKleur(self, value):
        self._buitenmantelKleur.set_waarde(value, owner=self)

    @property
    def fabrikant(self) -> str:
        """De naam van de producent van de kabel."""
        return self._fabrikant.get_waarde()

    @fabrikant.setter
    def fabrikant(self, value):
        self._fabrikant.set_waarde(value, owner=self)

    @property
    def gewicht(self) -> KwantWrdInKilogramPerMeterWaarden:
        """Het gewicht van de kabel per meter."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def typeBescherming(self) -> str:
        """Geeft aan of en hoe de leiding bijkomend mechanisch beschermd is."""
        return self._typeBescherming.get_waarde()

    @typeBescherming.setter
    def typeBescherming(self, value):
        self._typeBescherming.set_waarde(value, owner=self)
