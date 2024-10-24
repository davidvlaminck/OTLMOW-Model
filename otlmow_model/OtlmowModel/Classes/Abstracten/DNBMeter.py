# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.Abstracten.Energiemeter import Energiemeter
from ...Datatypes.KlEnergiemeterDNBMeteropnameFrequentie import KlEnergiemeterDNBMeteropnameFrequentie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DNBMeter(Energiemeter):
    """Abstracte voor elk toestel dat eigendom is van de distributienetbeheerder en in de installatie van de asset beheerder geplaatst wordt voor diverse metingen van doorgevoerde energie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#MeteropnameEnergiemeter', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator', direction='i')  # i = direction: incoming

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
