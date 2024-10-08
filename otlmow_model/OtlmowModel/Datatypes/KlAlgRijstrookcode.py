# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgRijstrookcode(KeuzelijstField):
    """Lijst van rijstrookcodes."""
    naam = 'KlAlgRijstrookcode'
    label = 'Algemeen rijstrookcode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlAlgRijstrookcode'
    definition = 'Lijst van rijstrookcodes.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgRijstrookcode'
    options = {
        '0': KeuzelijstWaarde(invulwaarde='0',
                              label='0',
                              status='ingebruik',
                              definitie='pechstrook of BOB (Bijzondere Overrijdbare Bedding)',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijstrookcode/0'),
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='ingebruik',
                              definitie='meest rechtse rijstrook',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijstrookcode/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              definitie='tweede rijstrook van rechts te tellen',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijstrookcode/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              status='ingebruik',
                              definitie='derde rijstrook van rechts te tellen',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijstrookcode/3'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='4',
                              status='ingebruik',
                              definitie='vierde rijstrook van rechts te tellen',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijstrookcode/4'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              status='ingebruik',
                              definitie='vijfde rijstrook van rechts te tellen',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijstrookcode/5'),
        '6': KeuzelijstWaarde(invulwaarde='6',
                              label='6',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijstrookcode/6'),
        '7': KeuzelijstWaarde(invulwaarde='7',
                              label='7',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijstrookcode/7'),
        '8': KeuzelijstWaarde(invulwaarde='8',
                              label='8',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijstrookcode/8'),
        '9': KeuzelijstWaarde(invulwaarde='9',
                              label='9',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgRijstrookcode/9')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

