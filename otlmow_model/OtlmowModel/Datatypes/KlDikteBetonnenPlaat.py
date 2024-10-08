# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDikteBetonnenPlaat(KeuzelijstField):
    """De dikte van de betonnen plaat, opgedeeld in categorieën."""
    naam = 'KlDikteBetonnenPlaat'
    label = 'Dikte betonnen plaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDikteBetonnenPlaat'
    definition = 'De dikte van de betonnen plaat, opgedeeld in categorieën.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDikteBetonnenPlaat'
    options = {
        'groter-dan-1000mm': KeuzelijstWaarde(invulwaarde='groter-dan-1000mm',
                                              label='Groter dan 1000mm',
                                              status='ingebruik',
                                              definitie='De dikte van de betonnen plaat is groter dan 1000 millimeter.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDikteBetonnenPlaat/groter-dan-1000mm'),
        'kleiner-of-gelijk-aan-300mm': KeuzelijstWaarde(invulwaarde='kleiner-of-gelijk-aan-300mm',
                                                        label='Kleiner of gelijk aan 300mm',
                                                        status='ingebruik',
                                                        definitie='De dikte van de betonnen plaat is kleiner of gelijk aan 300 millimeter.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDikteBetonnenPlaat/kleiner-of-gelijk-aan-300mm'),
        'tussen-300mm-en-of-gelijk-aan-600mm': KeuzelijstWaarde(invulwaarde='tussen-300mm-en-of-gelijk-aan-600mm',
                                                                label='Tussen 300mm en/of gelijk aan 600mm',
                                                                status='ingebruik',
                                                                definitie='De dikte van de betonnen plaat is tussen 300 millimeter en/of gelijk aan 600 millimeter.',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDikteBetonnenPlaat/tussen-300mm-en-of-gelijk-aan-600mm'),
        'tussen-600mm-en-of-gelijk-aan-1000mm': KeuzelijstWaarde(invulwaarde='tussen-600mm-en-of-gelijk-aan-1000mm',
                                                                 label='Tussen 600mm en/of gelijk aan 1000mm',
                                                                 status='ingebruik',
                                                                 definitie='De dikte van de betonnen plaat is tussen 600 millimeter en/of gelijk aan 1000 millimeter.',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDikteBetonnenPlaat/tussen-600mm-en-of-gelijk-aan-1000mm')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

