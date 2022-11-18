# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.LaagBouwklasse import LaagBouwklasse
from otlmow_model.Datatypes.DtcSupplementenCBV import DtcSupplementenCBV, DtcSupplementenCBVWaarden
from otlmow_model.BaseClasses.IntegerField import IntegerField
from otlmow_model.Datatypes.KlCBVAardVerharding import KlCBVAardVerharding
from otlmow_model.Datatypes.KlCBVLaagtype import KlCBVLaagtype
from otlmow_model.Datatypes.KlCBVOppervlaktebehandeling import KlCBVOppervlaktebehandeling
from otlmow_model.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter, KwantWrdInKubiekeMeterWaarden
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cementbetonverharding(LaagBouwklasse):
    """Stijve verharding met of zonder wapening verkregen door cementbeton te spreiden en mechanisch te verdichten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verankeringslandhoofd')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegreflector')

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
