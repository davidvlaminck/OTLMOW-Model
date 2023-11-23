# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangscontrollerMerk(KeuzelijstField):
    """Lijst met merknamen voor toegangscontrollers volgens de fabrikant"""
    naam = 'KlToegangscontrollerMerk'
    label = 'Toegangscontroller merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToegangscontrollerMerk'
    definition = 'Lijst met merknamen voor toegangscontrollers volgens de fabrikant'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangscontrollerMerk'
    options = {
        'aeos': KeuzelijstWaarde(invulwaarde='aeos',
                                 label='AEOS',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangscontrollerMerk/aeos')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

