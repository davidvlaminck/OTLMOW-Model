# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordPKMerk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van Pijl-Kruisborden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlDynBordPKMerk'
    label = 'Dyn bord PK merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordPKMerk'
    definition = 'Keuzelijst met de gangbare merken van Pijl-Kruisborden. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordPKMerk'
    options = {
        'swarco': KeuzelijstWaarde(invulwaarde='swarco',
                                   label='Swarco',
                                   status='ingebruik',
                                   definitie='Swarco',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKMerk/swarco')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

