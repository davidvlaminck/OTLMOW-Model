# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


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
                                  definitie='De rijstrook wordt gebruikt door het verkeer dat de hoofdweg wenst te verlaten.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntGebied/afrit'),
        'hoofdweg': KeuzelijstWaarde(invulwaarde='hoofdweg',
                                     label='hoofdweg',
                                     status='ingebruik',
                                     definitie='De rijstrook maakt deel uit van een wegvak met meestal meerdere rijstroken bedoeld voor doorgaand verkeer.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntGebied/hoofdweg'),
        'oprit': KeuzelijstWaarde(invulwaarde='oprit',
                                  label='oprit',
                                  status='ingebruik',
                                  definitie='De rijstrook wordt gebruikt door het verkeer dat de hoofdweg wenst te betreden.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntGebied/oprit'),
        'spookstrook': KeuzelijstWaarde(invulwaarde='spookstrook',
                                        label='spookstrook',
                                        status='ingebruik',
                                        definitie='Een tweede meetpunt op dezelfde plaats in een tunnel (of net er buiten) om te kunnen tellen wanneer er omgekeerd gereden wordt op een rijstrook tijdens een tunnelsluiting.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntGebied/spookstrook'),
        'tunnel': KeuzelijstWaarde(invulwaarde='tunnel',
                                   label='tunnel',
                                   status='ingebruik',
                                   definitie='De rijstrook maakt deel uit van een tunnel (overdekte weg).',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntGebied/tunnel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

