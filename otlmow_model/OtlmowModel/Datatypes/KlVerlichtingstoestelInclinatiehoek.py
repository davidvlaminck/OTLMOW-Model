# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerlichtingstoestelInclinatiehoek(KeuzelijstField):
    """De inclinatiehoek geeft aan hoeveel het verlichtingstoestel naar voren of naar achteren is gekanteld ten opzichte van de horizontale stand. Deze informatie wordt uitgedrukt in graden."""
    naam = 'KlVerlichtingstoestelInclinatiehoek'
    label = 'Verlichtingstoestel inclinatiehoek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelInclinatiehoek'
    definition = 'De inclinatiehoek geeft aan hoeveel het verlichtingstoestel naar voren of naar achteren is gekanteld ten opzichte van de horizontale stand. Deze informatie wordt uitgedrukt in graden.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerlichtingstoestelInclinatiehoek'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

