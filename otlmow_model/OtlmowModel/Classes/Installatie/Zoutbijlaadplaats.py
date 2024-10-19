# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zoutbijlaadplaats(NaampadObject, VlakGeometrie):
    """Site in het beheer van een district,waar strooiwagens zout of pekel kunnen bijladen,wanneer ze tijdens de winterdienst hun strooiroute afleggen. De leverancier kan toegang krijgen (badge of codeklavier) om de tanks of de silo’s terug te vullen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zoutbijlaadplaats'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiting', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Badgelezer', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBLaagspanning', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank', direction='i')  # i = direction: incoming

        self._opstellingsplan = OTLAttribuut(field=DtcDocument,
                                             naam='opstellingsplan',
                                             label='opstellingsplan',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zoutbijlaadplaats.opstellingsplan',
                                             definition='Een plan dat de opstelling van alle infrastructuurelementen op de site aangeeft.',
                                             owner=self)

    @property
    def opstellingsplan(self) -> DtcDocumentWaarden:
        """Een plan dat de opstelling van alle infrastructuurelementen op de site aangeeft."""
        return self._opstellingsplan.get_waarde()

    @opstellingsplan.setter
    def opstellingsplan(self, value):
        self._opstellingsplan.set_waarde(value, owner=self)
