# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLichtmastAantArmen(KeuzelijstField):
    """Aantal armen van de lichtmast."""
    naam = 'KlWvLichtmastAantArmen'
    label = 'WV-mast aantal armen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastAantArmen'
    definition = 'Aantal armen van de lichtmast.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLichtmastAantArmen'
    options = {
        '0': KeuzelijstWaarde(invulwaarde='0',
                              label='0',
                              status='ingebruik',
                              definitie="keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST",
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/0'),
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='ingebruik',
                              definitie="keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST",
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              definitie="keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST",
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              status='ingebruik',
                              definitie="keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST",
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/3'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='4',
                              status='ingebruik',
                              definitie="keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST",
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/4')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

