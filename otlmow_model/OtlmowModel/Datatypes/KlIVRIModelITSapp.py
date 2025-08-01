# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIModelITSapp(KeuzelijstField):
    """De modelnaam van de ITSapp."""
    naam = 'KlIVRIModelITSapp'
    label = 'iVRIModelITSapp'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIModelITSapp'
    definition = 'De modelnaam van de ITSapp.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIModelITSapp'
    options = {
        'flowtack': KeuzelijstWaarde(invulwaarde='flowtack',
                                     label='Flowtack',
                                     status='ingebruik',
                                     definitie='Flowtack',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelITSapp/flowtack'),
        'goudenregelen': KeuzelijstWaarde(invulwaarde='goudenregelen',
                                          label='Goudenregelen',
                                          status='ingebruik',
                                          definitie='Goudenregelen',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelITSapp/goudenregelen'),
        'imflow': KeuzelijstWaarde(invulwaarde='imflow',
                                   label='Imflow',
                                   status='ingebruik',
                                   definitie='Imflow',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelITSapp/imflow'),
        'stridefx': KeuzelijstWaarde(invulwaarde='stridefx',
                                     label='StrideFX',
                                     status='ingebruik',
                                     definitie='StrideFX',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelITSapp/stridefx')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

