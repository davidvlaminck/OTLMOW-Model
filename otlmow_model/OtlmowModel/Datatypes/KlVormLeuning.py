# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVormLeuning(KeuzelijstField):
    """De keuzelijst die de verschillende opties van vormen voor een leuning bevat."""
    naam = 'KlVormLeuning'
    label = 'Vorm leuning'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlVormLeuning'
    definition = 'De keuzelijst die de verschillende opties van vormen voor een leuning bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormLeuning'
    options = {
        'getrapt': KeuzelijstWaarde(invulwaarde='getrapt',
                                    label='Getrapt',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormLeuning/getrapt'),
        'rechthoekig': KeuzelijstWaarde(invulwaarde='rechthoekig',
                                        label='Rechthoekig',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormLeuning/rechthoekig')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

