# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitvoeringRandafwerking(KeuzelijstField):
    """De lijst met verschillende types uitvoering van de randafwerking."""
    naam = 'KlUitvoeringRandafwerking'
    label = 'uitvoering randafwerking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlUitvoeringRandafwerking'
    definition = 'De lijst met verschillende types uitvoering van de randafwerking.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitvoeringRandafwerking'
    options = {
        'losse-elementen': KeuzelijstWaarde(invulwaarde='losse-elementen',
                                            label='losse elementen',
                                            status='ingebruik',
                                            definitie='Uitvoeringswijze waarbij de randafwerking wordt opgebouwd uit afzonderlijke, vooraf vervaardigde elementen die individueel worden geplaatst en samen een doorlopende afwerking vormen.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringRandafwerking/losse-elementen'),
        'profiel': KeuzelijstWaarde(invulwaarde='profiel',
                                    label='profiel',
                                    status='ingebruik',
                                    definitie='Uitvoeringswijze waarbij de randafwerking bestaat uit een doorlopend, industrieel vervaardigd profiel dat als afgewerkt element langs de rand of hoek van de constructie wordt gemonteerd.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringRandafwerking/profiel'),
        'ter-plaatste-gestort': KeuzelijstWaarde(invulwaarde='ter-plaatste-gestort',
                                                 label='ter plaatste gestort',
                                                 status='ingebruik',
                                                 definitie='Uitvoeringswijze waarbij de randafwerking op de werf in situ wordt gerealiseerd door het storten van materiaal in een bekisting, resulterend in een monolithisch geheel.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringRandafwerking/ter-plaatste-gestort')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

