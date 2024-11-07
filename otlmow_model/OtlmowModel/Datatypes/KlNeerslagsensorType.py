# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNeerslagsensorType(KeuzelijstField):
    """Het type van de neerslagsensor."""
    naam = 'KlNeerslagsensorType'
    label = 'Neerslagsensor type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNeerslagsensorType'
    definition = 'Het type van de neerslagsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNeerslagsensorType'
    options = {
        'capacitief': KeuzelijstWaarde(invulwaarde='capacitief',
                                       label='capacitief',
                                       status='ingebruik',
                                       definitie='Een type sensor dat neerslag (sneeuw, regen, hagel) detecteert door veranderingen in de elektrische capaciteit op te merken. Wanneer neerslag (sneeuw, regen, hagel) op het sensoroppervlak komt, verandert de capaciteit door de aanwezigheid van deze neerslag, wat wordt gedetecteerd door de sensor.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorType/capacitief'),
        'optisch': KeuzelijstWaarde(invulwaarde='optisch',
                                    label='optisch',
                                    status='ingebruik',
                                    definitie='Detecteert neerslag (sneeuw, regen, hagel) door licht te gebruiken. Wanneer bv. regendruppels op het oppervlak van de sensor vallen, verstrooien ze het licht, wat de sensor registreert als een verandering in de lichtintensiteit. Deze verstrooiing of vermindering van licht geeft aan dat er neerslag aanwezig is.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorType/optisch'),
        'radar': KeuzelijstWaarde(invulwaarde='radar',
                                  label='radar',
                                  status='ingebruik',
                                  definitie='Detecteert neerslag (sneeuw, regen, hagel) door gebruik te maken van radartechnologie. Dit type sensor zendt radargolven uit en analyseert de reflectie van deze golven op vallende neerslag.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorType/radar')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

