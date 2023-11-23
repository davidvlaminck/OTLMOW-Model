# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLokaalTerreinType(KeuzelijstField):
    """Lokale terrein types."""
    naam = 'KlLokaalTerreinType'
    label = 'Lokaal terreintype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlLokaalTerreinType'
    definition = 'Lokale terrein types.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLokaalTerreinType'
    options = {
        'andere-gelieve-te-omschrijven-in-extra-notitie-voor-het-object': KeuzelijstWaarde(invulwaarde='andere-gelieve-te-omschrijven-in-extra-notitie-voor-het-object',
                                                                                           label='Andere (gelieve te omschrijven in extra notitie voor het object)',
                                                                                           status='ingebruik',
                                                                                           definitie='Andere (gelieve te omschrijven in extra notitie voor het object)',
                                                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLokaalTerreinType/andere-gelieve-te-omschrijven-in-extra-notitie-voor-het-object'),
        'bergachtig-en-overwegend-bomen-struiken': KeuzelijstWaarde(invulwaarde='bergachtig-en-overwegend-bomen-struiken',
                                                                    label='Bergachtig en overwegend bomen / struiken',
                                                                    status='ingebruik',
                                                                    definitie='Bergachtig en overwegend bomen / struiken',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLokaalTerreinType/bergachtig-en-overwegend-bomen-struiken'),
        'bergachtig-verspreid-bomen-struiken': KeuzelijstWaarde(invulwaarde='bergachtig-verspreid-bomen-struiken',
                                                                label='Bergachtig verspreid bomen / struiken',
                                                                status='ingebruik',
                                                                definitie='Bergachtig verspreid bomen / struiken',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLokaalTerreinType/bergachtig-verspreid-bomen-struiken'),
        'bergachtig-zonder-bomen': KeuzelijstWaarde(invulwaarde='bergachtig-zonder-bomen',
                                                    label='Bergachtig zonder bomen',
                                                    status='ingebruik',
                                                    definitie='Bergachtig zonder bomen',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLokaalTerreinType/bergachtig-zonder-bomen'),
        'golvend-en-overwegend-bomen-struiken': KeuzelijstWaarde(invulwaarde='golvend-en-overwegend-bomen-struiken',
                                                                 label='Golvend en overwegend bomen / struiken',
                                                                 status='ingebruik',
                                                                 definitie='Golvend en overwegend bomen / struiken',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLokaalTerreinType/golvend-en-overwegend-bomen-struiken'),
        'golvend-verspreid-bomen-struiken': KeuzelijstWaarde(invulwaarde='golvend-verspreid-bomen-struiken',
                                                             label='Golvend verspreid bomen / struiken',
                                                             status='ingebruik',
                                                             definitie='Golvend verspreid bomen / struiken',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLokaalTerreinType/golvend-verspreid-bomen-struiken'),
        'golvend-zonder-bomen': KeuzelijstWaarde(invulwaarde='golvend-zonder-bomen',
                                                 label='Golvend zonder bomen',
                                                 status='ingebruik',
                                                 definitie='Golvend zonder bomen',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLokaalTerreinType/golvend-zonder-bomen'),
        'vlak-en-overwegend-bomen-struiken': KeuzelijstWaarde(invulwaarde='vlak-en-overwegend-bomen-struiken',
                                                              label='Vlak en overwegend bomen / struiken',
                                                              status='ingebruik',
                                                              definitie='Vlak en overwegend bomen / struiken',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLokaalTerreinType/vlak-en-overwegend-bomen-struiken'),
        'vlak-en-verspreid-bomen-struiken': KeuzelijstWaarde(invulwaarde='vlak-en-verspreid-bomen-struiken',
                                                             label='Vlak en verspreid bomen / struiken',
                                                             status='ingebruik',
                                                             definitie='Vlak en verspreid bomen / struiken',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLokaalTerreinType/vlak-en-verspreid-bomen-struiken'),
        'vlak-zonder-bomen': KeuzelijstWaarde(invulwaarde='vlak-zonder-bomen',
                                              label='Vlak zonder bomen',
                                              status='ingebruik',
                                              definitie='Vlak zonder bomen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLokaalTerreinType/vlak-zonder-bomen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

