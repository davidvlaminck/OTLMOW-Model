# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOphogingSoorten(KeuzelijstField):
    """De specificatie van type grond bij ophoging."""
    naam = 'KlOphogingSoorten'
    label = 'Ophoging soorten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlOphogingSoorten'
    definition = 'De specificatie van type grond bij ophoging.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOphogingSoorten'
    options = {
        'in-den-droge': KeuzelijstWaarde(invulwaarde='in-den-droge',
                                         label='in den droge',
                                         status='ingebruik',
                                         definitie='Het droog grondverzet heeft tot doel het baanbed, de wegbermen, de steunbermen, de taluds en de sloten te verwezenlijken.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOphogingSoorten/in-den-droge'),
        'onbevaarbare-waterlopen': KeuzelijstWaarde(invulwaarde='onbevaarbare-waterlopen',
                                                    label='onbevaarbare waterlopen',
                                                    status='ingebruik',
                                                    definitie='Het grondwerk aan deze waterlopen heeft tot doel de bedding, ondervlak, taluds, dijken, ontwateringssloten en bermen te verwezenlijken.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOphogingSoorten/onbevaarbare-waterlopen'),
        'strandzand': KeuzelijstWaarde(invulwaarde='strandzand',
                                       label='strandzand',
                                       status='ingebruik',
                                       definitie='Zand afkomstig van zones gelegen rechtover de op te hogen strandzones vanaf peil (TAW + 2,5 m) tot tegen de waterlijn.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOphogingSoorten/strandzand'),
        'zeezand': KeuzelijstWaarde(invulwaarde='zeezand',
                                    label='zeezand',
                                    status='ingebruik',
                                    definitie='Zand gebaggerd op de consessie van de Vlaamse overheid, of de consessie van de opdrachtnemer.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOphogingSoorten/zeezand')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

