# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVeiligheidsrelaisModelnaam(KeuzelijstField):
    """Een lijst met modelnamen van veilgheidsrelais volgens de fabrikant."""
    naam = 'KlVeiligheidsrelaisModelnaam'
    label = 'Veiligheidsrelais modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVeiligheidsrelaisModelnaam'
    definition = 'Een lijst met modelnamen van veilgheidsrelais volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVeiligheidsrelaisModelnaam'
    options = {
        'pnoz-x7': KeuzelijstWaarde(invulwaarde='pnoz-x7',
                                    label='PNOZ-X7',
                                    status='ingebruik',
                                    definitie='PNOZ-X7',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVeiligheidsrelaisModelnaam/pnoz-x7')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

