# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSleufUitvoering(KeuzelijstField):
    """Uitvoeringen van de sleuf."""
    naam = 'KlSleufUitvoering'
    label = 'Sleuf uitvoering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSleufUitvoering'
    definition = 'Uitvoeringen van de sleuf.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSleufUitvoering'
    options = {
        'beschoeide-sleuf': KeuzelijstWaarde(invulwaarde='beschoeide-sleuf',
                                             label='beschoeide sleuf',
                                             status='ingebruik',
                                             definitie='beschoeide sleuf',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/beschoeide-sleuf'),
        'beschoeide-sleuf-met-voorafgraving': KeuzelijstWaarde(invulwaarde='beschoeide-sleuf-met-voorafgraving',
                                                               label='beschoeide sleuf met voorafgraving',
                                                               status='ingebruik',
                                                               definitie='beschoeide sleuf met voorafgraving',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/beschoeide-sleuf-met-voorafgraving'),
        'directional-drilling': KeuzelijstWaarde(invulwaarde='directional-drilling',
                                                 label='directional drilling',
                                                 status='ingebruik',
                                                 definitie='directional drilling',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/directional-drilling'),
        'onderdoorpersing': KeuzelijstWaarde(invulwaarde='onderdoorpersing',
                                             label='onderdoorpersing',
                                             status='ingebruik',
                                             definitie='onderdoorpersing',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/onderdoorpersing'),
        'open-sleuf': KeuzelijstWaarde(invulwaarde='open-sleuf',
                                       label='open sleuf',
                                       status='ingebruik',
                                       definitie='open sleuf',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/open-sleuf'),
        'waterdicht-beschoeide-sleuf-met-damplanken': KeuzelijstWaarde(invulwaarde='waterdicht-beschoeide-sleuf-met-damplanken',
                                                                       label='waterdicht beschoeide sleuf met damplanken',
                                                                       status='ingebruik',
                                                                       definitie='waterdicht beschoeide sleuf met damplanken',
                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSleufUitvoering/waterdicht-beschoeide-sleuf-met-damplanken')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

