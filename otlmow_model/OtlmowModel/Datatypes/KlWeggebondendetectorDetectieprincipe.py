# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeggebondendetectorDetectieprincipe(KeuzelijstField):
    """Keuzelijst met de verschillende gangbare manieren waarop een weggebonden detector voertuigen detecteert, bv. door gebruik te maken van inductie of doppler."""
    naam = 'KlWeggebondendetectorDetectieprincipe'
    label = 'Weggebondendetector detectieprincipe'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeggebondendetectorDetectieprincipe'
    definition = 'Keuzelijst met de verschillende gangbare manieren waarop een weggebonden detector voertuigen detecteert, bv. door gebruik te maken van inductie of doppler.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeggebondendetectorDetectieprincipe'
    options = {
        'doppler': KeuzelijstWaarde(invulwaarde='doppler',
                                    label='doppler',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeggebondendetectorDetectieprincipe/doppler'),
        'inductief': KeuzelijstWaarde(invulwaarde='inductief',
                                      label='inductief',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeggebondendetectorDetectieprincipe/inductief'),
        'infrarood': KeuzelijstWaarde(invulwaarde='infrarood',
                                      label='infrarood',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeggebondendetectorDetectieprincipe/infrarood'),
        'infrarood+inductief': KeuzelijstWaarde(invulwaarde='infrarood+inductief',
                                                label='infrarood+inductief',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeggebondendetectorDetectieprincipe/infrarood+inductief')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

