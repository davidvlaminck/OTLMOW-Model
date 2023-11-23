# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTGCUitbreidingsModuleType(KeuzelijstField):
    """Keuzelijst om het type uitbreidingsmodule van een toeganscontroller te specifiëren."""
    naam = 'KlTGCUitbreidingsModuleType'
    label = 'TGC uitbreidingsmodule type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTGCUitbreidingsModuleType'
    definition = 'Keuzelijst om het type uitbreidingsmodule van een toeganscontroller te specifiëren.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTGCUitbreidingsModuleType'
    options = {
        'deurmodule': KeuzelijstWaarde(invulwaarde='deurmodule',
                                       label='Deurmodule',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTGCUitbreidingsModuleType/deurmodule'),
        'iomodule': KeuzelijstWaarde(invulwaarde='iomodule',
                                     label='IOModule',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTGCUitbreidingsModuleType/iomodule')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

