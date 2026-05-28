# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypePut(KeuzelijstField):
    """Soort van funderingsput."""
    naam = 'KlTypePut'
    label = 'type put'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypePut'
    definition = 'Soort van funderingsput.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypePut'
    options = {
        'beschoeide-put': KeuzelijstWaarde(invulwaarde='beschoeide-put',
                                           label='beschoeide put',
                                           status='ingebruik',
                                           definitie='Een put waarbij de grond laagsgewijs wordt weggegraven en de putwanden systematisch worden beschoeid met houten balken, met betonplaatjes of met stalen plaatjes.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypePut/beschoeide-put'),
        'valse-put': KeuzelijstWaarde(invulwaarde='valse-put',
                                      label='valse put',
                                      status='ingebruik',
                                      definitie='Een cirkelvormige put waarbij de grond mechanisch wordt uitgegraven, al dan niet binnen een recupereerbare cirkelvormige mantelbuis.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypePut/valse-put'),
        'zinkput-of-caisson': KeuzelijstWaarde(invulwaarde='zinkput-of-caisson',
                                               label='zinkput of caisson',
                                               status='ingebruik',
                                               definitie='Een put waarbij de grond wordt uitgegraven binnen gewapende betonringen die in de grond worden achtergelaten. Het verschil tussen zinkputten en valse putten is de grootte van de put.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypePut/zinkput-of-caisson')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

