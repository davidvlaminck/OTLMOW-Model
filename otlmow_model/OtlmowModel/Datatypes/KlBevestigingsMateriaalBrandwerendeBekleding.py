# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBevestigingsMateriaalBrandwerendeBekleding(KeuzelijstField):
    """Keuzelijst met het type materiaal van de ankers, bouten of andere middelen waarmee de bekleding is bevestigd."""
    naam = 'KlBevestigingsMateriaalBrandwerendeBekleding'
    label = 'bevestigingsmateriaal brandwerende bekleding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBevestigingsMateriaalBrandwerendeBekleding'
    definition = 'Keuzelijst met het type materiaal van de ankers, bouten of andere middelen waarmee de bekleding is bevestigd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBevestigingsMateriaalBrandwerendeBekleding'
    options = {
        'n-v-t': KeuzelijstWaarde(invulwaarde='n-v-t',
                                  label='n.v.t.',
                                  status='ingebruik',
                                  definitie='n.v.t.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBevestigingsMateriaalBrandwerendeBekleding/n-v-t'),
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='rvs',
                                status='ingebruik',
                                definitie='rvs',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBevestigingsMateriaalBrandwerendeBekleding/rvs'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  definitie='staal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBevestigingsMateriaalBrandwerendeBekleding/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

