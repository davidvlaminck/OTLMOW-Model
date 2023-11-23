# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestratingselementAfmetingLxB(KeuzelijstField):
    """De afmetingen of aanduidingen voor bestrating van betonstraatstenen."""
    naam = 'KlBestratingselementAfmetingLxB'
    label = 'Afmeting bestratingselement lengte x breedte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingselementAfmetingLxB'
    definition = 'De afmetingen of aanduidingen voor bestrating van betonstraatstenen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingselementAfmetingLxB'
    options = {
        '1000-x-1000': KeuzelijstWaarde(invulwaarde='1000-x-1000',
                                        label='1000 x 1000',
                                        status='ingebruik',
                                        definitie='1000 x 1000',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/1000-x-1000'),
        '150-x-150': KeuzelijstWaarde(invulwaarde='150-x-150',
                                      label='150 x 150',
                                      status='ingebruik',
                                      definitie='150 x 150',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/150-x-150'),
        '200-x-200': KeuzelijstWaarde(invulwaarde='200-x-200',
                                      label='200 x 200',
                                      status='ingebruik',
                                      definitie='200 x 200',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/200-x-200'),
        '200-x-200-voegstenen': KeuzelijstWaarde(invulwaarde='200-x-200-voegstenen',
                                                 label='200 x 200 voegstenen',
                                                 status='ingebruik',
                                                 definitie='200 x 200 voegstenen',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/200-x-200-voegstenen'),
        '220-x-110': KeuzelijstWaarde(invulwaarde='220-x-110',
                                      label='220 x 110',
                                      status='ingebruik',
                                      definitie='220 x 110',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/220-x-110'),
        '220-x-220': KeuzelijstWaarde(invulwaarde='220-x-220',
                                      label='220 x 220',
                                      status='ingebruik',
                                      definitie='220 x 220',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/220-x-220'),
        '220-x-220-voegstenen': KeuzelijstWaarde(invulwaarde='220-x-220-voegstenen',
                                                 label='220 x 220 voegstenen',
                                                 status='ingebruik',
                                                 definitie='220 x 220 voegstenen',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/220-x-220-voegstenen'),
        '300-x-300': KeuzelijstWaarde(invulwaarde='300-x-300',
                                      label='300 x 300',
                                      status='ingebruik',
                                      definitie='300 x 300',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/300-x-300'),
        '400-x-400': KeuzelijstWaarde(invulwaarde='400-x-400',
                                      label='400 x 400',
                                      status='ingebruik',
                                      definitie='400 x 400',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/400-x-400'),
        '500-x-500': KeuzelijstWaarde(invulwaarde='500-x-500',
                                      label='500 x 500',
                                      status='ingebruik',
                                      definitie='500 x 500',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/500-x-500'),
        '600-x-600': KeuzelijstWaarde(invulwaarde='600-x-600',
                                      label='600 x 600',
                                      status='ingebruik',
                                      definitie='600 x 600',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/600-x-600'),
        '800-x-800': KeuzelijstWaarde(invulwaarde='800-x-800',
                                      label='800 x 800',
                                      status='ingebruik',
                                      definitie='800 x 800',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/800-x-800'),
        'afmetingen-volgens-de-opdrachtdocumenten': KeuzelijstWaarde(invulwaarde='afmetingen-volgens-de-opdrachtdocumenten',
                                                                     label='afmetingen volgens de opdrachtdocumenten',
                                                                     status='ingebruik',
                                                                     definitie='afmetingen volgens de opdrachtdocumenten',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingselementAfmetingLxB/afmetingen-volgens-de-opdrachtdocumenten')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

