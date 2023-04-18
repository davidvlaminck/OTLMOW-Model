# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.DNBMeter import DNBMeter
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlEnergiemeterDNBUurtarief import KlEnergiemeterDNBUurtarief


# Generated with OTLClassCreator. To modify: extend, do not edit
class EnergiemeterDNB(DNBMeter):
    """Toestel dat eigendom is van de distributienetbeheerder en in de installatie van de asset beheerder geplaatst wordt voor het meten van het energieverbruik van de betreffende installatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking')

        self._isGecombineerdeEnergiemeter = OTLAttribuut(field=BooleanField,
                                                         naam='isGecombineerdeEnergiemeter',
                                                         label='is gecombineerde energiemeter',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB.isGecombineerdeEnergiemeter',
                                                         definition='Geeft aan of de meter naast de gewone verbruiksmeting ook reactief vermogen en piek metingen doet.',
                                                         owner=self)

        self._uurtarief = OTLAttribuut(field=KlEnergiemeterDNBUurtarief,
                                       naam='uurtarief',
                                       label='uurtarief',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB.uurtarief',
                                       definition='Type uurtarief vb enkelvoudig, dubbelvoudig,...',
                                       owner=self)

    @property
    def isGecombineerdeEnergiemeter(self) -> bool:
        """Geeft aan of de meter naast de gewone verbruiksmeting ook reactief vermogen en piek metingen doet."""
        return self._isGecombineerdeEnergiemeter.get_waarde()

    @isGecombineerdeEnergiemeter.setter
    def isGecombineerdeEnergiemeter(self, value):
        self._isGecombineerdeEnergiemeter.set_waarde(value, owner=self)

    @property
    def uurtarief(self) -> str:
        """Type uurtarief vb enkelvoudig, dubbelvoudig,..."""
        return self._uurtarief.get_waarde()

    @uurtarief.setter
    def uurtarief(self, value):
        self._uurtarief.set_waarde(value, owner=self)
