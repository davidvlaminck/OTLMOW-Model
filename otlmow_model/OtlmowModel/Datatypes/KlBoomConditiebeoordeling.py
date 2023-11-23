# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomConditiebeoordeling(KeuzelijstField):
    """De conditie beoordeeld volgens de kronenstructuur van Dr. A. Roloff, gelet op de scheutlengte ontwikkeling en vorming van dood hout."""
    naam = 'KlBoomConditiebeoordeling'
    label = 'Boom conditiebeoordeling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomConditiebeoordeling'
    definition = 'De conditie beoordeeld volgens de kronenstructuur van Dr. A. Roloff, gelet op de scheutlengte ontwikkeling en vorming van dood hout.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomConditiebeoordeling'
    options = {
        '0': KeuzelijstWaarde(invulwaarde='0',
                              label='0',
                              status='ingebruik',
                              definitie='De conditie is goed. Op middellange termijn (10 tot 15 jaar) worden geen problemen verwacht.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiebeoordeling/0'),
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='ingebruik',
                              definitie='De conditie is verminderd, maar op korte termijn (< 5 jaar) worden ten aanzien van de fysiologische toestand van de boom geen problemen verwacht.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiebeoordeling/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              definitie='De conditie is duidelijk verminderd. De fysiologische toestand van de boom is slecht, maar herstel van de boom is eventueel mogelijk.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiebeoordeling/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              status='ingebruik',
                              definitie="De conditie en toekomstverwachting van de boom is minimaal. De mechanische en/of fysiologische toestand van de boom is dusdanig slecht dat 'herstel' van de boom niet of nauwelijks mogelijk is.",
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiebeoordeling/3')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

