# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTechnischDocument(KeuzelijstField):
    """Keuzelijst met de verschillende optie voor technische documenten"""
    naam = 'KlTechnischDocument'
    label = 'Keuzelijst technisch document'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTechnischDocument'
    definition = 'Keuzelijst met de verschillende optie voor technische documenten'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTechnischDocument'
    options = {
        'detailplan': KeuzelijstWaarde(invulwaarde='detailplan',
                                       label='detailplan',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTechnischDocument/detailplan'),
        'rekennota': KeuzelijstWaarde(invulwaarde='rekennota',
                                      label='rekennota',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTechnischDocument/rekennota'),
        'technische-fiche': KeuzelijstWaarde(invulwaarde='technische-fiche',
                                             label='technische fiche',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTechnischDocument/technische-fiche')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

