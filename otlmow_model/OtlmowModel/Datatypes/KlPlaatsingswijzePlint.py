# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlaatsingswijzePlint(KeuzelijstField):
    """De manier waarop de plint geplaatst is ten opzichte van de profielen."""
    naam = 'KlPlaatsingswijzePlint'
    label = 'Plaatsingswijze plint'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlaatsingswijzePlint'
    definition = 'De manier waarop de plint geplaatst is ten opzichte van de profielen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlaatsingswijzePlint'
    options = {
        'bevestigd-tegen-de-profielen': KeuzelijstWaarde(invulwaarde='bevestigd-tegen-de-profielen',
                                                         label='bevestigd tegen de profielen',
                                                         status='ingebruik',
                                                         definitie='bevestigd tegen de profielen',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingswijzePlint/bevestigd-tegen-de-profielen'),
        'geschoven-tussen-de-profielen': KeuzelijstWaarde(invulwaarde='geschoven-tussen-de-profielen',
                                                          label='geschoven tussen de profielen',
                                                          status='ingebruik',
                                                          definitie='geschoven tussen de profielen',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingswijzePlint/geschoven-tussen-de-profielen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

