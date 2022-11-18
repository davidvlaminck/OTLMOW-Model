# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordsteunType(KeuzelijstField):
    """Types voor een verkeersbordsteun."""
    naam = 'KlVerkeersbordsteunType'
    label = 'Verkeersbordsteuntype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordsteunType'
    definition = 'Types voor een verkeersbordsteun.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordsteunType'
    options = {
        'botsvriendelijke-steun': KeuzelijstWaarde(invulwaarde='botsvriendelijke-steun',
                                                   label='botsvriendelijke steun',
                                                   status='ingebruik',
                                                   definitie='Constructie die na aanrijding zijn oorspronkelijke positie hersteld',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/botsvriendelijke-steun'),
        'botsvriendelijke-steun-type-100NE2': KeuzelijstWaarde(invulwaarde='botsvriendelijke-steun-type-100NE2',
                                                               label='botsvriendelijke steun type 100NE2',
                                                               status='ingebruik',
                                                               definitie='te bepalen',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/botsvriendelijke-steun-type-100NE2'),
        'botsvriendelijke-steun-type-100NE3': KeuzelijstWaarde(invulwaarde='botsvriendelijke-steun-type-100NE3',
                                                               label='botsvriendelijke steun type 100NE3',
                                                               status='ingebruik',
                                                               definitie='te bepalen',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/botsvriendelijke-steun-type-100NE3'),
        'galgpaal': KeuzelijstWaarde(invulwaarde='galgpaal',
                                     label='galgpaal',
                                     status='uitgebruik',
                                     definitie="Deze optie mag niet aangeduid worden! Bij instantiëren van een galgpaal moet het onderdeel 'Galgpaal' gebruikt worden.",
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/galgpaal'),
        'rechte-paal': KeuzelijstWaarde(invulwaarde='rechte-paal',
                                        label='rechte paal',
                                        status='ingebruik',
                                        definitie='Een rechte paal met als doel een verkeersbord te bevestigen.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/rechte-paal'),
        'seinbrug': KeuzelijstWaarde(invulwaarde='seinbrug',
                                     label='seinbrug',
                                     status='uitgebruik',
                                     definitie="Deze optie mag niet aangeduid worden! Bij instantiëren van een seinbrug moet het onderdeel 'Seinbrug' gebruikt worden.",
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/seinbrug'),
        'vakwerksteun': KeuzelijstWaarde(invulwaarde='vakwerksteun',
                                         label='vakwerksteun',
                                         status='ingebruik',
                                         definitie='Een keuzelijst om het type verkeersbordpaal te bepalen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/vakwerksteun')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

