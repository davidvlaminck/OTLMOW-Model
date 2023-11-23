# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHardwareOS(KeuzelijstField):
    """vb : Windows 10 SP1, Windows 10 SP2, unix."""
    naam = 'KlHardwareOS'
    label = 'Hardware OS'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlHardwareOS'
    definition = 'vb : Windows 10 SP1, Windows 10 SP2, unix.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareOS'
    options = {
        'cent-os-linux-7-core': KeuzelijstWaarde(invulwaarde='cent-os-linux-7-core',
                                                 label='CentOS Linux 7 (Core)',
                                                 status='ingebruik',
                                                 definitie='CentOS Linux 7 (Core)',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/cent-os-linux-7-core'),
        'unix': KeuzelijstWaarde(invulwaarde='unix',
                                 label='unix',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/unix'),
        'win2019': KeuzelijstWaarde(invulwaarde='win2019',
                                    label='Win2019',
                                    status='ingebruik',
                                    definitie='Win2019',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/win2019'),
        'windows-10-SP1': KeuzelijstWaarde(invulwaarde='windows-10-SP1',
                                           label='windows 10 SP1',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/windows-10-SP1'),
        'windows-10-SP2': KeuzelijstWaarde(invulwaarde='windows-10-SP2',
                                           label='windows 10 SP2',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/windows-10-SP2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

