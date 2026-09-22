# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactpuntModelnaam(KeuzelijstField):
    """Lijst van modelnamen van contactpunten volgens de fabrikant."""
    naam = 'KlContactpuntModelnaam'
    label = 'Modelnamen contactpunten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactpuntModelnaam'
    definition = 'Lijst van modelnamen van contactpunten volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactpuntModelnaam'
    options = {
        'aritech-dc-107': KeuzelijstWaarde(invulwaarde='aritech-dc-107',
                                           label='Aritech-DC-107',
                                           status='ingebruik',
                                           definitie='Aritech-DC-107',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactpuntModelnaam/aritech-dc-107'),
        'em-7wfm': KeuzelijstWaarde(invulwaarde='em-7wfm',
                                    label='EM-7WFM',
                                    status='ingebruik',
                                    definitie='EM-7WFM (Maasland Groep)',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactpuntModelnaam/em-7wfm'),
        'ii502a': KeuzelijstWaarde(invulwaarde='ii502a',
                                   label='II502a',
                                   status='ingebruik',
                                   definitie='II502a (IFM)',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactpuntModelnaam/ii502a'),
        'iq2010': KeuzelijstWaarde(invulwaarde='iq2010',
                                   label='IQ2010',
                                   status='ingebruik',
                                   definitie='IQ2010 (IFM)',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactpuntModelnaam/iq2010')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

