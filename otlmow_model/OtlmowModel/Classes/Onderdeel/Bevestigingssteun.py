# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcBeschermendeLaag import DtcBeschermendeLaag, DtcBeschermendeLaagWaarden
from ...Datatypes.KlAlgMateriaal import KlAlgMateriaal
from ...Datatypes.KlBevestigingssteunMerk import KlBevestigingssteunMerk
from ...Datatypes.KlBevestigingssteunModelnaam import KlBevestigingssteunModelnaam
from ...Datatypes.KlBevestigingssteunType import KlBevestigingssteunType
from ...Datatypes.KlDraagConstrBeschermlaag import KlDraagConstrBeschermlaag
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bevestigingssteun(AIMNaamObject, PuntGeometrie):
    """Een solide verbindingsstuk waaraan een object kan worden bevestigd ter ondersteuning en bevestiging aan een oppervlak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingssteun'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendmast', direction='u')  # u = unidirectional

        self._beschermendeLaag = OTLAttribuut(field=DtcBeschermendeLaag,
                                              naam='beschermendeLaag',
                                              label='beschermende laag',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingssteun.beschermendeLaag',
                                              definition='Het type van bescherming van de constructie of steun met de corresponderende corrosieklasse.',
                                              owner=self)

        self._beschermlaag = OTLAttribuut(field=KlDraagConstrBeschermlaag,
                                          naam='beschermlaag',
                                          label='beschermlaag',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingssteun.beschermlaag',
                                          usagenote='Attribuut uit gebruik sinds versie 2.12.0 ',
                                          deprecated_version='2.12.0',
                                          definition='Type bescherming van de steun, bv. geschilderd, gegalvaniseerd, ....',
                                          owner=self)

        self._hoogteBovenkant = OTLAttribuut(field=KwantWrdInMeter,
                                             naam='hoogteBovenkant',
                                             label='hoogte bovenkant',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingssteun.hoogteBovenkant',
                                             definition='Hoogte van het maaiveld tot aan de bovenkant van de bevestigingssteun in meter.',
                                             owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingssteun.lengte',
                                    definition='De lengte van de bevestigingssteun in  millimeter.',
                                    owner=self)

        self._materiaal = OTLAttribuut(field=KlAlgMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingssteun.materiaal',
                                       definition='Het materiaal waaruit de steun vervaardigd is.',
                                       owner=self)

        self._merk = OTLAttribuut(field=KlBevestigingssteunMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingssteun.merk',
                                  definition='Het merk van de bevestigingssteun.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlBevestigingssteunModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingssteun.modelnaam',
                                       definition='Het model van de bevestigingssteun zoals gekend bij de fabrikant.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlBevestigingssteunType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingssteun.type',
                                  definition='Typering van de bevestigingssteun.',
                                  owner=self)

    @property
    def beschermendeLaag(self) -> DtcBeschermendeLaagWaarden:
        """Het type van bescherming van de constructie of steun met de corresponderende corrosieklasse."""
        return self._beschermendeLaag.get_waarde()

    @beschermendeLaag.setter
    def beschermendeLaag(self, value):
        self._beschermendeLaag.set_waarde(value, owner=self)

    @property
    def beschermlaag(self) -> str:
        """Type bescherming van de steun, bv. geschilderd, gegalvaniseerd, ...."""
        return self._beschermlaag.get_waarde()

    @beschermlaag.setter
    def beschermlaag(self, value):
        self._beschermlaag.set_waarde(value, owner=self)

    @property
    def hoogteBovenkant(self) -> KwantWrdInMeterWaarden:
        """Hoogte van het maaiveld tot aan de bovenkant van de bevestigingssteun in meter."""
        return self._hoogteBovenkant.get_waarde()

    @hoogteBovenkant.setter
    def hoogteBovenkant(self, value):
        self._hoogteBovenkant.set_waarde(value, owner=self)

    @property
    def lengte(self) -> KwantWrdInMillimeterWaarden:
        """De lengte van de bevestigingssteun in  millimeter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de steun vervaardigd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de bevestigingssteun."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Het model van de bevestigingssteun zoals gekend bij de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Typering van de bevestigingssteun."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
