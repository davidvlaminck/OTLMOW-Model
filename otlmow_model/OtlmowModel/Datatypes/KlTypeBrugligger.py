# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBrugligger(KeuzelijstField):
    """Het type van de brugligger."""
    naam = 'KlTypeBrugligger'
    label = 'Type brugligger'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeBrugligger'
    definition = 'Het type van de brugligger.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBrugligger'
    options = {
        'dwarsdrager': KeuzelijstWaarde(invulwaarde='dwarsdrager',
                                        label='Dwarsdrager',
                                        status='ingebruik',
                                        definitie='Balk of ligger volgens de dwarsrichting van de brug die één of meerdere van volgende functies vervult:biedt ondersteuning aan het brugdek en/of de langsliggers en/of de hoofdliggers,verstijft de langs- en/of hoofdliggers,draagt de belastingen af naar de hoofdliggers,bevordert de samenwerking tussen de hoofdliggers.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugligger/dwarsdrager'),
        'hoofdligger': KeuzelijstWaarde(invulwaarde='hoofdligger',
                                        label='Hoofdligger',
                                        status='ingebruik',
                                        definitie='Primaire dragende balk of ligger volgens de lengterichting van de brug, die de belastingen afdraagt naar de oplegpunten van de brug, hetzij rechtstreeks, hetzij via einddwarsdragers/diafragma’s.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugligger/hoofdligger'),
        'langsligger': KeuzelijstWaarde(invulwaarde='langsligger',
                                        label='Langsligger',
                                        status='ingebruik',
                                        definitie='Secundaire balk of ligger volgens de lengterichting van de brug, die ondersteuning biedt aan het brugdek en de belastingen erop afdraagt naar de dwarsliggers.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugligger/langsligger')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

