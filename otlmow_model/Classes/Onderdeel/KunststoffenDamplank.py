# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.DamplankAbstracte import DamplankAbstracte
from otlmow_model.Datatypes.DtcKunststofspecificaties import DtcKunststofspecificaties, DtcKunststofspecificatiesWaarden
from otlmow_model.Datatypes.KlKunststoffenDamplankvorm import KlKunststoffenDamplankvorm
from otlmow_model.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class KunststoffenDamplank(DamplankAbstracte):
    """Een grondkerende plank, vervaardigd uit kunststof (bv. PVC, glasvezel, composiet, ...), die kan bestaan in verschillende plankvormen. De plank weegt minder dan beton, hout of staal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KunststoffenDamplank'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SteunStandaard')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')

        self._dikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KunststoffenDamplank.dikte',
                                   definition='De dikte van de kunststoffen damplank in millimeter.',
                                   owner=self)

        self._kunststofspecificaties = OTLAttribuut(field=DtcKunststofspecificaties,
                                                    naam='kunststofspecificaties',
                                                    label='kunststofspecificaties',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KunststoffenDamplank.kunststofspecificaties',
                                                    definition='Document dat de specificaties van het kunststof bijhoudt.',
                                                    owner=self)

        self._vorm = OTLAttribuut(field=KlKunststoffenDamplankvorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KunststoffenDamplank.vorm',
                                  definition='De uitvoering van de kunstoffen damplank.',
                                  owner=self)

    @property
    def dikte(self) -> KwantWrdInMillimeterWaarden:
        """De dikte van de kunststoffen damplank in millimeter."""
        return self._dikte.get_waarde()

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def kunststofspecificaties(self) -> DtcKunststofspecificatiesWaarden:
        """Document dat de specificaties van het kunststof bijhoudt."""
        return self._kunststofspecificaties.get_waarde()

    @kunststofspecificaties.setter
    def kunststofspecificaties(self, value):
        self._kunststofspecificaties.set_waarde(value, owner=self)

    @property
    def vorm(self) -> str:
        """De uitvoering van de kunstoffen damplank."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
