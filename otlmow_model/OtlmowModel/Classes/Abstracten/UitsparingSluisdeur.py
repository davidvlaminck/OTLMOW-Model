# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlVastAanslagmateriaal import KlVastAanslagmateriaal
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class UitsparingSluisdeur(VlakGeometrie):
    """Een abstracte om eigenschappen en relaties van de uitsparingen te bundelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#UitsparingSluisdeur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluishoofd', direction='o')  # o = direction: outgoing

        self._detailplan = OTLAttribuut(field=DtcDocument,
                                        naam='detailplan',
                                        label='detailplan',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#UitsparingSluisdeur.detailplan',
                                        definition='Het detailplan van de uitsparing.',
                                        owner=self)

        self._vastAanslagmateriaal = OTLAttribuut(field=KlVastAanslagmateriaal,
                                                  naam='vastAanslagmateriaal',
                                                  label='vast aanslagmateriaal',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#UitsparingSluisdeur.vastAanslagmateriaal',
                                                  definition='De verschillende mogelijkheden m.b.t. het materiaal van de aanslag',
                                                  owner=self)

    @property
    def detailplan(self) -> DtcDocumentWaarden:
        """Het detailplan van de uitsparing."""
        return self._detailplan.get_waarde()

    @detailplan.setter
    def detailplan(self, value):
        self._detailplan.set_waarde(value, owner=self)

    @property
    def vastAanslagmateriaal(self) -> str:
        """De verschillende mogelijkheden m.b.t. het materiaal van de aanslag"""
        return self._vastAanslagmateriaal.get_waarde()

    @vastAanslagmateriaal.setter
    def vastAanslagmateriaal(self, value):
        self._vastAanslagmateriaal.set_waarde(value, owner=self)
