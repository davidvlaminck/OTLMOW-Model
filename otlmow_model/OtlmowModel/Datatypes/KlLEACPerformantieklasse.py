# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACPerformantieklasse(KeuzelijstField):
    """De verschillende performantieklasses van de geteste beginconstructie."""
    naam = 'KlLEACPerformantieklasse'
    label = 'Performantieklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACPerformantieklasse'
    definition = 'De verschillende performantieklasses van de geteste beginconstructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACPerformantieklasse'
    options = {
        'P1': KeuzelijstWaarde(invulwaarde='P1',
                               label='P1',
                               status='ingebruik',
                               definitie='Beginconstructie enkel frontaal getest met een lichte wagen aan 80km/h',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/P1'),
        'P2': KeuzelijstWaarde(invulwaarde='P2',
                               label='P2',
                               status='ingebruik',
                               definitie='Beginconstructie zowel frontaal als zijwaarts getest, met een lichte en kleine gezinswagen aan 80km/h',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/P2'),
        'P3': KeuzelijstWaarde(invulwaarde='P3',
                               label='P3',
                               status='ingebruik',
                               definitie='Beginconstructie zowel frontaal als zijwaarts getest, met een lichte en kleine gezinswagen aan 100km/h',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/P3'),
        'P4': KeuzelijstWaarde(invulwaarde='P4',
                               label='P4',
                               status='ingebruik',
                               definitie='Beginconstructie zowel frontaal als zijwaarts getest, met een lichte en grote gezinswagen aan 110km/h',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/P4'),
        't100': KeuzelijstWaarde(invulwaarde='t100',
                                 label='T100',
                                 status='ingebruik',
                                 definitie='Beginconstructie zowel frontaal als zijwaarts getest, met een lichte en kleine gezinswagen aan 100km/h, maar er zijn meer testen dan P3.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/t100'),
        't110': KeuzelijstWaarde(invulwaarde='t110',
                                 label='T110',
                                 status='ingebruik',
                                 definitie='Beginconstructie zowel frontaal als zijwaarts getest, met een lichte en grote gezinswagen aan 100 of 110km/h , maar er zijn meer testen dan P4.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/t110'),
        't50': KeuzelijstWaarde(invulwaarde='t50',
                                label='T50',
                                status='ingebruik',
                                definitie='Beginconstructie enkel frontaal getest met een lichte wagen aan 50km/h.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/t50'),
        't80': KeuzelijstWaarde(invulwaarde='t80',
                                label='T80',
                                status='ingebruik',
                                definitie='Beginconstructie zowel frontaal als zijwaarts getest, met een lichte en kleine gezinswagen aan 80km/h, maar er zijn meer testen dan P2.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/t80'),
        't80-1': KeuzelijstWaarde(invulwaarde='t80-1',
                                  label='T80/1',
                                  status='ingebruik',
                                  definitie='Beginconstructie zowel beperkt frontaal als zijwaarts getest, met een lichte en kleine gezinswagen aan 80km/h, maar er zijn minder testen dan T80, maar meer dan P2 en P1.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACPerformantieklasse/t80-1')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

