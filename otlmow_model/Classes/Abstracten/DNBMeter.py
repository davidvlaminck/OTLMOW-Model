# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.Energiemeter import Energiemeter
from otlmow_model.Datatypes.KlEnergiemeterDNBMeteropnameFrequentie import KlEnergiemeterDNBMeteropnameFrequentie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DNBMeter(Energiemeter):
    """Abstracte voor elk toestel dat eigendom is van de distributienetbeheerder en in de installatie van de asset beheerder geplaatst wordt voor diverse metingen van doorgevoerde energie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring')

        self._meteropnameFrequentie = OTLAttribuut(field=KlEnergiemeterDNBMeteropnameFrequentie,
                                                   naam='meteropnameFrequentie',
                                                   label='meteropname frequentie',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter.meteropnameFrequentie',
                                                   definition='Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder.',
                                                   owner=self)

    @property
    def meteropnameFrequentie(self) -> str:
        """Frequentie waarmee de meterstand opgenomen wordt door de netbeheerder."""
        return self._meteropnameFrequentie.get_waarde()

    @meteropnameFrequentie.setter
    def meteropnameFrequentie(self, value):
        self._meteropnameFrequentie.set_waarde(value, owner=self)
