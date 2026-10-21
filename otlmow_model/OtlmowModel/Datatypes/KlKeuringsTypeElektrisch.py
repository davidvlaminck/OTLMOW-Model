# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKeuringsTypeElektrisch(KeuzelijstField):
    """De mogelijke keuringstypes voor de elektrische keuring."""
    naam = 'KlKeuringsTypeElektrisch'
    label = 'Keuringstype elektrisch'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKeuringsTypeElektrisch'
    definition = 'De mogelijke keuringstypes voor de elektrische keuring.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKeuringsTypeElektrisch'
    options = {
        'eerste-keuring': KeuzelijstWaarde(invulwaarde='eerste-keuring',
                                           label='eerste keuring',
                                           status='ingebruik',
                                           definitie='Eerste formele keuring van een bestaande elektrische installatie waarvoor nog geen eerdere keuring werd uitgevoerd of geregistreerd.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKeuringsTypeElektrisch/eerste-keuring'),
        'indienstnamekeuring': KeuzelijstWaarde(invulwaarde='indienstnamekeuring',
                                                label='indienstnamekeuring',
                                                status='ingebruik',
                                                definitie='Keuring van een elektrische installatie vóór de eerste ingebruikname, om na te gaan of deze voldoet aan de geldende veiligheidsvoorschriften en wettelijke vereisten.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKeuringsTypeElektrisch/indienstnamekeuring'),
        'periodieke-keuring': KeuzelijstWaarde(invulwaarde='periodieke-keuring',
                                               label='periodieke keuring',
                                               status='ingebruik',
                                               definitie='Keuring die op regelmatige of wettelijk voorgeschreven tijdstippen wordt herhaald om na te gaan of een elektrische installatie nog steeds voldoet aan de geldende veiligheidsvoorschriften en wettelijke vereisten.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKeuringsTypeElektrisch/periodieke-keuring')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

