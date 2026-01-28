# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPictogramSymbool(KeuzelijstField):
    """De mogelijke symbolen op het pictogram."""
    naam = 'KlPictogramSymbool'
    label = 'Pictogram symbool'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPictogramSymbool'
    definition = 'De mogelijke symbolen op het pictogram.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPictogramSymbool'
    options = {
        'brandblusser': KeuzelijstWaarde(invulwaarde='brandblusser',
                                         label='brandblusser',
                                         status='ingebruik',
                                         definitie='brandblusser',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/brandblusser'),
        'halte': KeuzelijstWaarde(invulwaarde='halte',
                                  label='halte',
                                  status='ingebruik',
                                  definitie='Duidt de locatie aan waar het openbaar vervoer, bv. bus, tram of trolley, stopt om passagiers te laten in- en uitstappen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/halte'),
        'hydrant-bovengronds-(H)': KeuzelijstWaarde(invulwaarde='hydrant-bovengronds-(H)',
                                                    label='hydrant bovengronds (H)',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/hydrant-bovengronds-(H)'),
        'hydrant-ondergronds-(B)': KeuzelijstWaarde(invulwaarde='hydrant-ondergronds-(B)',
                                                    label='hydrant ondergronds (B)',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/hydrant-ondergronds-(B)'),
        'nooddeurnummer': KeuzelijstWaarde(invulwaarde='nooddeurnummer',
                                           label='nooddeurnummer',
                                           status='ingebruik',
                                           definitie='nooddeurnummer',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/nooddeurnummer'),
        'nummer-veiligheidsnis': KeuzelijstWaarde(invulwaarde='nummer-veiligheidsnis',
                                                  label='nummer veiligheidsnis',
                                                  status='ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/nummer-veiligheidsnis'),
        'telefoon': KeuzelijstWaarde(invulwaarde='telefoon',
                                     label='telefoon',
                                     status='ingebruik',
                                     definitie='telefoon',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/telefoon'),
        'tunnelnaam': KeuzelijstWaarde(invulwaarde='tunnelnaam',
                                       label='tunnelnaam',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/tunnelnaam'),
        'verbodsbord': KeuzelijstWaarde(invulwaarde='verbodsbord',
                                        label='verbodsbord',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/verbodsbord'),
        'verzamelplaats': KeuzelijstWaarde(invulwaarde='verzamelplaats',
                                           label='verzamelplaats',
                                           status='ingebruik',
                                           definitie='Een pictogram dat iedereen helpt om tijdens een noodsituatie snel de juiste plek te vinden.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/verzamelplaats'),
        'vluchtend-persoon': KeuzelijstWaarde(invulwaarde='vluchtend-persoon',
                                              label='vluchtend persoon',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/vluchtend-persoon'),
        'vluchtroute': KeuzelijstWaarde(invulwaarde='vluchtroute',
                                        label='vluchtroute',
                                        status='ingebruik',
                                        definitie='Aankondiging van de dichtstbijzijnde nooduitgang, in de aangeduide richting. De afstand in meter is aangeduid op het pictogram (F52bis).',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/vluchtroute')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

