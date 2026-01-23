# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRechteSteunType(KeuzelijstField):
    """Keuzelijst die de verschillende types rechte steunen aanduidt."""
    naam = 'KlRechteSteunType'
    label = 'Rechte steun type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRechteSteunType'
    definition = 'Keuzelijst die de verschillende types rechte steunen aanduidt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRechteSteunType'
    options = {
        'VRI-met-zwanehals': KeuzelijstWaarde(invulwaarde='VRI-met-zwanehals',
                                              label='VRI met zwanehals',
                                              status='verwijderd',
                                              definitie="VRI met zwanehals (uit gebruik : vervangen door optie 'zwanehals')",
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/VRI-met-zwanehals'),
        'a-paal': KeuzelijstWaarde(invulwaarde='a-paal',
                                   label='a-paal',
                                   status='ingebruik',
                                   definitie='a-paal',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/a-paal'),
        'bi-flash': KeuzelijstWaarde(invulwaarde='bi-flash',
                                     label='bi-flash',
                                     status='verwijderd',
                                     definitie="bi-flash  (uit gebruik : vervangen door optie 'a-paal')",
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/bi-flash'),
        'd-paal': KeuzelijstWaarde(invulwaarde='d-paal',
                                   label='d-paal',
                                   status='ingebruik',
                                   definitie='d-paal',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/d-paal'),
        'variabele-Z30': KeuzelijstWaarde(invulwaarde='variabele-Z30',
                                          label='variabele Z30',
                                          status='verwijderd',
                                          definitie="variabele Z30 (uit gebruik : vervangen door optie 'a-paal')",
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/variabele-Z30'),
        'vri-met-zwanehals': KeuzelijstWaarde(invulwaarde='vri-met-zwanehals',
                                              label='VRI met zwanehals',
                                              status='verwijderd',
                                              definitie='VRI met zwanehals',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/vri-met-zwanehals'),
        'zwanehals': KeuzelijstWaarde(invulwaarde='zwanehals',
                                      label='zwanehals',
                                      status='ingebruik',
                                      definitie='Een paal met zwanehals (verwijzing naar de bocht in de paal).',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/zwanehals')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

