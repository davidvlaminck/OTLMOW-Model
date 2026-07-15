# coding=utf-8
from typing import List
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie
from ...Datatypes.DtcDienstdatum import DtcDienstdatum, DtcDienstdatumWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftVPlan(DirectioneleRelatie):
    """Deze relatie duidt aan welke V plannen gekoppeld zijn aan een verkeersregelinstallatie en/of ITSapp, met aanduiding van de periode waarin deze koppeling geldig is via een indienstdatum en uitdienstdatum."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftVPlan'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._dienstdatum = OTLAttribuut(field=DtcDienstdatum,
                                         naam='dienstdatum',
                                         label='dienstdatum',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftVPlan.dienstdatum',
                                         kardinaliteit_max='*',
                                         definition='De datum(s) waarop een V-plan indienst of uitdienst werd genomen.',
                                         owner=self)

    @property
    def dienstdatum(self) -> List[DtcDienstdatumWaarden]:
        """De datum(s) waarop een V-plan indienst of uitdienst werd genomen."""
        return self._dienstdatum.get_waarde()

    @dienstdatum.setter
    def dienstdatum(self, value):
        self._dienstdatum.set_waarde(value, owner=self)
