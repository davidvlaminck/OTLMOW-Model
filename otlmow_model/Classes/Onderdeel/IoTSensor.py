# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcCompacteBatterij import DtcCompacteBatterij, DtcCompacteBatterijWaarden
from otlmow_model.Datatypes.KlIoTSensorMerk import KlIoTSensorMerk
from otlmow_model.Datatypes.KlIoTSensorModelnaam import KlIoTSensorModelnaam
from otlmow_model.Datatypes.KlIoTSensorParameter import KlIoTSensorParameter
from otlmow_model.Datatypes.KlIoTSensorVerbindingstype import KlIoTSensorVerbindingstype
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IoTSensor(AIMNaamObject, PuntGeometrie):
    """Een sensor die veranderingen in de omgeving registreert en erop reageert."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang')

        self._batterij = OTLAttribuut(field=DtcCompacteBatterij,
                                      naam='batterij',
                                      label='batterij',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor.batterij',
                                      definition='Bevat de informatie van de inwendige compacte batterij.',
                                      owner=self)

        self._gemetenParameters = OTLAttribuut(field=KlIoTSensorParameter,
                                               naam='gemetenParameters',
                                               label='gemeten parameters',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor.gemetenParameters',
                                               kardinaliteit_max='*',
                                               definition='De mogelijke parameters die kunnen gemeten worden door de IoT-sensor.',
                                               owner=self)

        self._merk = OTLAttribuut(field=KlIoTSensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor.merk',
                                  definition='Het merk van een IoT-sensor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlIoTSensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor.modelnaam',
                                       definition='De modelnaam van een IoT-sensor.',
                                       owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor.serienummer',
                                         definition='Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is.',
                                         owner=self)

        self._typeVerbinding = OTLAttribuut(field=KlIoTSensorVerbindingstype,
                                            naam='typeVerbinding',
                                            label='type verbinding',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IoTSensor.typeVerbinding',
                                            definition='De manier van de communicatieverbinding van de IoT-sensor.',
                                            owner=self)

    @property
    def batterij(self) -> DtcCompacteBatterijWaarden:
        """Bevat de informatie van de inwendige compacte batterij."""
        return self._batterij.get_waarde()

    @batterij.setter
    def batterij(self, value):
        self._batterij.set_waarde(value, owner=self)

    @property
    def gemetenParameters(self) -> List[str]:
        """De mogelijke parameters die kunnen gemeten worden door de IoT-sensor."""
        return self._gemetenParameters.get_waarde()

    @gemetenParameters.setter
    def gemetenParameters(self, value):
        self._gemetenParameters.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van een IoT-sensor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van een IoT-sensor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def serienummer(self) -> str:
        """Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)

    @property
    def typeVerbinding(self) -> str:
        """De manier van de communicatieverbinding van de IoT-sensor."""
        return self._typeVerbinding.get_waarde()

    @typeVerbinding.setter
    def typeVerbinding(self, value):
        self._typeVerbinding.set_waarde(value, owner=self)
