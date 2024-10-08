# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeOplegging(KeuzelijstField):
    """De soort van oplegging."""
    naam = 'KlTypeOplegging'
    label = 'Type oplegging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeOplegging'
    definition = 'De soort van oplegging.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeOplegging'
    options = {
        'betonnen-oplegging-freyssinetscharnier': KeuzelijstWaarde(invulwaarde='betonnen-oplegging-freyssinetscharnier',
                                                                   label='Betonnen oplegging - Freyssinetscharnier',
                                                                   status='ingebruik',
                                                                   definitie='Betonnen oplegging die ontstaat door een plaatselijke vernauwing, over een hoogte van niet meer dan 2 cm, van de doorsnede die de drukkracht overbrengt.',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeOplegging/betonnen-oplegging-freyssinetscharnier'),
        'betonnen-oplegging-mesnagerscharnier': KeuzelijstWaarde(invulwaarde='betonnen-oplegging-mesnagerscharnier',
                                                                 label='Betonnen oplegging - Mesnagerscharnier',
                                                                 status='ingebruik',
                                                                 definitie='Betonnen oplegging die uit kruiselings geplaatste wapeningsstaven bestaat. Deze wapeningsstaven zijn niet ingestort over een lengte van ongeveer tienmaal hun diameter.',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeOplegging/betonnen-oplegging-mesnagerscharnier'),
        'rubber-oplegging': KeuzelijstWaarde(invulwaarde='rubber-oplegging',
                                             label='Rubber oplegging',
                                             status='ingebruik',
                                             definitie='Rubber oplegging',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeOplegging/rubber-oplegging'),
        'stalen-oplegging-roloplegging': KeuzelijstWaarde(invulwaarde='stalen-oplegging-roloplegging',
                                                          label='Stalen oplegging - roloplegging',
                                                          status='ingebruik',
                                                          definitie='Rolopleggingen bieden een oplossing voor het overdragen van oplegkrachten verticaal en horizontaal en tegelijkertijd ook het mogelijk maken van translaties en kleine rotaties met een geringe weerstand.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeOplegging/stalen-oplegging-roloplegging')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

