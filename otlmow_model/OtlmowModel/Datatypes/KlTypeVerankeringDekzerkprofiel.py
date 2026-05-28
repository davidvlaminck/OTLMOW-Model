# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeVerankeringDekzerkprofiel(KeuzelijstField):
    """Lijst met de verschillende opties voor de verankering van een dekzerkprofiel."""
    naam = 'KlTypeVerankeringDekzerkprofiel'
    label = 'type verankering dekzerkprofiel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeVerankeringDekzerkprofiel'
    definition = 'Lijst met de verschillende opties voor de verankering van een dekzerkprofiel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeVerankeringDekzerkprofiel'
    options = {
        'deuvels': KeuzelijstWaarde(invulwaarde='deuvels',
                                    label='deuvels',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVerankeringDekzerkprofiel/deuvels'),
        'plaatstaal-met-zwaluwstaarten': KeuzelijstWaarde(invulwaarde='plaatstaal-met-zwaluwstaarten',
                                                          label='plaatstaal met zwaluwstaarten',
                                                          status='ingebruik',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVerankeringDekzerkprofiel/plaatstaal-met-zwaluwstaarten')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

