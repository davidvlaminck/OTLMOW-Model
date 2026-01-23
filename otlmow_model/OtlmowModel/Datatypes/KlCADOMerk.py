# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCADOMerk(KeuzelijstField):
    """Het merk van de calamiteitendoorsteek."""
    naam = 'KlCADOMerk'
    label = 'Calamiteitendoorsteek merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCADOMerk'
    definition = 'Het merk van de calamiteitendoorsteek.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCADOMerk'
    options = {
        'heintzmann': KeuzelijstWaarde(invulwaarde='heintzmann',
                                       label='Heintzmann',
                                       status='ingebruik',
                                       definitie='Heintzmann',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCADOMerk/heintzmann')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

