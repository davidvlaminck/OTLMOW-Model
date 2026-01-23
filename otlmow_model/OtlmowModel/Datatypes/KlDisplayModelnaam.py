# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDisplayModelnaam(KeuzelijstField):
    """Lijst met modelnamen van displays volgens de fabrikant."""
    naam = 'KlDisplayModelnaam'
    label = 'Display modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDisplayModelnaam'
    definition = 'Lijst met modelnamen van displays volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDisplayModelnaam'
    options = {
        'ktp1200': KeuzelijstWaarde(invulwaarde='ktp1200',
                                    label='KTP1200',
                                    status='ingebruik',
                                    definitie='KTP1200',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDisplayModelnaam/ktp1200')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

