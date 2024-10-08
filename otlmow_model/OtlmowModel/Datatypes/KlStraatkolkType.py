# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStraatkolkType(KeuzelijstField):
    """Types van straatkolk."""
    naam = 'KlStraatkolkType'
    label = 'Straatkolk type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStraatkolkType'
    definition = 'Types van straatkolk.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStraatkolkType'
    options = {
        'geisoleerd': KeuzelijstWaarde(invulwaarde='geisoleerd',
                                       label='geisoleerd',
                                       status='ingebruik',
                                       definitie='Een straatkolk die niet in een rij geplaatst werd maar bijvoorbeeld ergens solitair op een plein.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkType/geisoleerd'),
        'horizontaal': KeuzelijstWaarde(invulwaarde='horizontaal',
                                        label='horizontaal',
                                        status='ingebruik',
                                        definitie='Een gietijzeren rooster met horizontale afvoeropening dat op regelmatige afstand geplaatst wordt langs of in een weg, fietspad of voetpad.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkType/horizontaal'),
        'verticaal': KeuzelijstWaarde(invulwaarde='verticaal',
                                      label='verticaal',
                                      status='ingebruik',
                                      definitie='Verticale afvoeropening die op regelmatige afstand geplaatst wordt langs of in een boordsteen van de weg, fietspad of voetpad.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkType/verticaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

