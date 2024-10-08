# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelmofType(KeuzelijstField):
    """Types voor kabel- en leidingmoffen."""
    naam = 'KlKabelmofType'
    label = 'Kabelmof type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKabelmofType'
    definition = 'Types voor kabel- en leidingmoffen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelmofType'
    options = {
        'geldoos': KeuzelijstWaarde(invulwaarde='geldoos',
                                    label='geldoos',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmofType/geldoos'),
        'gietmof': KeuzelijstWaarde(invulwaarde='gietmof',
                                    label='gietmof',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmofType/gietmof'),
        'hdpe-mof': KeuzelijstWaarde(invulwaarde='hdpe-mof',
                                     label='HDPE mof',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmofType/hdpe-mof')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

