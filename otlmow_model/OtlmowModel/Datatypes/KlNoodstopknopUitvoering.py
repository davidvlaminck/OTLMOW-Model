# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNoodstopknopUitvoering(KeuzelijstField):
    """Verschillende types voor de uitvoering van een noodstopknop of -schakelaarvolgens zijn werkingsprincipe."""
    naam = 'KlNoodstopknopUitvoering'
    label = 'Noodstopknop uitvoering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNoodstopknopUitvoering'
    definition = 'Verschillende types voor de uitvoering van een noodstopknop of -schakelaarvolgens zijn werkingsprincipe.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNoodstopknopUitvoering'
    options = {
        'draaischakelaar': KeuzelijstWaarde(invulwaarde='draaischakelaar',
                                            label='draaischakelaar',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopUitvoering/draaischakelaar'),
        'drukknop': KeuzelijstWaarde(invulwaarde='drukknop',
                                     label='drukknop',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopUitvoering/drukknop'),
        'met-sleutel': KeuzelijstWaarde(invulwaarde='met-sleutel',
                                        label='met sleutel',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopUitvoering/met-sleutel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

