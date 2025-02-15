# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedOverhang(KeuzelijstField):
    """Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan."""
    naam = 'KlWvLedOverhang'
    label = 'WV LED overhang'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedOverhang'
    definition = 'Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedOverhang'
    options = {
        '0': KeuzelijstWaarde(invulwaarde='0',
                              label='+0',
                              status='uitgebruik',
                              definitie='0',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/0'),
        '0-2': KeuzelijstWaarde(invulwaarde='0-2',
                                label='0',
                                status='ingebruik',
                                definitie='0-2',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/0-2'),
        '0-5': KeuzelijstWaarde(invulwaarde='0-5',
                                label='+0.5',
                                status='ingebruik',
                                definitie='0-5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/0-5'),
        '0-5-2': KeuzelijstWaarde(invulwaarde='0-5-2',
                                  label='-0.5',
                                  status='ingebruik',
                                  definitie='0-5-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/0-5-2'),
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='-1',
                              status='uitgebruik',
                              definitie='-1',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/1'),
        '1-0': KeuzelijstWaarde(invulwaarde='1-0',
                                label='+1.0',
                                status='ingebruik',
                                definitie='1-0',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/1-0'),
        '1-0-2': KeuzelijstWaarde(invulwaarde='1-0-2',
                                  label='-1.0',
                                  status='ingebruik',
                                  definitie='1-0-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/1-0-2'),
        '1-5': KeuzelijstWaarde(invulwaarde='1-5',
                                label='+1.5',
                                status='ingebruik',
                                definitie='1-5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/1-5'),
        '1-5-2': KeuzelijstWaarde(invulwaarde='1-5-2',
                                  label='-1.5',
                                  status='ingebruik',
                                  definitie='1-5-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/1-5-2'),
        '10-5': KeuzelijstWaarde(invulwaarde='10-5',
                                 label='-10.5',
                                 status='ingebruik',
                                 definitie='-10.5',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/10-5'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='-2',
                              status='uitgebruik',
                              definitie='-2',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/2'),
        '2-0': KeuzelijstWaarde(invulwaarde='2-0',
                                label='+2.0',
                                status='ingebruik',
                                definitie='2-0',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/2-0'),
        '2-0-2': KeuzelijstWaarde(invulwaarde='2-0-2',
                                  label='-2.0',
                                  status='ingebruik',
                                  definitie='2-0-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/2-0-2'),
        '2-5': KeuzelijstWaarde(invulwaarde='2-5',
                                label='+2.5',
                                status='ingebruik',
                                definitie='2-5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/2-5'),
        '2-5-2': KeuzelijstWaarde(invulwaarde='2-5-2',
                                  label='-2.5',
                                  status='ingebruik',
                                  definitie='2-5-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/2-5-2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='-3',
                              status='uitgebruik',
                              definitie='-3',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/3'),
        '3-0': KeuzelijstWaarde(invulwaarde='3-0',
                                label='+3.0',
                                status='ingebruik',
                                definitie='3-0',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/3-0'),
        '3-0-2': KeuzelijstWaarde(invulwaarde='3-0-2',
                                  label='-3.0',
                                  status='ingebruik',
                                  definitie='3-0-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/3-0-2'),
        '3-5': KeuzelijstWaarde(invulwaarde='3-5',
                                label='+3.5',
                                status='ingebruik',
                                definitie='3-5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/3-5'),
        '3-5-2': KeuzelijstWaarde(invulwaarde='3-5-2',
                                  label='-3.5',
                                  status='ingebruik',
                                  definitie='3-5-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/3-5-2'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='-4',
                              status='ingebruik',
                              definitie='4-0-2',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/4'),
        '4-2': KeuzelijstWaarde(invulwaarde='4-2',
                                label='+4',
                                status='ingebruik',
                                definitie='4-0',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/4-2'),
        '4-5': KeuzelijstWaarde(invulwaarde='4-5',
                                label='+4.5',
                                status='ingebruik',
                                definitie='4-5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/4-5'),
        '4-5-2': KeuzelijstWaarde(invulwaarde='4-5-2',
                                  label='-4.5',
                                  status='ingebruik',
                                  definitie='4-5-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/4-5-2'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='-5',
                              status='uitgebruik',
                              definitie='-5',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/5'),
        '5-0': KeuzelijstWaarde(invulwaarde='5-0',
                                label='+5.0',
                                status='ingebruik',
                                definitie='5-0',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/5-0'),
        '5-0-2': KeuzelijstWaarde(invulwaarde='5-0-2',
                                  label='-5.0',
                                  status='ingebruik',
                                  definitie='5-0-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/5-0-2'),
        '5-5': KeuzelijstWaarde(invulwaarde='5-5',
                                label='+5.5',
                                status='ingebruik',
                                definitie='5-5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/5-5'),
        '5-5-2': KeuzelijstWaarde(invulwaarde='5-5-2',
                                  label='-5.5',
                                  status='ingebruik',
                                  definitie='5-5-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/5-5-2'),
        '6-0': KeuzelijstWaarde(invulwaarde='6-0',
                                label='+6.0',
                                status='ingebruik',
                                definitie='6-0',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/6-0'),
        '6-0-2': KeuzelijstWaarde(invulwaarde='6-0-2',
                                  label='-6.0',
                                  status='ingebruik',
                                  definitie='6-0-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/6-0-2'),
        '6-5': KeuzelijstWaarde(invulwaarde='6-5',
                                label='+6.5',
                                status='ingebruik',
                                definitie='6-5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/6-5'),
        '6-5-2': KeuzelijstWaarde(invulwaarde='6-5-2',
                                  label='-6.5',
                                  status='ingebruik',
                                  definitie='6-5-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/6-5-2'),
        '7-0': KeuzelijstWaarde(invulwaarde='7-0',
                                label='+7.0',
                                status='ingebruik',
                                definitie='7-0',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/7-0'),
        '7-0-2': KeuzelijstWaarde(invulwaarde='7-0-2',
                                  label='-7.0',
                                  status='ingebruik',
                                  definitie='7-0-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/7-0-2'),
        '7-5': KeuzelijstWaarde(invulwaarde='7-5',
                                label='-7.5',
                                status='ingebruik',
                                definitie='-7.5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/7-5'),
        '7-5-2': KeuzelijstWaarde(invulwaarde='7-5-2',
                                  label='+7.5',
                                  status='ingebruik',
                                  definitie='7-5-2',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/7-5-2'),
        '8-5': KeuzelijstWaarde(invulwaarde='8-5',
                                label='-8.5',
                                status='ingebruik',
                                definitie='-8.5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/8-5'),
        '9-5': KeuzelijstWaarde(invulwaarde='9-5',
                                label='-9.5',
                                status='ingebruik',
                                definitie='-9.5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/9-5'),
        'o+0': KeuzelijstWaarde(invulwaarde='o+0',
                                label='o+0',
                                status='uitgebruik',
                                definitie='o+0',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+0'),
        'o+0.5': KeuzelijstWaarde(invulwaarde='o+0.5',
                                  label='o+0.5',
                                  status='uitgebruik',
                                  definitie='o+0,5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+0.5'),
        'o+1.5': KeuzelijstWaarde(invulwaarde='o+1.5',
                                  label='o+1.5',
                                  status='uitgebruik',
                                  definitie='o+1,5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+1.5'),
        'o+2.5': KeuzelijstWaarde(invulwaarde='o+2.5',
                                  label='o+2.5',
                                  status='uitgebruik',
                                  definitie='o+2.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+2.5'),
        'o+3.5': KeuzelijstWaarde(invulwaarde='o+3.5',
                                  label='o+3.5',
                                  status='uitgebruik',
                                  definitie='o+3,5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+3.5'),
        'o+4.5': KeuzelijstWaarde(invulwaarde='o+4.5',
                                  label='o+4.5',
                                  status='uitgebruik',
                                  definitie='o+4,5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o+4.5'),
        'o-0-5': KeuzelijstWaarde(invulwaarde='o-0-5',
                                  label='o-0.5',
                                  status='uitgebruik',
                                  definitie='o-0.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-0-5'),
        'o-1': KeuzelijstWaarde(invulwaarde='o-1',
                                label='o-1',
                                status='uitgebruik',
                                definitie='o-1',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-1'),
        'o-1-0': KeuzelijstWaarde(invulwaarde='o-1-0',
                                  label='o+1.0',
                                  status='uitgebruik',
                                  definitie='o+1.0',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-1-0'),
        'o-1-0-2': KeuzelijstWaarde(invulwaarde='o-1-0-2',
                                    label='o-1.0',
                                    status='uitgebruik',
                                    definitie='o-1.0',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-1-0-2'),
        'o-1-5': KeuzelijstWaarde(invulwaarde='o-1-5',
                                  label='o-1.5',
                                  status='uitgebruik',
                                  definitie='o-1.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-1-5'),
        'o-2': KeuzelijstWaarde(invulwaarde='o-2',
                                label='o-2',
                                status='uitgebruik',
                                definitie='o-2',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-2'),
        'o-2-5': KeuzelijstWaarde(invulwaarde='o-2-5',
                                  label='o-2.5',
                                  status='uitgebruik',
                                  definitie='o-2.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-2-5'),
        'o-3': KeuzelijstWaarde(invulwaarde='o-3',
                                label='o-3',
                                status='uitgebruik',
                                definitie='o-3.0',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-3'),
        'o-3-0': KeuzelijstWaarde(invulwaarde='o-3-0',
                                  label='o+3.0',
                                  status='uitgebruik',
                                  definitie='o+3.0',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-3-0'),
        'o-3-0-2': KeuzelijstWaarde(invulwaarde='o-3-0-2',
                                    label='o-3.0',
                                    status='uitgebruik',
                                    definitie='o-3.0',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-3-0-2'),
        'o-3-5': KeuzelijstWaarde(invulwaarde='o-3-5',
                                  label='o-3.5',
                                  status='uitgebruik',
                                  definitie='o-3.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-3-5'),
        'o-4': KeuzelijstWaarde(invulwaarde='o-4',
                                label='o-4',
                                status='uitgebruik',
                                definitie='o-4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-4'),
        'o-4-0': KeuzelijstWaarde(invulwaarde='o-4-0',
                                  label='o+4.0',
                                  status='uitgebruik',
                                  definitie='o+4.0',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-4-0'),
        'o-4-0-2': KeuzelijstWaarde(invulwaarde='o-4-0-2',
                                    label='o-4.0',
                                    status='uitgebruik',
                                    definitie='o-4.0',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-4-0-2'),
        'o-4-5': KeuzelijstWaarde(invulwaarde='o-4-5',
                                  label='o-4.5',
                                  status='uitgebruik',
                                  definitie='o-4.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-4-5'),
        'o-5': KeuzelijstWaarde(invulwaarde='o-5',
                                label='o-5',
                                status='uitgebruik',
                                definitie='o-5',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-5'),
        'o-5-0': KeuzelijstWaarde(invulwaarde='o-5-0',
                                  label='o+5.0',
                                  status='uitgebruik',
                                  definitie='o+5.0',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-5-0'),
        'o-5-0-2': KeuzelijstWaarde(invulwaarde='o-5-0-2',
                                    label='o-5.0',
                                    status='uitgebruik',
                                    definitie='o-5.0',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-5-0-2'),
        'o-5-5': KeuzelijstWaarde(invulwaarde='o-5-5',
                                  label='o+5.5',
                                  status='uitgebruik',
                                  definitie='o+5.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-5-5'),
        'o-5-5-2': KeuzelijstWaarde(invulwaarde='o-5-5-2',
                                    label='o-5.5',
                                    status='uitgebruik',
                                    definitie='o-5.5',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-5-5-2'),
        'o-6-0': KeuzelijstWaarde(invulwaarde='o-6-0',
                                  label='o+6.0',
                                  status='uitgebruik',
                                  definitie='o+6.0',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-6-0'),
        'o-6-0-2': KeuzelijstWaarde(invulwaarde='o-6-0-2',
                                    label='o-6.0',
                                    status='uitgebruik',
                                    definitie='o-6.0',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-6-0-2'),
        'o-6-5': KeuzelijstWaarde(invulwaarde='o-6-5',
                                  label='o+6.5',
                                  status='uitgebruik',
                                  definitie='o+6.5',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-6-5'),
        'o-6-5-2': KeuzelijstWaarde(invulwaarde='o-6-5-2',
                                    label='o-6.5',
                                    status='uitgebruik',
                                    definitie='o-6.5',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-6-5-2'),
        'o-7-0': KeuzelijstWaarde(invulwaarde='o-7-0',
                                  label='o+7.0',
                                  status='uitgebruik',
                                  definitie='o+7.0',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-7-0'),
        'o-7-0-2': KeuzelijstWaarde(invulwaarde='o-7-0-2',
                                    label='o-7.0',
                                    status='uitgebruik',
                                    definitie='o-7.0',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedOverhang/o-7-0-2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

