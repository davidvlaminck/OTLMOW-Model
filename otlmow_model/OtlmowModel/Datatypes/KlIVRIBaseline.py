# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIBaseline(KeuzelijstField):
    """De specificatieversie van het protocol van de iVRI component."""
    naam = 'KlIVRIBaseline'
    label = 'iVRIBaseline'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlIVRIBaseline'
    definition = 'De specificatieversie van het protocol van de iVRI component.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIBaseline'
    options = {
        'idd-ris-fi-version-1-3-0': KeuzelijstWaarde(invulwaarde='idd-ris-fi-version-1-3-0',
                                                     label='IDD RIS-FI version 1.3.0',
                                                     status='ingebruik',
                                                     definitie='IDD RIS-FI version 1.3.0',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIBaseline/idd-ris-fi-version-1-3-0'),
        'idd-tlc-fi-version-1-3-1': KeuzelijstWaarde(invulwaarde='idd-tlc-fi-version-1-3-1',
                                                     label='IDD TLC-FI version 1.3.1',
                                                     status='ingebruik',
                                                     definitie='IDD TLC-FI version 1.3.1',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIBaseline/idd-tlc-fi-version-1-3-1'),
        'idd-tlc-fi-version-1-4-0': KeuzelijstWaarde(invulwaarde='idd-tlc-fi-version-1-4-0',
                                                     label='IDD TLC-FI version 1.4.0',
                                                     status='ingebruik',
                                                     definitie='IDD TLC-FI version 1.4.0',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIBaseline/idd-tlc-fi-version-1-4-0'),
        'idd-tlc-fi-version-2-0-1': KeuzelijstWaarde(invulwaarde='idd-tlc-fi-version-2-0-1',
                                                     label='IDD TLC-FI version 2.0.1',
                                                     status='ingebruik',
                                                     definitie='IDD TLC-FI version 2.0.1',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIBaseline/idd-tlc-fi-version-2-0-1')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

