# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCapacitieveNiveaumetingMerk(KeuzelijstField):
    """Merknamen van de capacitieve niveaumeting."""
    naam = 'KlCapacitieveNiveaumetingMerk'
    label = 'Capacitieve niveaumeting merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCapacitieveNiveaumetingMerk'
    definition = 'Merknamen van de capacitieve niveaumeting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCapacitieveNiveaumetingMerk'
    options = {
        'endress-hauser': KeuzelijstWaarde(invulwaarde='endress-hauser',
                                           label='Endress+Hauser',
                                           status='ingebruik',
                                           definitie='Endress+Hauser',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCapacitieveNiveaumetingMerk/endress-hauser'),
        'grundfos': KeuzelijstWaarde(invulwaarde='grundfos',
                                     label='Grundfos',
                                     status='ingebruik',
                                     definitie='Grundfos',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCapacitieveNiveaumetingMerk/grundfos'),
        'lowara': KeuzelijstWaarde(invulwaarde='lowara',
                                   label='Lowara',
                                   status='ingebruik',
                                   definitie='Lowara-Xylem',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCapacitieveNiveaumetingMerk/lowara')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

