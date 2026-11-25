# coding=utf-8
from typing import ClassVar

from ...BaseClasses.IntegerField import IntegerField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LaagBouwklasse import LaagBouwklasse
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcSupplementenCBV import (
    DtcSupplementenCBV,
    DtcSupplementenCBVWaarden,
)
from ...Datatypes.KlCBVAardVerharding import KlCBVAardVerharding
from ...Datatypes.KlCBVLaagtype import KlCBVLaagtype
from ...Datatypes.KlCBVOppervlaktebehandeling import KlCBVOppervlaktebehandeling
from ...Datatypes.KwantWrdInKubiekeMeter import (
    KwantWrdInKubiekeMeter,
    KwantWrdInKubiekeMeterWaarden,
)
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cementbetonverharding(LaagBouwklasse, NaampadObject):
    """Stijve verharding met of zonder wapening verkregen door cementbeton te spreiden en mechanisch te verdichten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegreflector', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefConsistentie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDruksterkte', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGemetenDikte', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefHechtsterkte', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLangsvlakheid', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuchtgehalte', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRolgeluid', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStaalvezelgehalte', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStroefheid', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTextuurdiepte', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVerankeringskracht', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVlakheid', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWatergehalte', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWateropslorping', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWeerstandAfschilfering', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._aantalAnkerstaven = OTLAttribuut(field=IntegerField,
                                               naam='aantalAnkerstaven',
                                               label='aantal ankerstaven',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.aantalAnkerstaven',
                                               definition='Aantal ankerstaven waarmee de voegen verankerd zijn.',
                                               owner=self)

        self._aardVerharding = OTLAttribuut(field=KlCBVAardVerharding,
                                            naam='aardVerharding',
                                            label='aard verharding',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.aardVerharding',
                                            definition='De uitvoeringswijze van de cementbetonverharding.',
                                            owner=self)

        self._krimpvoegFrequentie = OTLAttribuut(field=KwantWrdInMeter,
                                                 naam='krimpvoegFrequentie',
                                                 label='krimpvoeg frequentie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.krimpvoegFrequentie',
                                                 definition='De afstand tussen de krimpvoegen in meter.',
                                                 owner=self)

        self._laagtype = OTLAttribuut(field=KlCBVLaagtype,
                                      naam='laagtype',
                                      label='laagtype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.laagtype',
                                      definition='Het type van de cementbetonverhardingslaag.',
                                      owner=self)

        self._oppervlakbehandeling = OTLAttribuut(field=KlCBVOppervlaktebehandeling,
                                                  naam='oppervlakbehandeling',
                                                  label='oppervlakbehandeling',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.oppervlakbehandeling',
                                                  definition='Behandeling die wordt toegepast op het oppervlak van een laag, met of zonder toevoeging van materialen, en bestemd is om de eigenschappen van de laag te verbeteren, hetzij bij de uitvoering, hetzij achteraf.',
                                                  owner=self)

        self._supplementen = OTLAttribuut(field=DtcSupplementenCBV,
                                          naam='supplementen',
                                          label='supplementen van de verharding',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.supplementen',
                                          definition='Additionele toevoegingen aan de verharding.',
                                          owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding.volume',
                                    definition='Het volume van cementbetonverharding in kubieke meter.',
                                    owner=self)

    @property
    def aantalAnkerstaven(self) -> int:
        """Aantal ankerstaven waarmee de voegen verankerd zijn."""
        return self._aantalAnkerstaven.get_waarde()

    @aantalAnkerstaven.setter
    def aantalAnkerstaven(self, value):
        self._aantalAnkerstaven.set_waarde(value, owner=self)

    @property
    def aardVerharding(self) -> str:
        """De uitvoeringswijze van de cementbetonverharding."""
        return self._aardVerharding.get_waarde()

    @aardVerharding.setter
    def aardVerharding(self, value):
        self._aardVerharding.set_waarde(value, owner=self)

    @property
    def krimpvoegFrequentie(self) -> KwantWrdInMeterWaarden:
        """De afstand tussen de krimpvoegen in meter."""
        return self._krimpvoegFrequentie.get_waarde()

    @krimpvoegFrequentie.setter
    def krimpvoegFrequentie(self, value):
        self._krimpvoegFrequentie.set_waarde(value, owner=self)

    @property
    def laagtype(self) -> str:
        """Het type van de cementbetonverhardingslaag."""
        return self._laagtype.get_waarde()

    @laagtype.setter
    def laagtype(self, value):
        self._laagtype.set_waarde(value, owner=self)

    @property
    def oppervlakbehandeling(self) -> str:
        """Behandeling die wordt toegepast op het oppervlak van een laag, met of zonder toevoeging van materialen, en bestemd is om de eigenschappen van de laag te verbeteren, hetzij bij de uitvoering, hetzij achteraf."""
        return self._oppervlakbehandeling.get_waarde()

    @oppervlakbehandeling.setter
    def oppervlakbehandeling(self, value):
        self._oppervlakbehandeling.set_waarde(value, owner=self)

    @property
    def supplementen(self) -> DtcSupplementenCBVWaarden:
        """Additionele toevoegingen aan de verharding."""
        return self._supplementen.get_waarde()

    @supplementen.setter
    def supplementen(self, value):
        self._supplementen.set_waarde(value, owner=self)

    @property
    def volume(self) -> KwantWrdInKubiekeMeterWaarden:
        """Het volume van cementbetonverharding in kubieke meter."""
        return self._volume.get_waarde()

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
