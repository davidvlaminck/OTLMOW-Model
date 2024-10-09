# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkpoortType(KeuzelijstField):
    """Lijst van types voor Netwerkpoort."""
    naam = 'KlNetwerkpoortType'
    label = 'Netwerkpoort type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkpoortType'
    definition = 'Lijst van types voor Netwerkpoort.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkpoortType'
    options = {
        'NNI': KeuzelijstWaarde(invulwaarde='NNI',
                                label='NNI',
                                status='ingebruik',
                                definitie='Network-Network-Interface: deze poort verbindt het netwerk toestel met een ander netwerk toestel binnen eenzelfde netwerk technologie',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/NNI'),
        'NULL': KeuzelijstWaarde(invulwaarde='NULL',
                                 label='NULL',
                                 status='ingebruik',
                                 definitie='Geen interface.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/NULL'),
        'Other': KeuzelijstWaarde(invulwaarde='Other',
                                  label='Other',
                                  status='ingebruik',
                                  definitie='Ander, onbekend type interface. Deze optie mag uitsluitend TIJDELIJK worden gebruikt en enkel tot de juiste gegevens beschikbaar zijn. Misbruik van deze optie leidt tot verminderde datakwaliteit.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/Other'),
        'UNI': KeuzelijstWaarde(invulwaarde='UNI',
                                label='UNI',
                                status='ingebruik',
                                definitie='User-Network-Interface: deze poort verbindt het netwerk toestel direct met de poort van een gebruiker',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/UNI'),
        'e-nni': KeuzelijstWaarde(invulwaarde='e-nni',
                                  label='e-NNI',
                                  status='ingebruik',
                                  definitie='External Network-Network-Interface: deze poort verbindt het netwerk toestel met een ander netwerk toestel van een andere netwerk technologie',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/e-nni'),
        'i-uni': KeuzelijstWaarde(invulwaarde='i-uni',
                                  label='i-UNI',
                                  status='ingebruik',
                                  definitie='Internal User-Network-Interface: deze poort verbindt het netwerk toestel via een link met de poort van een gebruiker.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/i-uni'),
        'ncni': KeuzelijstWaarde(invulwaarde='ncni',
                                 label='NCNI',
                                 status='ingebruik',
                                 definitie='Een Not Configured Network Interface.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/ncni')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

