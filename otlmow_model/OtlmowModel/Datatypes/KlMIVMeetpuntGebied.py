# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVMeetpuntGebied(KeuzelijstField):
    """Mogelijke MIV meetpuntgebieden."""
    naam = 'KlMIVMeetpuntGebied'
    label = 'MIV meetpuntgebied'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMIVMeetpuntGebied'
    definition = 'Mogelijke MIV meetpuntgebieden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVMeetpuntGebied'
    options = {
        'afrit': KeuzelijstWaarde(invulwaarde='afrit',
                                  label='afrit',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntGebied/afrit'),
        'hoofdweg': KeuzelijstWaarde(invulwaarde='hoofdweg',
                                     label='hoofdweg',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntGebied/hoofdweg'),
        'oprit': KeuzelijstWaarde(invulwaarde='oprit',
                                  label='oprit',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntGebied/oprit'),
        'spookstrook': KeuzelijstWaarde(invulwaarde='spookstrook',
                                        label='spookstrook',
                                        status='ingebruik',
                                        definitie='Een tweede meetpunt op dezelfde plaats in een tunnel (of net er buiten) om te kunnen tellen wanneer er omgekeerd gereden wordt op een rijstrook tijdens een tunnelsluiting.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntGebied/spookstrook'),
        'tunnel': KeuzelijstWaarde(invulwaarde='tunnel',
                                   label='tunnel',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntGebied/tunnel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

