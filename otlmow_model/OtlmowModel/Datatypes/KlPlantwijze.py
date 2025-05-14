# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlantwijze(KeuzelijstField):
    """De mogelijke (aanplant)plantmanieren."""
    naam = 'KlPlantwijze'
    label = 'Plantwijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlPlantwijze'
    definition = 'De mogelijke (aanplant)plantmanieren.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlantwijze'
    options = {
        'in-groep-van-2-5-stuks': KeuzelijstWaarde(invulwaarde='in-groep-van-2-5-stuks',
                                                   label='in groep van 2 - 5 stuks',
                                                   status='ingebruik',
                                                   definitie='0,7 - in groep van 2 - 5 stuks',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantwijze/in-groep-van-2-5-stuks'),
        'in-groep-van-6-10-stuks': KeuzelijstWaarde(invulwaarde='in-groep-van-6-10-stuks',
                                                    label='in groep van 6 - 10 stuks',
                                                    status='ingebruik',
                                                    definitie='0,6 - in groep van 6 - 10 stuks',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantwijze/in-groep-van-6-10-stuks'),
        'in-grote-dicht-beplante-groepen': KeuzelijstWaarde(invulwaarde='in-grote-dicht-beplante-groepen',
                                                            label='in grote dicht beplante groepen',
                                                            status='ingebruik',
                                                            definitie='0,4 - in grote dicht beplante groepen (>10 stuks) (ook bosachtige beplantingen, bospark)',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantwijze/in-grote-dicht-beplante-groepen'),
        'perfecte-rijbeplanting-zonder-uitval': KeuzelijstWaarde(invulwaarde='perfecte-rijbeplanting-zonder-uitval',
                                                                 label='perfecte rijbeplanting (zonder uitval)',
                                                                 status='ingebruik',
                                                                 definitie='0,9 - perfecte rijbeplanting (zonder uitval)',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantwijze/perfecte-rijbeplanting-zonder-uitval'),
        'rijbeplanting-met-belangrijke-uitval': KeuzelijstWaarde(invulwaarde='rijbeplanting-met-belangrijke-uitval',
                                                                 label='rijbeplanting met belangrijke uitval',
                                                                 status='ingebruik',
                                                                 definitie='0,8 - rijbeplanting met belangrijke uitval',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantwijze/rijbeplanting-met-belangrijke-uitval'),
        'solitair': KeuzelijstWaarde(invulwaarde='solitair',
                                     label='solitair',
                                     status='ingebruik',
                                     definitie='1 - solitair',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantwijze/solitair')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

