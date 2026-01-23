# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBrandwerendeBekleding(KeuzelijstField):
    """De verschijningsvorm of applicatiemethode van het materiaal, zoals plaat, paneel, gespoten materiaal of intumescente verf."""
    naam = 'KlTypeBrandwerendeBekleding'
    label = 'type brandwerende bekleding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBrandwerendeBekleding'
    definition = 'De verschijningsvorm of applicatiemethode van het materiaal, zoals plaat, paneel, gespoten materiaal of intumescente verf.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBrandwerendeBekleding'
    options = {
        'gespoten-materiaal': KeuzelijstWaarde(invulwaarde='gespoten-materiaal',
                                               label='gespoten materiaal',
                                               status='ingebruik',
                                               definitie='gespoten materiaal',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrandwerendeBekleding/gespoten-materiaal'),
        'intumescerende-verf': KeuzelijstWaarde(invulwaarde='intumescerende-verf',
                                                label='intumescerende verf',
                                                status='ingebruik',
                                                definitie='intumescerende verf',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrandwerendeBekleding/intumescerende-verf'),
        'plaat': KeuzelijstWaarde(invulwaarde='plaat',
                                  label='plaat',
                                  status='ingebruik',
                                  definitie='plaat',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrandwerendeBekleding/plaat')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

