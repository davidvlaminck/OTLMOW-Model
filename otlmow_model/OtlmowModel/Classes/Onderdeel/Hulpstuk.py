# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkendElement import LinkendElement
from ...Classes.Abstracten.OmhullendeInrichting import OmhullendeInrichting
from ...Datatypes.KlAansluitstukMateriaal import KlAansluitstukMateriaal
from ...Datatypes.KlHulpstukType import KlHulpstukType
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hulpstuk(LinkendElement, OmhullendeInrichting, PuntGeometrie):
    """Stukken die zorgen voor verbindingen tussen buizen en/of leidingen om bv. van richting te veranderen,te verlengen,te verlopen van diameter,meerdere buizen op mekaar aan te sluiten,..."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i')  # i = direction: incoming

        self._inwendigeDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                               naam='inwendigeDiameter',
                                               label='inwendige diameter',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.inwendigeDiameter',
                                               kardinaliteit_max='*',
                                               definition='De diameter van de binnenzijde van het hulpstuk in millimeter.',
                                               owner=self)

        self._materiaal = OTLAttribuut(field=KlAansluitstukMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.materiaal',
                                       definition='Het materiaal waaruit het hulpstuk vervaardigd is.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlHulpstukType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.type',
                                  definition='Het type van het hulpstuk.',
                                  owner=self)

        self._uitwendigeDiameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                                naam='uitwendigeDiameter',
                                                label='uitwendige diameter',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulpstuk.uitwendigeDiameter',
                                                kardinaliteit_max='*',
                                                definition='De diameter van de buitenzijde van het hulpstuk in millimeter.',
                                                owner=self)

    @property
    def inwendigeDiameter(self) -> List[KwantWrdInMillimeterWaarden]:
        """De diameter van de binnenzijde van het hulpstuk in millimeter."""
        return self._inwendigeDiameter.get_waarde()

    @inwendigeDiameter.setter
    def inwendigeDiameter(self, value):
        self._inwendigeDiameter.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit het hulpstuk vervaardigd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van het hulpstuk."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def uitwendigeDiameter(self) -> List[KwantWrdInMillimeterWaarden]:
        """De diameter van de buitenzijde van het hulpstuk in millimeter."""
        return self._uitwendigeDiameter.get_waarde()

    @uitwendigeDiameter.setter
    def uitwendigeDiameter(self, value):
        self._uitwendigeDiameter.set_waarde(value, owner=self)
