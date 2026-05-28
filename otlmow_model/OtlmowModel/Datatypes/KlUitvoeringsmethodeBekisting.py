# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitvoeringsmethodeBekisting(KeuzelijstField):
    """De uitvoeringsmethode van de bekisting."""
    naam = 'KlUitvoeringsmethodeBekisting'
    label = 'Uitvoeringsmethode bekisting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUitvoeringsmethodeBekisting'
    definition = 'De uitvoeringsmethode van de bekisting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitvoeringsmethodeBekisting'
    options = {
        'afzinkmethode': KeuzelijstWaarde(invulwaarde='afzinkmethode',
                                          label='Afzinkmethode',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethodeBekisting/afzinkmethode'),
        'inzetmethode': KeuzelijstWaarde(invulwaarde='inzetmethode',
                                         label='Inzetmethode',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethodeBekisting/inzetmethode'),
        'rolsteunbeschoeiing': KeuzelijstWaarde(invulwaarde='rolsteunbeschoeiing',
                                                label='Rolsteunbeschoeiing',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethodeBekisting/rolsteunbeschoeiing')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

