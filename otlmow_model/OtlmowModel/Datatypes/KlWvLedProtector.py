# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedProtector(KeuzelijstField):
    """Type doorschijnende kap ter bescherming van de LED's (vlak glas, polycarbonaat,...)."""
    naam = 'KlWvLedProtector'
    label = 'WV protector'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedProtector'
    definition = "Type doorschijnende kap ter bescherming van de LED's (vlak glas, polycarbonaat,...)."
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedProtector'
    options = {
        'gebogen-glas': KeuzelijstWaarde(invulwaarde='gebogen-glas',
                                         label='gebogen glas',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/gebogen-glas'),
        'polycarbonaat': KeuzelijstWaarde(invulwaarde='polycarbonaat',
                                          label='polycarbonaat',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/polycarbonaat'),
        'vlak-glas': KeuzelijstWaarde(invulwaarde='vlak-glas',
                                      label='vlak glas',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/vlak-glas')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

