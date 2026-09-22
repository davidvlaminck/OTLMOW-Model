# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHydrostatischeNiveaumetingMerk(KeuzelijstField):
    """Merknamen van de hydrostatische niveaumeting."""
    naam = 'KlHydrostatischeNiveaumetingMerk'
    label = 'Hydrostatische niveaumeting merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHydrostatischeNiveaumetingMerk'
    definition = 'Merknamen van de hydrostatische niveaumeting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHydrostatischeNiveaumetingMerk'
    options = {
        'endress-hauser': KeuzelijstWaarde(invulwaarde='endress-hauser',
                                           label='Endress+Hauser',
                                           status='ingebruik',
                                           definitie='Endress+Hauser',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHydrostatischeNiveaumetingMerk/endress-hauser')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

