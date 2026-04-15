# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeVerbinding(KeuzelijstField):
    """De verschillende types verbindingen tussen (kelder)landhoofd, (kelder)pijler met brugdek."""
    naam = 'KlTypeVerbinding'
    label = 'type verbinding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeVerbinding'
    definition = 'De verschillende types verbindingen tussen (kelder)landhoofd, (kelder)pijler met brugdek.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeVerbinding'
    options = {
        'combinatie': KeuzelijstWaarde(invulwaarde='combinatie',
                                       label='combinatie',
                                       status='ingebruik',
                                       definitie='combinatie',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVerbinding/combinatie'),
        'integraal-verbonden': KeuzelijstWaarde(invulwaarde='integraal-verbonden',
                                                label='integraal verbonden',
                                                status='ingebruik',
                                                definitie='integraal verbonden',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVerbinding/integraal-verbonden'),
        'opgelegd': KeuzelijstWaarde(invulwaarde='opgelegd',
                                     label='opgelegd',
                                     status='ingebruik',
                                     definitie='opgelegd',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVerbinding/opgelegd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

