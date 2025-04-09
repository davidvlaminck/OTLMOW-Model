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
                                         definitie='Glas dat meestal door middel van warmte in een specifieke kromming of gebogen vorm is gebracht.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/gebogen-glas'),
        'gebogen-polycarbonaat': KeuzelijstWaarde(invulwaarde='gebogen-polycarbonaat',
                                                  label='gebogen polycarbonaat',
                                                  status='ingebruik',
                                                  definitie='Polycarbonaat dat door middel van warmte en/of mechanische druk in een gebogen of gebogen vorm werd gebracht.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/gebogen-polycarbonaat'),
        'polycarbonaat': KeuzelijstWaarde(invulwaarde='polycarbonaat',
                                          label='polycarbonaat',
                                          status='ingebruik',
                                          definitie='Een sterke, transparante en slagvaste kunststof die bekend staat om zijn hoge duurzaamheid. ',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/polycarbonaat'),
        'vlak-glas': KeuzelijstWaarde(invulwaarde='vlak-glas',
                                      label='vlak glas',
                                      status='ingebruik',
                                      definitie='Glas zonder vervormingen of krommingen.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedProtector/vlak-glas')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

