# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEDDriverModelnaam(KeuzelijstField):
    """De modelnaam van de LED-driver."""
    naam = 'KlLEDDriverModelnaam'
    label = 'LED-driver modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEDDriverModelnaam'
    definition = 'De modelnaam van de LED-driver.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEDDriverModelnaam'
    options = {
        'elg-100-c350b-3y': KeuzelijstWaarde(invulwaarde='elg-100-c350b-3y',
                                             label='ELG 100 C350B 3Y',
                                             status='ingebruik',
                                             definitie='ELG 100 C350B 3Y',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverModelnaam/elg-100-c350b-3y'),
        'hlg-320h-c700b': KeuzelijstWaarde(invulwaarde='hlg-320h-c700b',
                                           label='HLG 320H C700B',
                                           status='ingebruik',
                                           definitie='HLG 320H C700B',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverModelnaam/hlg-320h-c700b'),
        'ot-dx-110-220-240-1a0-dima-lt2-e': KeuzelijstWaarde(invulwaarde='ot-dx-110-220-240-1a0-dima-lt2-e',
                                                             label='OT DX 110 220-240 1A0 DIMA LT2 E',
                                                             status='ingebruik',
                                                             definitie='OT DX 110 220-240 1A0 DIMA LT2 E',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverModelnaam/ot-dx-110-220-240-1a0-dima-lt2-e'),
        'ot-dx-165-220-240-1a0-dima-lt2-e': KeuzelijstWaarde(invulwaarde='ot-dx-165-220-240-1a0-dima-lt2-e',
                                                             label='OT DX 165 220-240 1A0 DIMA LT2 E',
                                                             status='ingebruik',
                                                             definitie='OT DX 165 220-240 1A0 DIMA LT2 E',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverModelnaam/ot-dx-165-220-240-1a0-dima-lt2-e'),
        'ot-dx-40-220-240-1a0-dima-lt2-e': KeuzelijstWaarde(invulwaarde='ot-dx-40-220-240-1a0-dima-lt2-e',
                                                            label='OT DX 40 220-240 1A0 DIMA LT2 E',
                                                            status='ingebruik',
                                                            definitie='OT DX 40 220-240 1A0 DIMA LT2 E',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverModelnaam/ot-dx-40-220-240-1a0-dima-lt2-e'),
        'ot-dx-75-220-240-1a0-dima-lt2-e': KeuzelijstWaarde(invulwaarde='ot-dx-75-220-240-1a0-dima-lt2-e',
                                                            label='OT DX 75 220-240 1A0 DIMA LT2 E',
                                                            status='ingebruik',
                                                            definitie='OT DX 75 220-240 1A0 DIMA LT2 E',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverModelnaam/ot-dx-75-220-240-1a0-dima-lt2-e'),
        'xi-sr-110w-0-2-0-7a-snemp-230v-c150-sxt': KeuzelijstWaarde(invulwaarde='xi-sr-110w-0-2-0-7a-snemp-230v-c150-sxt',
                                                                    label='Xi SR 110W 0.2-0.7A SNEMP 230V C150 sXt',
                                                                    status='ingebruik',
                                                                    definitie='Xi SR 110W 0.2-0.7A SNEMP 230V C150 sXt',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverModelnaam/xi-sr-110w-0-2-0-7a-snemp-230v-c150-sxt'),
        'xi-sr-150w-0-2-0-7a-snemp-230v-s240-sxt': KeuzelijstWaarde(invulwaarde='xi-sr-150w-0-2-0-7a-snemp-230v-s240-sxt',
                                                                    label='Xi SR 150W 0.2-0.7A SNEMP 230V S240 sXt',
                                                                    status='ingebruik',
                                                                    definitie='Xi SR 150W 0.2-0.7A SNEMP 230V S240 sXt',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverModelnaam/xi-sr-150w-0-2-0-7a-snemp-230v-s240-sxt'),
        'xi-sr-40w-0-2-0-7a-snemp-230v-c133-sxt': KeuzelijstWaarde(invulwaarde='xi-sr-40w-0-2-0-7a-snemp-230v-c133-sxt',
                                                                   label='Xi SR 40W 0.2-0.7A SNEMP 230V C133 sXt',
                                                                   status='ingebruik',
                                                                   definitie='Xi SR 40W 0.2-0.7A SNEMP 230V C133 sXt',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEDDriverModelnaam/xi-sr-40w-0-2-0-7a-snemp-230v-c133-sxt')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

