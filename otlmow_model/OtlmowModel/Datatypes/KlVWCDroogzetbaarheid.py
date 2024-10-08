# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVWCDroogzetbaarheid(KeuzelijstField):
    """Geeft aan of het constructiefhoofd al dan niet droog gezet kan worden."""
    naam = 'KlVWCDroogzetbaarheid'
    label = 'Droogzetbaarheidtypes'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlVWCDroogzetbaarheid'
    definition = 'Geeft aan of het constructiefhoofd al dan niet droog gezet kan worden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVWCDroogzetbaarheid'
    options = {
        'enkel-deurkamer-droogzetbaar': KeuzelijstWaarde(invulwaarde='enkel-deurkamer-droogzetbaar',
                                                         label='enkel deurkamer droogzetbaar',
                                                         status='ingebruik',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVWCDroogzetbaarheid/enkel-deurkamer-droogzetbaar'),
        'gedeeltelijke-waterpeilverlaging': KeuzelijstWaarde(invulwaarde='gedeeltelijke-waterpeilverlaging',
                                                             label='gedeeltelijke waterpeilverlaging',
                                                             status='ingebruik',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVWCDroogzetbaarheid/gedeeltelijke-waterpeilverlaging'),
        'niet-droogzetbaar': KeuzelijstWaarde(invulwaarde='niet-droogzetbaar',
                                              label='niet droogzetbaar',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVWCDroogzetbaarheid/niet-droogzetbaar'),
        'volledig-droogzetbaar': KeuzelijstWaarde(invulwaarde='volledig-droogzetbaar',
                                                  label='volledig droogzetbaar',
                                                  status='ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVWCDroogzetbaarheid/volledig-droogzetbaar')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

