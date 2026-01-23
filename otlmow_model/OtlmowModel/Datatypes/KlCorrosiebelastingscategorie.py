# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCorrosiebelastingscategorie(KeuzelijstField):
    """De mogelijke codes om de mate van corrosieve belasting in een bepaalde omgeving te beschrijven."""
    naam = 'KlCorrosiebelastingscategorie'
    label = 'Corrosiebelastingscategorie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlCorrosiebelastingscategorie'
    definition = 'De mogelijke codes om de mate van corrosieve belasting in een bepaalde omgeving te beschrijven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCorrosiebelastingscategorie'
    options = {
        'c1': KeuzelijstWaarde(invulwaarde='c1',
                               label='C1',
                               status='ingebruik',
                               definitie='Zeer lage corrosiviteit',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosiebelastingscategorie/c1'),
        'c2': KeuzelijstWaarde(invulwaarde='c2',
                               label='C2',
                               status='ingebruik',
                               definitie='Lage corrosiviteit',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosiebelastingscategorie/c2'),
        'c3': KeuzelijstWaarde(invulwaarde='c3',
                               label='C3',
                               status='ingebruik',
                               definitie='Gemiddelde corrosiviteit',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosiebelastingscategorie/c3'),
        'c4': KeuzelijstWaarde(invulwaarde='c4',
                               label='C4',
                               status='ingebruik',
                               definitie='Hoge corrosiviteit',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosiebelastingscategorie/c4'),
        'c5': KeuzelijstWaarde(invulwaarde='c5',
                               label='C5',
                               status='ingebruik',
                               definitie='Zeer hoge corrosiviteit',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCorrosiebelastingscategorie/c5')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

