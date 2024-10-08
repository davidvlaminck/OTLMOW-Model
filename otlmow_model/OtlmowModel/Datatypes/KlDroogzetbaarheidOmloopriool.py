# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDroogzetbaarheidOmloopriool(KeuzelijstField):
    """De keuzelijst die de verschillende manieren van droogzetbaarheid van de omloopriool bevat."""
    naam = 'KlDroogzetbaarheidOmloopriool'
    label = 'Keuzelijst droogzetbaarheid omloopriool'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlDroogzetbaarheidOmloopriool'
    definition = 'De keuzelijst die de verschillende manieren van droogzetbaarheid van de omloopriool bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDroogzetbaarheidOmloopriool'
    options = {
        'gedeeltelijke-droogzetbaar-enkel-t.p.v.-schuif': KeuzelijstWaarde(invulwaarde='gedeeltelijke-droogzetbaar-enkel-t.p.v.-schuif',
                                                                           label='gedeeltelijke droogzetbaar enkel t.p.v. schuif',
                                                                           status='ingebruik',
                                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDroogzetbaarheidOmloopriool/gedeeltelijke-droogzetbaar-enkel-t.p.v.-schuif'),
        'gedeeltelijke-droogzetbaar-in-combinatie-met-hoofd': KeuzelijstWaarde(invulwaarde='gedeeltelijke-droogzetbaar-in-combinatie-met-hoofd',
                                                                               label='gedeeltelijke droogzetbaar in combinatie met hoofd',
                                                                               status='ingebruik',
                                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDroogzetbaarheidOmloopriool/gedeeltelijke-droogzetbaar-in-combinatie-met-hoofd'),
        'gedeeltelijke-waterpeilverlaging': KeuzelijstWaarde(invulwaarde='gedeeltelijke-waterpeilverlaging',
                                                             label='gedeeltelijke waterpeilverlaging',
                                                             status='ingebruik',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDroogzetbaarheidOmloopriool/gedeeltelijke-waterpeilverlaging'),
        'niet-droogzetbaar': KeuzelijstWaarde(invulwaarde='niet-droogzetbaar',
                                              label='niet droogzetbaar',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDroogzetbaarheidOmloopriool/niet-droogzetbaar'),
        'volledig-droogzetbaar': KeuzelijstWaarde(invulwaarde='volledig-droogzetbaar',
                                                  label='volledig droogzetbaar',
                                                  status='ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDroogzetbaarheidOmloopriool/volledig-droogzetbaar')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

