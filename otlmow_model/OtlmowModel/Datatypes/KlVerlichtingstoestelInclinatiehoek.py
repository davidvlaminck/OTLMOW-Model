# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerlichtingstoestelInclinatiehoek(KeuzelijstField):
    """De inclinatiehoek geeft aan hoeveel het verlichtingstoestel naar voren of naar achteren is gekanteld ten opzichte van de horizontale stand. Deze informatie wordt uitgedrukt in graden."""
    naam = 'KlVerlichtingstoestelInclinatiehoek'
    label = 'Verlichtingstoestel inclinatiehoek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelInclinatiehoek'
    definition = 'De inclinatiehoek geeft aan hoeveel het verlichtingstoestel naar voren of naar achteren is gekanteld ten opzichte van de horizontale stand. Deze informatie wordt uitgedrukt in graden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerlichtingstoestelInclinatiehoek'
    options = {
        '0': KeuzelijstWaarde(invulwaarde='0',
                              label='0',
                              status='ingebruik',
                              definitie='0',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelInclinatiehoek/0'),
        '10': KeuzelijstWaarde(invulwaarde='10',
                               label='10',
                               status='ingebruik',
                               definitie='10',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelInclinatiehoek/10'),
        '15': KeuzelijstWaarde(invulwaarde='15',
                               label='15',
                               status='ingebruik',
                               definitie='15',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelInclinatiehoek/15'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              status='ingebruik',
                              definitie='5',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelInclinatiehoek/5')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

