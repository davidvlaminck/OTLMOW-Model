# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomOnderhoudstoestand(KeuzelijstField):
    """De verschillende mogelijke onderhoudstoestanden."""
    naam = 'KlBoomOnderhoudstoestand'
    label = 'Boom onderhoudstoestand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomOnderhoudstoestand'
    definition = 'De verschillende mogelijke onderhoudstoestanden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomOnderhoudstoestand'
    options = {
        'niet': KeuzelijstWaarde(invulwaarde='niet',
                                 label='niet',
                                 status='ingebruik',
                                 definitie='niet',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomOnderhoudstoestand/niet'),
        'niet-op-beeld-achterstallig': KeuzelijstWaarde(invulwaarde='niet-op-beeld-achterstallig',
                                                        label='niet op beeld-achterstallig',
                                                        status='ingebruik',
                                                        definitie='De boom heeft 1 snoeibeurt nodig om op beeld te komen',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomOnderhoudstoestand/niet-op-beeld-achterstallig'),
        'niet-op-beeld-problematisch': KeuzelijstWaarde(invulwaarde='niet-op-beeld-problematisch',
                                                        label='niet op beeld-problematisch',
                                                        status='ingebruik',
                                                        definitie='De boom is niet meer in een gewenste onderhoudstoestand te brengen',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomOnderhoudstoestand/niet-op-beeld-problematisch'),
        'niet-op-beeld-verwaarloosd': KeuzelijstWaarde(invulwaarde='niet-op-beeld-verwaarloosd',
                                                       label='niet op beeld-verwaarloosd',
                                                       status='ingebruik',
                                                       definitie='De boom heeft 2 of meer snoeibeurten nodig om op beeld te komen',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomOnderhoudstoestand/niet-op-beeld-verwaarloosd'),
        'op': KeuzelijstWaarde(invulwaarde='op',
                               label='op',
                               status='ingebruik',
                               definitie='op',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomOnderhoudstoestand/op'),
        'op-beeld': KeuzelijstWaarde(invulwaarde='op-beeld',
                                     label='op beeld',
                                     status='ingebruik',
                                     definitie='De boom heeft een tijdige en goede begeleidings- of onderhoudssnoei en ziet er uit zoals hij er hoort uit te zien.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomOnderhoudstoestand/op-beeld')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

