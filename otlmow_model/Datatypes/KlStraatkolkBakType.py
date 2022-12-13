# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStraatkolkBakType(KeuzelijstField):
    """Het type van bak van de straatkolk."""
    naam = 'KlStraatkolkBakType'
    label = 'Straatkolk bak type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStraatkolkBakType'
    definition = 'Het type van bak van de straatkolk.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStraatkolkBakType'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/beton'),
        'gemetst': KeuzelijstWaarde(invulwaarde='gemetst',
                                    label='gemetst',
                                    status='ingebruik',
                                    definitie='gemetst',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/gemetst'),
        'geprefabriceerde-betonnen-bak-type-I': KeuzelijstWaarde(invulwaarde='geprefabriceerde-betonnen-bak-type-I',
                                                                 label='geprefabriceerde betonnen bak type I',
                                                                 status='ingebruik',
                                                                 definitie='geprefabriceerde betonnen bak type I',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/geprefabriceerde-betonnen-bak-type-I'),
        'geprefabriceerde-betonnen-bak-type-II': KeuzelijstWaarde(invulwaarde='geprefabriceerde-betonnen-bak-type-II',
                                                                  label='geprefabriceerde betonnen bak type II',
                                                                  status='ingebruik',
                                                                  definitie='geprefabriceerde betonnen bak type II',
                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/geprefabriceerde-betonnen-bak-type-II'),
        'gietijzeren-bak': KeuzelijstWaarde(invulwaarde='gietijzeren-bak',
                                            label='gietijzeren bak',
                                            status='ingebruik',
                                            definitie='gietijzeren bak',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/gietijzeren-bak'),
        'infiltratiekolk-type-1': KeuzelijstWaarde(invulwaarde='infiltratiekolk-type-1',
                                                   label='Infiltratiekolk type 1',
                                                   status='ingebruik',
                                                   definitie='Infiltratiekolk type 1',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/infiltratiekolk-type-1'),
        'infiltratiekolk-type-1-2': KeuzelijstWaarde(invulwaarde='infiltratiekolk-type-1-2',
                                                     label='Infiltratiekolk type 1+',
                                                     status='ingebruik',
                                                     definitie='Infiltratiekolk type 1+',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/infiltratiekolk-type-1-2'),
        'infiltratiekolk-type-2': KeuzelijstWaarde(invulwaarde='infiltratiekolk-type-2',
                                                   label='Infiltratiekolk type 2',
                                                   status='ingebruik',
                                                   definitie='Infiltratiekolk type 2',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkBakType/infiltratiekolk-type-2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

