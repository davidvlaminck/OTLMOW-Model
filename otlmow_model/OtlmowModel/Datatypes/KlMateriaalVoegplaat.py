# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalVoegplaat(KeuzelijstField):
    """Lijst met de verschillende opties van materiaal voor een voegplaat."""
    naam = 'KlMateriaalVoegplaat'
    label = 'materiaal voegplaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalVoegplaat'
    definition = 'Lijst met de verschillende opties van materiaal voor een voegplaat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalVoegplaat'
    options = {
        'asfaltvilt': KeuzelijstWaarde(invulwaarde='asfaltvilt',
                                       label='asfaltvilt',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalVoegplaat/asfaltvilt'),
        'geexpandeerd-polystyreen': KeuzelijstWaarde(invulwaarde='geexpandeerd-polystyreen',
                                                     label='geexpandeerd polystyreen',
                                                     status='ingebruik',
                                                     definitie='geëxpandeerd polystyreen',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalVoegplaat/geexpandeerd-polystyreen'),
        'kurk': KeuzelijstWaarde(invulwaarde='kurk',
                                 label='kurk',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalVoegplaat/kurk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

