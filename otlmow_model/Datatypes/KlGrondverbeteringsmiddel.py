# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrondverbeteringsmiddel(KeuzelijstField):
    """Het verwerken van bodemverbeteringsmiddelen omvat het gelijkmatig spreiden ervan op bepaalde grondoppervlakken en/of het verwerken in plantputten."""
    naam = 'KlGrondverbeteringsmiddel'
    label = 'Grondverbeteringsmiddel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlGrondverbeteringsmiddel'
    definition = 'Het verwerken van bodemverbeteringsmiddelen omvat het gelijkmatig spreiden ervan op bepaalde grondoppervlakken en/of het verwerken in plantputten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrondverbeteringsmiddel'
    options = {
        'bezanden': KeuzelijstWaarde(invulwaarde='bezanden',
                                     label='bezanden',
                                     status='ingebruik',
                                     definitie='Natuurlijk zand.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondverbeteringsmiddel/bezanden'),
        'gft-compost': KeuzelijstWaarde(invulwaarde='gft-compost',
                                        label='GFT-compost',
                                        status='ingebruik',
                                        definitie='GFT-compost is het product verkregen door een gecontroleerde aÃƒÂ«robe compostering van het gescheiden ingezamelde organische deel van het huishoudelijk afval tot volledige rijping.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondverbeteringsmiddel/gft-compost'),
        'groencompost': KeuzelijstWaarde(invulwaarde='groencompost',
                                         label='groencompost',
                                         status='ingebruik',
                                         definitie='Groencompost is een product verkregen door een gecontroleerde aerobe compostering van groenafval tot volledige rijping, voorafgegaan of gevolgd door mechanische behandelingen.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondverbeteringsmiddel/groencompost')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

