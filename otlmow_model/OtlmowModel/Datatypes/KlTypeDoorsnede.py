# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeDoorsnede(KeuzelijstField):
    """Type doorsnede van de ligger."""
    naam = 'KlTypeDoorsnede'
    label = 'type doorsnede'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeDoorsnede'
    definition = 'Type doorsnede van de ligger.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeDoorsnede'
    options = {
        'niet-toegankelijke-koker': KeuzelijstWaarde(invulwaarde='niet-toegankelijke-koker',
                                                     label='Niet-toegankelijke koker',
                                                     status='ingebruik',
                                                     definitie='Een holle ligger die niet betreedbaar is voor inspecties en onderhoud.',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeDoorsnede/niet-toegankelijke-koker'),
        'open-doorsnede-balk': KeuzelijstWaarde(invulwaarde='open-doorsnede-balk',
                                                label='Open doorsnede (balk)',
                                                status='ingebruik',
                                                definitie='Een ligger met een open, niet-gesloten vorm, zoals een I-, T-, of U-profiel.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeDoorsnede/open-doorsnede-balk'),
        'toegankelijke-koker': KeuzelijstWaarde(invulwaarde='toegankelijke-koker',
                                                label='Toegankelijke koker',
                                                status='ingebruik',
                                                definitie='Een holle ligger die betreedbaar is voor inspecties en onderhoud',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeDoorsnede/toegankelijke-koker')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

