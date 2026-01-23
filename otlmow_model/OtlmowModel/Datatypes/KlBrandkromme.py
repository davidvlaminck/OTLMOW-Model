# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandkromme(KeuzelijstField):
    """Keuzelijst met de verschillende specifieke temperatuur-tijdscurves die als belasting is gehanteerd bij de validatie van de brandweerstand."""
    naam = 'KlBrandkromme'
    label = 'brandkromme'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandkromme'
    definition = 'Keuzelijst met de verschillende specifieke temperatuur-tijdscurves die als belasting is gehanteerd bij de validatie van de brandweerstand.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandkromme'
    options = {
        'hc': KeuzelijstWaarde(invulwaarde='hc',
                               label='HC',
                               status='ingebruik',
                               definitie='HC',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandkromme/hc'),
        'hcm': KeuzelijstWaarde(invulwaarde='hcm',
                                label='HCM',
                                status='ingebruik',
                                definitie='HCM',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandkromme/hcm'),
        'iso': KeuzelijstWaarde(invulwaarde='iso',
                                label='ISO',
                                status='ingebruik',
                                definitie='ISO',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandkromme/iso'),
        'rabt': KeuzelijstWaarde(invulwaarde='rabt',
                                 label='RABT',
                                 status='ingebruik',
                                 definitie='RABT',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandkromme/rabt'),
        'rws': KeuzelijstWaarde(invulwaarde='rws',
                                label='RWS',
                                status='ingebruik',
                                definitie='RWS',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandkromme/rws')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

