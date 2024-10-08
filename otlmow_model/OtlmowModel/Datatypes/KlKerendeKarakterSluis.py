# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKerendeKarakterSluis(KeuzelijstField):
    """De verschillende kerende karakters van een sluis."""
    naam = 'KlKerendeKarakterSluis'
    label = 'Kerende karakter van een sluis'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlKerendeKarakterSluis'
    definition = 'De verschillende kerende karakters van een sluis.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKerendeKarakterSluis'
    options = {
        'dubbel': KeuzelijstWaarde(invulwaarde='dubbel',
                                   label='dubbel',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKerendeKarakterSluis/dubbel'),
        'enkel': KeuzelijstWaarde(invulwaarde='enkel',
                                  label='enkel',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKerendeKarakterSluis/enkel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

