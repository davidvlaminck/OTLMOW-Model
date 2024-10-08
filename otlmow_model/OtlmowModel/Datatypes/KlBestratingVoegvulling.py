# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestratingVoegvulling(KeuzelijstField):
    """De voegvullingen van de bestrating."""
    naam = 'KlBestratingVoegvulling'
    label = 'Bestrating voegvulling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingVoegvulling'
    definition = 'De voegvullingen van de bestrating.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingVoegvulling'
    options = {
        'granulaatmengsel-0-4': KeuzelijstWaarde(invulwaarde='granulaatmengsel-0-4',
                                                 label='granulaatmengsel 0-4',
                                                 status='ingebruik',
                                                 definitie='granulaatmengsel 0/4',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/granulaatmengsel-0-4'),
        'granulaatmengsel-0-6.3': KeuzelijstWaarde(invulwaarde='granulaatmengsel-0-6.3',
                                                   label='granulaatmengsel 0-6.3',
                                                   status='ingebruik',
                                                   definitie='granulaatmengsel 0/63',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/granulaatmengsel-0-6.3'),
        'mortel-met-bouwklasse-B6-B10': KeuzelijstWaarde(invulwaarde='mortel-met-bouwklasse-B6-B10',
                                                         label='mortel met bouwklasse B6-B10',
                                                         status='ingebruik',
                                                         definitie='mortel met bouwklasse B6-B10',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/mortel-met-bouwklasse-B6-B10'),
        'mortel-met-bouwklasse-BF': KeuzelijstWaarde(invulwaarde='mortel-met-bouwklasse-BF',
                                                     label='mortel met bouwklasse BF',
                                                     status='ingebruik',
                                                     definitie='mortel met bouwklasse BF',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/mortel-met-bouwklasse-BF'),
        'split': KeuzelijstWaarde(invulwaarde='split',
                                  label='split',
                                  status='ingebruik',
                                  definitie='split',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/split'),
        'steenslag-2-4': KeuzelijstWaarde(invulwaarde='steenslag-2-4',
                                          label='steenslag 2-4',
                                          status='ingebruik',
                                          definitie='steenslag 2/4',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/steenslag-2-4'),
        'steenslag-2-6.3': KeuzelijstWaarde(invulwaarde='steenslag-2-6.3',
                                            label='steenslag 2-6.3',
                                            status='ingebruik',
                                            definitie='steenslag 2/6.3',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/steenslag-2-6.3'),
        'zandcement': KeuzelijstWaarde(invulwaarde='zandcement',
                                       label='zandcement',
                                       status='ingebruik',
                                       definitie='zandcement',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingVoegvulling/zandcement')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

