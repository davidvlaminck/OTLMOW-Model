# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomConditiewaarde(KeuzelijstField):
    """De verschillende conditiewaardes voor een boom."""
    naam = 'KlBoomConditiewaarde'
    label = 'Boom conditiewaarde'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomConditiewaarde'
    definition = 'De verschillende conditiewaardes voor een boom.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomConditiewaarde'
    options = {
        '0': KeuzelijstWaarde(invulwaarde='0',
                              label='0',
                              status='ingebruik',
                              definitie='Dode boom',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0'),
        '0.1': KeuzelijstWaarde(invulwaarde='0.1',
                                label='0.1',
                                status='ingebruik',
                                definitie='Bijna dode boom',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.1'),
        '0.2': KeuzelijstWaarde(invulwaarde='0.2',
                                label='0.2',
                                status='ingebruik',
                                definitie='kwijnende boom met zeer slechte conditie die binnen een periode van 2 jaar kan afsterven',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.2'),
        '0.3': KeuzelijstWaarde(invulwaarde='0.3',
                                label='0.3',
                                status='ingebruik',
                                definitie='kwijnende boom met zeer slechte conditie die binnen een periode van 3 jaar kan afsterven',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.3'),
        '0.4': KeuzelijstWaarde(invulwaarde='0.4',
                                label='0.4',
                                status='ingebruik',
                                definitie='kwijnende boom met een slechte conditie die binnen een periode van 4 jaar kan afsterven',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.4'),
        '0.5': KeuzelijstWaarde(invulwaarde='0.5',
                                label='0.5',
                                status='ingebruik',
                                definitie='kwijnende boom met een slechte conditie die binnen een periode van 5-6 jaar kan afsterven',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.5'),
        '0.6': KeuzelijstWaarde(invulwaarde='0.6',
                                label='0.6',
                                status='ingebruik',
                                definitie='Boom in matige conditie voor zijn levensfase (bladbezetting, knopzetting, scheutlengte, kroonarchitectuur, …) EN/OF aanzienlijke schade of aantastingen aan stam, gesteltakken of wortels EN/OF matige levensverwachting.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.6'),
        '0.7': KeuzelijstWaarde(invulwaarde='0.7',
                                label='0.7',
                                status='ingebruik',
                                definitie='Boom in goede conditie voor zijn levensfase (bladbezetting, knopzetting, scheutlengte, kroonarchitectuur, …) EN/OF beperkte schade of aantastingen aan stam, gesteltakken of wortels EN/OF goede levensverwachting op middellange termijn.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.7'),
        '0.8': KeuzelijstWaarde(invulwaarde='0.8',
                                label='0.8',
                                status='ingebruik',
                                definitie='Boom in goede conditie voor zijn levensfase (bladbezetting, knopzetting, scheutlengte, kroonarchitectuur, …) EN/OF beperkte schade of aantastingen aan stam, gesteltakken of wortels EN/OF goede levensverwachting op middellange termijn.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.8'),
        '0.9': KeuzelijstWaarde(invulwaarde='0.9',
                                label='0.9',
                                status='ingebruik',
                                definitie='Boom in goede conditie voor zijn levensfase (bladbezetting, knopzetting, scheutlengte, kroonarchitectuur, …) EN/OF beperkte schade of aantastingen aan stam, gesteltakken of wortels EN/OF goede levensverwachting op middellange termijn.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.9'),
        '1.0': KeuzelijstWaarde(invulwaarde='1.0',
                                label='1.0',
                                status='ingebruik',
                                definitie='kerngezonde boom die voldoet aan alle vereisten wat gezondheid, levensverwachting, esthetisch aanzien en vormgeving betreft',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/1.0')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

