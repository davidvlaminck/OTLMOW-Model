# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPompGroepModelnaam(KeuzelijstField):
    """De modelnaam van de pompgroep."""
    naam = 'KlPompGroepModelnaam'
    label = 'Pompgroep modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlPompGroepModelnaam'
    definition = 'De modelnaam van de pompgroep.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPompGroepModelnaam'
    options = {
        'tp50v': KeuzelijstWaarde(invulwaarde='tp50v',
                                  label='TP50V',
                                  status='ingebruik',
                                  definitie='TP50V',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompGroepModelnaam/tp50v')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

