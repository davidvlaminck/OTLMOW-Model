# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlTypeSpankabel import KlTypeSpankabel
from otlmow_model.Datatypes.KwantWrdInVierkanteMillimeter import KwantWrdInVierkanteMillimeter, KwantWrdInVierkanteMillimeterWaarden
from otlmow_model.BaseClasses.NonNegIntegerField import NonNegIntegerField
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Spankabel(AIMNaamObject, LijnGeometrie):
    """Een kabel die gebruikt kan worden als externe naspanning of als wapening."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spankabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ExterneNaspanning')

        self._aantalDradenStrengen = OTLAttribuut(field=NonNegIntegerField,
                                                  naam='aantalDradenStrengen',
                                                  label='aantal draden of strengen',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spankabel.aantalDradenStrengen',
                                                  definition='Het aantal draden of strengen die de kabel bevat.',
                                                  owner=self)

        self._doorsnedeDradenStrengen = OTLAttribuut(field=KwantWrdInVierkanteMillimeter,
                                                     naam='doorsnedeDradenStrengen',
                                                     label='doorsnede draden of strengen',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spankabel.doorsnedeDradenStrengen',
                                                     definition='De doorsnede van de draden of strengen in de kabel, uitgedrukt in vierkante millimeter.',
                                                     owner=self)

        self._totaleSectieSpankabel = OTLAttribuut(field=KwantWrdInVierkanteMillimeter,
                                                   naam='totaleSectieSpankabel',
                                                   label='totale sectie spankabel',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spankabel.totaleSectieSpankabel',
                                                   definition='De doorsnede van de gehele spankabel, uitgedrukt in vierkante millimeter.',
                                                   owner=self)

        self._typeKabel = OTLAttribuut(field=KlTypeSpankabel,
                                       naam='typeKabel',
                                       label='type kabel',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spankabel.typeKabel',
                                       definition='Het type waaruit de spankabel is opgebouwd.',
                                       owner=self)

    @property
    def aantalDradenStrengen(self) -> int:
        """Het aantal draden of strengen die de kabel bevat."""
        return self._aantalDradenStrengen.get_waarde()

    @aantalDradenStrengen.setter
    def aantalDradenStrengen(self, value):
        self._aantalDradenStrengen.set_waarde(value, owner=self)

    @property
    def doorsnedeDradenStrengen(self) -> KwantWrdInVierkanteMillimeterWaarden:
        """De doorsnede van de draden of strengen in de kabel, uitgedrukt in vierkante millimeter."""
        return self._doorsnedeDradenStrengen.get_waarde()

    @doorsnedeDradenStrengen.setter
    def doorsnedeDradenStrengen(self, value):
        self._doorsnedeDradenStrengen.set_waarde(value, owner=self)

    @property
    def totaleSectieSpankabel(self) -> KwantWrdInVierkanteMillimeterWaarden:
        """De doorsnede van de gehele spankabel, uitgedrukt in vierkante millimeter."""
        return self._totaleSectieSpankabel.get_waarde()

    @totaleSectieSpankabel.setter
    def totaleSectieSpankabel(self, value):
        self._totaleSectieSpankabel.set_waarde(value, owner=self)

    @property
    def typeKabel(self) -> str:
        """Het type waaruit de spankabel is opgebouwd."""
        return self._typeKabel.get_waarde()

    @typeKabel.setter
    def typeKabel(self, value):
        self._typeKabel.set_waarde(value, owner=self)
