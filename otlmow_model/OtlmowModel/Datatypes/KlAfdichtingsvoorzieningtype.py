# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfdichtingsvoorzieningtype(KeuzelijstField):
    """De mogelijke types van een afdichtingsvoorziening."""
    naam = 'KlAfdichtingsvoorzieningtype'
    label = 'Afdichtingsvoorzieningtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfdichtingsvoorzieningtype'
    definition = 'De mogelijke types van een afdichtingsvoorziening.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfdichtingsvoorzieningtype'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfdichtingsvoorzieningtype/andere'),
        'd-fender': KeuzelijstWaarde(invulwaarde='d-fender',
                                     label='d-fender',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfdichtingsvoorzieningtype/d-fender'),
        'gina-profiel': KeuzelijstWaarde(invulwaarde='gina-profiel',
                                         label='gina-profiel',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfdichtingsvoorzieningtype/gina-profiel'),
        'hoekprofiel': KeuzelijstWaarde(invulwaarde='hoekprofiel',
                                        label='hoekprofiel',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfdichtingsvoorzieningtype/hoekprofiel'),
        'muzieknoot-met-dubbelzijdige-bevestiging': KeuzelijstWaarde(invulwaarde='muzieknoot-met-dubbelzijdige-bevestiging',
                                                                     label='muzieknoot met dubbelzijdige bevestiging',
                                                                     status='ingebruik',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfdichtingsvoorzieningtype/muzieknoot-met-dubbelzijdige-bevestiging'),
        'muzieknoot-met-enkelzijdigde-bevestiging': KeuzelijstWaarde(invulwaarde='muzieknoot-met-enkelzijdigde-bevestiging',
                                                                     label='muzieknoot met enkelzijdigde bevestiging',
                                                                     status='ingebruik',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfdichtingsvoorzieningtype/muzieknoot-met-enkelzijdigde-bevestiging'),
        'omega': KeuzelijstWaarde(invulwaarde='omega',
                                  label='omega',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfdichtingsvoorzieningtype/omega'),
        'rubberflap': KeuzelijstWaarde(invulwaarde='rubberflap',
                                       label='rubberflap',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfdichtingsvoorzieningtype/rubberflap')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

