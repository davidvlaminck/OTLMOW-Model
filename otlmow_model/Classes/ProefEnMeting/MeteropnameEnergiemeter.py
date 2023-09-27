# coding=utf-8
from datetime import date
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.DateField import DateField
from otlmow_model.Datatypes.KwantWrdInkWh import KwantWrdInkWh, KwantWrdInkWhWaarden
from otlmow_model.GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MeteropnameEnergiemeter(AIMNaamObject, GeenGeometrie):
    """Resultaten van een meteropname van een energiemeter."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Energiemeter')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterAWV')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNBPiek')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNBReactief')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDerden')

        self._datumMeterstand = OTLAttribuut(field=DateField,
                                             naam='datumMeterstand',
                                             label='datum meterstand dag',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter.datumMeterstand',
                                             definition='De datum van de laatste meteropname van de energiemeter.',
                                             owner=self)

        self._meterstandDag = OTLAttribuut(field=KwantWrdInkWh,
                                           naam='meterstandDag',
                                           label='meterstand dag',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter.meterstandDag',
                                           definition='De meterstand bij de laatste meteropname van de dag-energiemeter.',
                                           owner=self)

        self._meterstandNacht = OTLAttribuut(field=KwantWrdInkWh,
                                             naam='meterstandNacht',
                                             label='meterstand nacht',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter.meterstandNacht',
                                             definition='De meterstand bij de laatste meteropname van de nacht-energiemeter.',
                                             owner=self)

    @property
    def datumMeterstand(self) -> date:
        """De datum van de laatste meteropname van de energiemeter."""
        return self._datumMeterstand.get_waarde()

    @datumMeterstand.setter
    def datumMeterstand(self, value):
        self._datumMeterstand.set_waarde(value, owner=self)

    @property
    def meterstandDag(self) -> KwantWrdInkWhWaarden:
        """De meterstand bij de laatste meteropname van de dag-energiemeter."""
        return self._meterstandDag.get_waarde()

    @meterstandDag.setter
    def meterstandDag(self, value):
        self._meterstandDag.set_waarde(value, owner=self)

    @property
    def meterstandNacht(self) -> KwantWrdInkWhWaarden:
        """De meterstand bij de laatste meteropname van de nacht-energiemeter."""
        return self._meterstandNacht.get_waarde()

    @meterstandNacht.setter
    def meterstandNacht(self, value):
        self._meterstandNacht.set_waarde(value, owner=self)
