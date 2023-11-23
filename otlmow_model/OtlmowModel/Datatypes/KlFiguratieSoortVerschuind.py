# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFiguratieSoortVerschuind(KeuzelijstField):
    """Soorten van verschuinde figuratie markering."""
    naam = 'KlFiguratieSoortVerschuind'
    label = 'Figuratie soort verschuind'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieSoortVerschuind'
    definition = 'Soorten van verschuinde figuratie markering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieSoortVerschuind'
    options = {
        'letterfiguratiemarkering(schuin)': KeuzelijstWaarde(invulwaarde='letterfiguratiemarkering(schuin)',
                                                             label='letterfiguratiemarkering(schuin)',
                                                             status='ingebruik',
                                                             definitie='Een schuine lettermarking als figuratie zoals BUS, TAXI, TRAM,....',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoortVerschuind/letterfiguratiemarkering(schuin)'),
        'omgekeerde-driehoek(schuin)': KeuzelijstWaarde(invulwaarde='omgekeerde-driehoek(schuin)',
                                                        label='omgekeerde driehoek(schuin)',
                                                        status='ingebruik',
                                                        definitie='Een schuine omgekeerde driehoek markering.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoortVerschuind/omgekeerde-driehoek(schuin)')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

