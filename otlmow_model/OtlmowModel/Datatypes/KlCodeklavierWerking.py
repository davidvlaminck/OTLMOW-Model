# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCodeklavierWerking(KeuzelijstField):
    """Een keuzelijst met werkingsprincipes van een codeklavier."""
    naam = 'KlCodeklavierWerking'
    label = 'Codeklavier werking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCodeklavierWerking'
    definition = 'Een keuzelijst met werkingsprincipes van een codeklavier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCodeklavierWerking'
    options = {
        'cijfercodeslot': KeuzelijstWaarde(invulwaarde='cijfercodeslot',
                                           label='cijfercodeslot',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCodeklavierWerking/cijfercodeslot'),
        'cijfercodeslot-met-drukknop': KeuzelijstWaarde(invulwaarde='cijfercodeslot-met-drukknop',
                                                        label='cijfercodeslot met drukknop',
                                                        status='ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCodeklavierWerking/cijfercodeslot-met-drukknop'),
        'drukknop': KeuzelijstWaarde(invulwaarde='drukknop',
                                     label='drukknop',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCodeklavierWerking/drukknop')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

