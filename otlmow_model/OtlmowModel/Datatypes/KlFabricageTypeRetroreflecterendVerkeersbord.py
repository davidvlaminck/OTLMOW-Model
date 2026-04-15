# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFabricageTypeRetroreflecterendVerkeersbord(KeuzelijstField):
    """Genormaliseerde referenties waaraan het verkeersbord moet voldoen."""
    naam = 'KlFabricageTypeRetroreflecterendVerkeersbord'
    label = 'Fabricage type retroreflecterend verkeersbord'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFabricageTypeRetroreflecterendVerkeersbord'
    definition = 'Genormaliseerde referenties waaraan het verkeersbord moet voldoen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFabricageTypeRetroreflecterendVerkeersbord'
    options = {
        'BRUGGEN_EN_WEGEN': KeuzelijstWaarde(invulwaarde='BRUGGEN_EN_WEGEN',
                                             label='Bruggen en wegen',
                                             status='ingebruik',
                                             definitie='Bruggen en wegen',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFabricageTypeRetroreflecterendVerkeersbord/BRUGGEN_EN_WEGEN'),
        'INWENDIG_VERLICHT': KeuzelijstWaarde(invulwaarde='INWENDIG_VERLICHT',
                                              label='Inwendig verlicht',
                                              status='ingebruik',
                                              definitie='Inwendig verlicht',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFabricageTypeRetroreflecterendVerkeersbord/INWENDIG_VERLICHT'),
        'ONBEKEND': KeuzelijstWaarde(invulwaarde='ONBEKEND',
                                     label='Onbekend',
                                     status='ingebruik',
                                     definitie='Onbekend',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFabricageTypeRetroreflecterendVerkeersbord/ONBEKEND'),
        'PRISMABORDEN': KeuzelijstWaarde(invulwaarde='PRISMABORDEN',
                                         label='Prismaborden',
                                         status='uitgebruik',
                                         definitie='Prismaborden',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFabricageTypeRetroreflecterendVerkeersbord/PRISMABORDEN'),
        'SB250': KeuzelijstWaarde(invulwaarde='SB250',
                                  label='Standaardbestek 250',
                                  status='ingebruik',
                                  definitie='Standaardbestek 250',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFabricageTypeRetroreflecterendVerkeersbord/SB250'),
        'SB250_SCHARNIER': KeuzelijstWaarde(invulwaarde='SB250_SCHARNIER',
                                            label='Standaardbestek 250 Scharnierbord',
                                            status='ingebruik',
                                            definitie='Standaardbestek 250 Scharnierbord',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFabricageTypeRetroreflecterendVerkeersbord/SB250_SCHARNIER'),
        'SB270': KeuzelijstWaarde(invulwaarde='SB270',
                                  label='Standaardbestek 270',
                                  status='ingebruik',
                                  definitie='Standaardbestek 270',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFabricageTypeRetroreflecterendVerkeersbord/SB270'),
        'SB280': KeuzelijstWaarde(invulwaarde='SB280',
                                  label='Standaardbestek 280',
                                  status='ingebruik',
                                  definitie='Standaardbestek 280',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFabricageTypeRetroreflecterendVerkeersbord/SB280'),
        'T2000': KeuzelijstWaarde(invulwaarde='T2000',
                                  label='T2000',
                                  status='ingebruik',
                                  definitie='T2000',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFabricageTypeRetroreflecterendVerkeersbord/T2000'),
        'VLAK': KeuzelijstWaarde(invulwaarde='VLAK',
                                 label='Vlak',
                                 status='ingebruik',
                                 definitie='Vlak',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFabricageTypeRetroreflecterendVerkeersbord/VLAK'),
        'standaardbestek-280': KeuzelijstWaarde(invulwaarde='standaardbestek-280',
                                                label='Standaardbestek 280',
                                                status='verwijderd',
                                                definitie='Standaardbestek 280',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFabricageTypeRetroreflecterendVerkeersbord/standaardbestek-280')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

