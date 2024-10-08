# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrondherkomst(KeuzelijstField):
    """De herkomst van de grond."""
    naam = 'KlGrondherkomst'
    label = 'Grondherkomst'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlGrondherkomst'
    definition = 'De herkomst van de grond.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrondherkomst'
    options = {
        'aanbestedende-overheid': KeuzelijstWaarde(invulwaarde='aanbestedende-overheid',
                                                   label='aanbestedende overheid',
                                                   status='ingebruik',
                                                   definitie='Grond aan te leveren door de aanbestedende overheid.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondherkomst/aanbestedende-overheid'),
        'ander-project': KeuzelijstWaarde(invulwaarde='ander-project',
                                          label='ander project',
                                          status='ingebruik',
                                          definitie='Grond afkomstig van een ander project.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondherkomst/ander-project'),
        'de-aannemer': KeuzelijstWaarde(invulwaarde='de-aannemer',
                                        label='de aannemer',
                                        status='ingebruik',
                                        definitie='Grond geleverd door de aannemer.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondherkomst/de-aannemer'),
        'gezeefde-gronden': KeuzelijstWaarde(invulwaarde='gezeefde-gronden',
                                             label='gezeefde gronden',
                                             status='ingebruik',
                                             definitie='Gezeefde gronden afkomstig van zones met invasieve duizendknoop.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondherkomst/gezeefde-gronden'),
        'werfzone': KeuzelijstWaarde(invulwaarde='werfzone',
                                     label='werfzone',
                                     status='ingebruik',
                                     definitie='Grond afkomstig van binnen de werfzone.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondherkomst/werfzone')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

