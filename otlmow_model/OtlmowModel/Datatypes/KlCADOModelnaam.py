# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCADOModelnaam(KeuzelijstField):
    """De modelnaam van de calamiteitendoorsteek."""
    naam = 'KlCADOModelnaam'
    label = 'Calamiteitendoorsteek modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCADOModelnaam'
    definition = 'De modelnaam van de calamiteitendoorsteek.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCADOModelnaam'
    options = {
        'duo-gate': KeuzelijstWaarde(invulwaarde='duo-gate',
                                     label='DUO-GATE',
                                     status='ingebruik',
                                     definitie='DUO-GATE',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCADOModelnaam/duo-gate')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

