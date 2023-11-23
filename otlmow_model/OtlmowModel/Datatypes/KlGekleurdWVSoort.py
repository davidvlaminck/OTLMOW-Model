# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGekleurdWVSoort(KeuzelijstField):
    """Types van gekleurd wegvlak."""
    naam = 'KlGekleurdWVSoort'
    label = 'Gekleurd WV type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGekleurdWVSoort'
    definition = 'Types van gekleurd wegvlak.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGekleurdWVSoort'
    options = {
        'OFOS-(Opgeblazen-fietsopstelstrook)': KeuzelijstWaarde(invulwaarde='OFOS-(Opgeblazen-fietsopstelstrook)',
                                                                label='OFOS (Opgeblazen fietsopstelstrook)',
                                                                status='ingebruik',
                                                                definitie='Gekleurd wegvlak als OFOS.',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/OFOS-(Opgeblazen-fietsopstelstrook)'),
        'OFOS-variant': KeuzelijstWaarde(invulwaarde='OFOS-variant',
                                         label='OFOS variant',
                                         status='ingebruik',
                                         definitie='Gekleurd wegvlak als OFOS variant.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/OFOS-variant'),
        'fiets-suggestiestrook': KeuzelijstWaarde(invulwaarde='fiets-suggestiestrook',
                                                  label='fiets suggestiestrook',
                                                  status='ingebruik',
                                                  definitie='Gekleurd wegvlak als fiets suggestiestrook.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/fiets-suggestiestrook'),
        'fietsoversteekplaats-met-blokken-(FOP)': KeuzelijstWaarde(invulwaarde='fietsoversteekplaats-met-blokken-(FOP)',
                                                                   label='fietsoversteekplaats met blokken (FOP)',
                                                                   status='ingebruik',
                                                                   definitie='Gekleurd wegvlak als fietsoversteekplaats met blokken.',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/fietsoversteekplaats-met-blokken-(FOP)'),
        'fietspad-(met-lijnen)': KeuzelijstWaarde(invulwaarde='fietspad-(met-lijnen)',
                                                  label='fietspad (met lijnen)',
                                                  status='ingebruik',
                                                  definitie='Gekleurd wegvlak als fietspad (met lijnen).',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/fietspad-(met-lijnen)'),
        'middengeleider-(Bv.-Groene-strook)': KeuzelijstWaarde(invulwaarde='middengeleider-(Bv.-Groene-strook)',
                                                               label='middengeleider (Bv. Groene strook)',
                                                               status='ingebruik',
                                                               definitie='Gekleurd wegvlak als middengeleider.',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/middengeleider-(Bv.-Groene-strook)'),
        'parkeerplaats-mindervaliden': KeuzelijstWaarde(invulwaarde='parkeerplaats-mindervaliden',
                                                        label='parkeerplaats mindervaliden',
                                                        status='ingebruik',
                                                        definitie='Gekleurd wegvlak als parkeerplaats mindervaliden.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/parkeerplaats-mindervaliden'),
        'verkeersplateau': KeuzelijstWaarde(invulwaarde='verkeersplateau',
                                            label='verkeersplateau',
                                            status='ingebruik',
                                            definitie='Gekleurd wegvlak als verkeersplateau.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/verkeersplateau'),
        'voetgangers-oversteekplaats': KeuzelijstWaarde(invulwaarde='voetgangers-oversteekplaats',
                                                        label='voetgangers-oversteekplaats',
                                                        status='ingebruik',
                                                        definitie='Gekleurd wegvlak als voetgangers-oversteekplaats.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/voetgangers-oversteekplaats')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

