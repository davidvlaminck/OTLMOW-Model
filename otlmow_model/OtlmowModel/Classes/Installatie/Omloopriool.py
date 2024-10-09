# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.KlDroogzetbaarheidOmloopriool import KlDroogzetbaarheidOmloopriool
from ...Datatypes.KwantWrdInMeterPerSeconde import KwantWrdInMeterPerSeconde, KwantWrdInMeterPerSecondeWaarden
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Omloopriool(AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """Een vaste waterbouwkundige constructie voor het nivelleren van een sluis."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Omloopriool'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondkeringen', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie', direction='o')  # o = direction: outgoing

        self._droogzetbaarheid = OTLAttribuut(field=KlDroogzetbaarheidOmloopriool,
                                              naam='droogzetbaarheid',
                                              label='droogzetbaarheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Omloopriool.droogzetbaarheid',
                                              definition='De verschillende mogelijkheden m.b.t. droogzetbaarheid.',
                                              owner=self)

        self._heeftOntluchtingskanaal = OTLAttribuut(field=BooleanField,
                                                     naam='heeftOntluchtingskanaal',
                                                     label='heeft ontluchtingskanaal',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Omloopriool.heeftOntluchtingskanaal',
                                                     definition='Geeft aan of er een ontluchtingskanaal aanwezig is.',
                                                     owner=self)

        self._natteSectie = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='natteSectie',
                                         label='nattesectie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Omloopriool.natteSectie',
                                         definition='De natte sectie van het omloopriool uitgedrukt in vierkante meter',
                                         owner=self)

        self._stroomsnelheid = OTLAttribuut(field=KwantWrdInMeterPerSeconde,
                                            naam='stroomsnelheid',
                                            label='stroomsnelheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Omloopriool.stroomsnelheid',
                                            definition='De stroomsnelheid bij maximaal verval binnen het omloopriool uitgedrukt in m/s.',
                                            owner=self)

    @property
    def droogzetbaarheid(self) -> str:
        """De verschillende mogelijkheden m.b.t. droogzetbaarheid."""
        return self._droogzetbaarheid.get_waarde()

    @droogzetbaarheid.setter
    def droogzetbaarheid(self, value):
        self._droogzetbaarheid.set_waarde(value, owner=self)

    @property
    def heeftOntluchtingskanaal(self) -> bool:
        """Geeft aan of er een ontluchtingskanaal aanwezig is."""
        return self._heeftOntluchtingskanaal.get_waarde()

    @heeftOntluchtingskanaal.setter
    def heeftOntluchtingskanaal(self, value):
        self._heeftOntluchtingskanaal.set_waarde(value, owner=self)

    @property
    def natteSectie(self) -> KwantWrdInVierkanteMeterWaarden:
        """De natte sectie van het omloopriool uitgedrukt in vierkante meter"""
        return self._natteSectie.get_waarde()

    @natteSectie.setter
    def natteSectie(self, value):
        self._natteSectie.set_waarde(value, owner=self)

    @property
    def stroomsnelheid(self) -> KwantWrdInMeterPerSecondeWaarden:
        """De stroomsnelheid bij maximaal verval binnen het omloopriool uitgedrukt in m/s."""
        return self._stroomsnelheid.get_waarde()

    @stroomsnelheid.setter
    def stroomsnelheid(self, value):
        self._stroomsnelheid.set_waarde(value, owner=self)
