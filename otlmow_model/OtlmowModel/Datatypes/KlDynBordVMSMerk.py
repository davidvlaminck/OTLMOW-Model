# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordVMSMerk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van VMS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlDynBordVMSMerk'
    label = 'Dyn bord VMS merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordVMSMerk'
    definition = 'Keuzelijst met de gangbare merken van VMS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordVMSMerk'
    options = {
        'dms': KeuzelijstWaarde(invulwaarde='dms',
                                label='DMS',
                                status='ingebruik',
                                definitie='Display and Mobility Solutions',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordVMSMerk/dms'),
        'swarco': KeuzelijstWaarde(invulwaarde='swarco',
                                   label='Swarco',
                                   status='ingebruik',
                                   definitie='Swarco',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordVMSMerk/swarco')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

