# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordconceptStatus(KeuzelijstField):
    """Keuzelijst met waarden die aangeven of een verkeersbordconcept nog gebruikt wordt."""
    naam = 'KlVerkeersbordconceptStatus'
    label = 'VerkeersbordconceptStatus'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordconceptStatus'
    definition = 'Keuzelijst met waarden die aangeven of een verkeersbordconcept nog gebruikt wordt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordconceptStatus'
    options = {
        'afgeschaft': KeuzelijstWaarde(invulwaarde='afgeschaft',
                                       label='afgeschaft',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordconceptStatus/afgeschaft'),
        'stabiel': KeuzelijstWaarde(invulwaarde='stabiel',
                                    label='stabiel',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordconceptStatus/stabiel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

