# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVentilatorGebruik(KeuzelijstField):
    """Keuzelijst die de types van gebruik voor de ventilator aangeeft."""
    naam = 'KlVentilatorGebruik'
    label = 'Gebruikstypes ventilator'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVentilatorGebruik'
    definition = 'Keuzelijst die de types van gebruik voor de ventilator aangeeft.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVentilatorGebruik'
    options = {
        'dwarsventilatie-aanzuigunit': KeuzelijstWaarde(invulwaarde='dwarsventilatie-aanzuigunit',
                                                        label='dwarsventilatie aanzuigunit',
                                                        status='verwijderd',
                                                        definitie='dwarsventilatie aanzuigunit',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/dwarsventilatie-aanzuigunit'),
        'dwarsventilatie-afvoer': KeuzelijstWaarde(invulwaarde='dwarsventilatie-afvoer',
                                                   label='dwarsventilatie afvoer',
                                                   status='ingebruik',
                                                   definitie='Een ventilatie-eenheid die lucht dwars uit de tunnel onttrekt, en deze via afvoerkanalen naar buiten afvoert.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/dwarsventilatie-afvoer'),
        'dwarsventilatie-inblaasunit': KeuzelijstWaarde(invulwaarde='dwarsventilatie-inblaasunit',
                                                        label='dwarsventilatie inblaasunit',
                                                        status='verwijderd',
                                                        definitie='dwarsventilatie inblaasunit',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/dwarsventilatie-inblaasunit'),
        'dwarsventilatie-toevoer': KeuzelijstWaarde(invulwaarde='dwarsventilatie-toevoer',
                                                    label='dwarsventilatie toevoer',
                                                    status='ingebruik',
                                                    definitie='Een ventilatie-eenheid die verse lucht toevoert dwars op de lengterichting van de tunnel eventueel via roosters of sleuven in wand of plafond.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/dwarsventilatie-toevoer'),
        'langsventilator': KeuzelijstWaarde(invulwaarde='langsventilator',
                                            label='langsventilator',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/langsventilator')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

