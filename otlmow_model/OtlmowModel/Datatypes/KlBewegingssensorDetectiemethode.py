# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBewegingssensorDetectiemethode(KeuzelijstField):
    """De methode waarvolgens de detectie gebeurt."""
    naam = 'KlBewegingssensorDetectiemethode'
    label = 'Bewegingssensor detectiemethode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBewegingssensorDetectiemethode'
    definition = 'De methode waarvolgens de detectie gebeurt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBewegingssensorDetectiemethode'
    options = {
        'actief-infrarood-(air)': KeuzelijstWaarde(invulwaarde='actief-infrarood-(air)',
                                                   label='actief infrarood (AIR)',
                                                   status='ingebruik',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBewegingssensorDetectiemethode/actief-infrarood-(air)'),
        'microgolven-(hf)': KeuzelijstWaarde(invulwaarde='microgolven-(hf)',
                                             label='microgolven (HF)',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBewegingssensorDetectiemethode/microgolven-(hf)'),
        'passief-infrarood-(pir)': KeuzelijstWaarde(invulwaarde='passief-infrarood-(pir)',
                                                    label='passief infrarood (PIR)',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBewegingssensorDetectiemethode/passief-infrarood-(pir)')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

