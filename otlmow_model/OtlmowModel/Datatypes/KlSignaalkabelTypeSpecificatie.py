# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignaalkabelTypeSpecificatie(KeuzelijstField):
    """Lijst met mogelijke specificaties van het type van de signaalkabel volgens een vaste lijst om bv. de brandklasse mee te geven."""
    naam = 'KlSignaalkabelTypeSpecificatie'
    label = 'Signaalkabel type specificatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignaalkabelTypeSpecificatie'
    definition = 'Lijst met mogelijke specificaties van het type van de signaalkabel volgens een vaste lijst om bv. de brandklasse mee te geven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignaalkabelTypeSpecificatie'
    options = {
        'cca-s3-d2-a3': KeuzelijstWaarde(invulwaarde='cca-s3-d2-a3',
                                         label='Cca s3 d2 a3',
                                         status='ingebruik',
                                         definitie='Cca s3 d2 a3',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelTypeSpecificatie/cca-s3-d2-a3'),
        'eca': KeuzelijstWaarde(invulwaarde='eca',
                                label='Eca',
                                status='ingebruik',
                                definitie='Eca',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelTypeSpecificatie/eca'),
        'rf1h': KeuzelijstWaarde(invulwaarde='rf1h',
                                 label='Rf1h',
                                 status='ingebruik',
                                 definitie='Rf1h',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelTypeSpecificatie/rf1h')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

