# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBetonnenProfiel(KeuzelijstField):
    """Het type betonnen profiel."""
    naam = 'KlTypeBetonnenProfiel'
    label = 'Type betonnen profiel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBetonnenProfiel'
    definition = 'Het type betonnen profiel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBetonnenProfiel'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='Andere',
                                   status='ingebruik',
                                   definitie='Niet-standaardprofiel: een profiel in een andere, specifieke vorm.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBetonnenProfiel/andere'),
        'i-profiel': KeuzelijstWaarde(invulwaarde='i-profiel',
                                      label='I-profiel',
                                      status='ingebruik',
                                      definitie='Standaardprofiel met een dwarsdoorsnede in de vorm van een I (onder- en bovenflens die met elkaar verbonden zijn door het lijf).',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBetonnenProfiel/i-profiel'),
        'omgekeerd-t-profiel': KeuzelijstWaarde(invulwaarde='omgekeerd-t-profiel',
                                                label='Omgekeerd T-profiel',
                                                status='ingebruik',
                                                definitie='Standaardprofiel met een dwarsdoorsnede in de vorm van een T (geen bovenfles, wel een onderflens en een lijf).',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBetonnenProfiel/omgekeerd-t-profiel'),
        'omgekeerd-u-profiel': KeuzelijstWaarde(invulwaarde='omgekeerd-u-profiel',
                                                label='Omgekeerd U-profiel',
                                                status='ingebruik',
                                                definitie='Standaardprofiel met een bovenflens en twee lijven die samen een omgekeerde U vormen.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBetonnenProfiel/omgekeerd-u-profiel'),
        'plaatligger': KeuzelijstWaarde(invulwaarde='plaatligger',
                                        label='Plaatligger',
                                        status='ingebruik',
                                        definitie='Standaardprofiel met een dwarsdoorsnede in de vorm van een I (onder- en bovenflens die met elkaar verbonden zijn door het lijf) maar de bovenflens is verbreed.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBetonnenProfiel/plaatligger'),
        'rechthoekige-ligger': KeuzelijstWaarde(invulwaarde='rechthoekige-ligger',
                                                label='Rechthoekige ligger',
                                                status='ingebruik',
                                                definitie='Niet-standaardprofiel met een dwarsdoorsnede van een rechthoek (massieve ligger).',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBetonnenProfiel/rechthoekige-ligger'),
        'u-profiel': KeuzelijstWaarde(invulwaarde='u-profiel',
                                      label='U-profiel',
                                      status='ingebruik',
                                      definitie='Standaardprofiel met een onderflens en twee lijven die samen een U vormen.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBetonnenProfiel/u-profiel'),
        'z-profiel': KeuzelijstWaarde(invulwaarde='z-profiel',
                                      label='Z-profiel',
                                      status='ingebruik',
                                      definitie='Niet-standaardprofiel met een dwarsdoorsnede in de vorm van een Z.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBetonnenProfiel/z-profiel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

