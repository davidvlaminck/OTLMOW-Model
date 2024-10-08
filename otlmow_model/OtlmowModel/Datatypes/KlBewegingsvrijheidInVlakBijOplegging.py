# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBewegingsvrijheidInVlakBijOplegging(KeuzelijstField):
    """De bewegingsvrijheid in het vlak bij een oplegging."""
    naam = 'KlBewegingsvrijheidInVlakBijOplegging'
    label = 'Bewegingsvrijheid in vlak bij oplegging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBewegingsvrijheidInVlakBijOplegging'
    definition = 'De bewegingsvrijheid in het vlak bij een oplegging.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBewegingsvrijheidInVlakBijOplegging'
    options = {
        'alzijdig-beweegbaar': KeuzelijstWaarde(invulwaarde='alzijdig-beweegbaar',
                                                label='alzijdig beweegbaar',
                                                status='ingebruik',
                                                definitie='alzijdig beweegbaar',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBewegingsvrijheidInVlakBijOplegging/alzijdig-beweegbaar'),
        'dwars-beweegbaar': KeuzelijstWaarde(invulwaarde='dwars-beweegbaar',
                                             label='dwars beweegbaar',
                                             status='ingebruik',
                                             definitie='dwars beweegbaar',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBewegingsvrijheidInVlakBijOplegging/dwars-beweegbaar'),
        'langs-beweegbaar': KeuzelijstWaarde(invulwaarde='langs-beweegbaar',
                                             label='langs beweegbaar',
                                             status='ingebruik',
                                             definitie='langs beweegbaar',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBewegingsvrijheidInVlakBijOplegging/langs-beweegbaar'),
        'vast': KeuzelijstWaarde(invulwaarde='vast',
                                 label='vast',
                                 status='ingebruik',
                                 definitie='vast',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBewegingsvrijheidInVlakBijOplegging/vast')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

