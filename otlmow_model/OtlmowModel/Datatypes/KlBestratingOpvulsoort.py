# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestratingOpvulsoort(KeuzelijstField):
    """De mogelijke opvulsoorten van de grasbetontegel en graskunststofplaat."""
    naam = 'KlBestratingOpvulsoort'
    label = 'Bestrating opvulsoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingOpvulsoort'
    definition = 'De mogelijke opvulsoorten van de grasbetontegel en graskunststofplaat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingOpvulsoort'
    options = {
        'bodemsubstraat': KeuzelijstWaarde(invulwaarde='bodemsubstraat',
                                           label='bodemsubstraat',
                                           status='ingebruik',
                                           definitie='Opgevuld met bodemsubstraat.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/bodemsubstraat'),
        'bodemsubstraat-en-ingezaaid': KeuzelijstWaarde(invulwaarde='bodemsubstraat-en-ingezaaid',
                                                        label='bodemsubstraat en ingezaaid',
                                                        status='ingebruik',
                                                        definitie='Opgevuld met bodemsubstraat en ingezaaid.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/bodemsubstraat-en-ingezaaid'),
        'bomenzand': KeuzelijstWaarde(invulwaarde='bomenzand',
                                      label='bomenzand',
                                      status='ingebruik',
                                      definitie='Opgevuld met bomenzand.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/bomenzand'),
        'bomenzand-en-ingezaaid': KeuzelijstWaarde(invulwaarde='bomenzand-en-ingezaaid',
                                                   label='bomenzand en ingezaaid',
                                                   status='ingebruik',
                                                   definitie='Opgevuld met bomenzand en ingezaaid.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/bomenzand-en-ingezaaid'),
        'steenslag-2-6.3': KeuzelijstWaarde(invulwaarde='steenslag-2-6.3',
                                            label='steenslag 2-6.3',
                                            status='ingebruik',
                                            definitie='Opgevuld met steenslag 2/6,3',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/steenslag-2-6.3')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

