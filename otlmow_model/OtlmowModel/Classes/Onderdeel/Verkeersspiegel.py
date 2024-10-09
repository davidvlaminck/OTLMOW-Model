# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Signalisatie import Signalisatie
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlVerkeersspiegelVorm import KlVerkeersspiegelVorm
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersspiegel(Signalisatie, AIMObject, PuntGeometrie):
    """Een verkeersspiegel is een spiegel die de zichtbaarheid verbetert van het aankomende verkeer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersspiegel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie', direction='u')  # u = unidirectional

        self._bijlageDocument = OTLAttribuut(field=DtcDocument,
                                             naam='bijlageDocument',
                                             label='bijlage document',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersspiegel.bijlageDocument',
                                             kardinaliteit_max='*',
                                             definition='Een document met dossiernummer waardoor men kan terugkoppelen naar de vergunning.',
                                             owner=self)

        self._isGoedgekeurd = OTLAttribuut(field=BooleanField,
                                           naam='isGoedgekeurd',
                                           label='is goedgekeurd',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersspiegel.isGoedgekeurd',
                                           definition='Geeft of de verkeersspiegel al dan niet goedgekeurd is.',
                                           owner=self)

        self._vorm = OTLAttribuut(field=KlVerkeersspiegelVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersspiegel.vorm',
                                  definition='Bepaling van de vorm van de gebruikte verkeersspiegel.',
                                  owner=self)

    @property
    def bijlageDocument(self) -> List[DtcDocumentWaarden]:
        """Een document met dossiernummer waardoor men kan terugkoppelen naar de vergunning."""
        return self._bijlageDocument.get_waarde()

    @bijlageDocument.setter
    def bijlageDocument(self, value):
        self._bijlageDocument.set_waarde(value, owner=self)

    @property
    def isGoedgekeurd(self) -> bool:
        """Geeft of de verkeersspiegel al dan niet goedgekeurd is."""
        return self._isGoedgekeurd.get_waarde()

    @isGoedgekeurd.setter
    def isGoedgekeurd(self, value):
        self._isGoedgekeurd.set_waarde(value, owner=self)

    @property
    def vorm(self) -> str:
        """Bepaling van de vorm van de gebruikte verkeersspiegel."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
