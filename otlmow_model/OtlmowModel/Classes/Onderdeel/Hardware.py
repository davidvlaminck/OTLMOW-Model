# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.HardwareToegang import HardwareToegang
from otlmow_model.OtlmowModel.BaseClasses.IntegerField import IntegerField
from ...Datatypes.KlHardwareMerk import KlHardwareMerk
from ...Datatypes.KlHardwareModelnaam import KlHardwareModelnaam
from ...Datatypes.KlHardwareVormfactor import KlHardwareVormfactor
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hardware(HardwareToegang, PuntGeometrie):
    """Fysieke componenten of onderdelen van een computer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cluster', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dongle', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsSWGehostOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='i')  # i = direction: incoming

        self._aantalUnits = OTLAttribuut(field=IntegerField,
                                         naam='aantalUnits',
                                         label='aantal units',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.aantalUnits',
                                         definition='Het aantal units dat een server in een rack inneemt.',
                                         owner=self)

        self._merk = OTLAttribuut(field=KlHardwareMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.merk',
                                  definition='Het merk van de hardware.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlHardwareModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.modelnaam',
                                       definition='De modelnaam van de hardware.',
                                       owner=self)

        self._vormfactor = OTLAttribuut(field=KlHardwareVormfactor,
                                        naam='vormfactor',
                                        label='vormfactor',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware.vormfactor',
                                        definition='Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven.',
                                        owner=self)

    @property
    def aantalUnits(self) -> int:
        """Het aantal units dat een server in een rack inneemt."""
        return self._aantalUnits.get_waarde()

    @aantalUnits.setter
    def aantalUnits(self, value):
        self._aantalUnits.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de hardware."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de hardware."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def vormfactor(self) -> str:
        """Het soort toestel waarin de fysieke componenten of onderdelen worden vormgegeven."""
        return self._vormfactor.get_waarde()

    @vormfactor.setter
    def vormfactor(self, value):
        self._vormfactor.set_waarde(value, owner=self)
