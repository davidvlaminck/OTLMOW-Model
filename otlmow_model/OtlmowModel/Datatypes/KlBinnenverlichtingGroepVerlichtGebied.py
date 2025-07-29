# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBinnenverlichtingGroepVerlichtGebied(KeuzelijstField):
    """Het gebied dat verlicht wordt door de binnenverlichtingstoestellen die deel uitmaken van de groep."""
    naam = 'KlBinnenverlichtingGroepVerlichtGebied'
    label = 'Binnenverlichting groep verlicht gebied'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlBinnenverlichtingGroepVerlichtGebied'
    definition = 'Het gebied dat verlicht wordt door de binnenverlichtingstoestellen die deel uitmaken van de groep.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBinnenverlichtingGroepVerlichtGebied'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

