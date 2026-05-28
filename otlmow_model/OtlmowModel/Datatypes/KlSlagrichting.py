# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlagrichting(KeuzelijstField):
    """De mogelijke slagrichting van een staalkabel."""
    naam = 'KlSlagrichting'
    label = 'Slagrichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlagrichting'
    definition = 'De mogelijke slagrichting van een staalkabel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlagrichting'
    options = {
        'links-afwisselende-slag-(lh-al)': KeuzelijstWaarde(invulwaarde='links-afwisselende-slag-(lh-al)',
                                                            label='links-afwisselende slag (LH-AL)',
                                                            status='ingebruik',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlagrichting/links-afwisselende-slag-(lh-al)'),
        'links-kruisslag-(lh-ol)': KeuzelijstWaarde(invulwaarde='links-kruisslag-(lh-ol)',
                                                    label='links-kruisslag (LH-OL)',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlagrichting/links-kruisslag-(lh-ol)'),
        'links-langslag-(lh-ll)': KeuzelijstWaarde(invulwaarde='links-langslag-(lh-ll)',
                                                   label='Links-langslag (LH-LL)',
                                                   status='ingebruik',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlagrichting/links-langslag-(lh-ll)'),
        'rechts-afwisselende-slag-(rh-al)': KeuzelijstWaarde(invulwaarde='rechts-afwisselende-slag-(rh-al)',
                                                             label='rechts-afwisselende slag (RH-AL)',
                                                             status='ingebruik',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlagrichting/rechts-afwisselende-slag-(rh-al)'),
        'rechts-kruisslag-(rh-ol)': KeuzelijstWaarde(invulwaarde='rechts-kruisslag-(rh-ol)',
                                                     label='rechts-kruisslag (RH-OL)',
                                                     status='ingebruik',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlagrichting/rechts-kruisslag-(rh-ol)'),
        'rechts-langslag-(rh-ll)': KeuzelijstWaarde(invulwaarde='rechts-langslag-(rh-ll)',
                                                    label='rechts-langslag (RH-LL)',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlagrichting/rechts-langslag-(rh-ll)')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

