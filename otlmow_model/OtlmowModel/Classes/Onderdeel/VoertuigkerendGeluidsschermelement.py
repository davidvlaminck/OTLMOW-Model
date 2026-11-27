# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BijlageVoertuigkering import BijlageVoertuigkering
from ...Classes.Abstracten.EigenschappenVoertuigkering import (
    EigenschappenVoertuigkering,
)
from ...Classes.Abstracten.Geluidsschermelement import Geluidsschermelement
from ...Classes.Abstracten.SchokindexVoertuigkering import SchokindexVoertuigkering
from ...Datatypes.KlLEACWerkingsbreedte import KlLEACWerkingsbreedte


# Generated with OTLClassCreator. To modify: extend, do not edit
class VoertuigkerendGeluidsschermelement(BijlageVoertuigkering, EigenschappenVoertuigkering, Geluidsschermelement, SchokindexVoertuigkering):
    """Dit zijn schermelementen met een voet in de vorm van een T. Op de voet worden deltablocs geplaatst die een stabiliserende en voertuigkerende functie hebben."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoertuigkerendGeluidsschermelement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BevestigingGC', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementenGC', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Geluidsschermelement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietConformBegin', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._werkingsbreedte = OTLAttribuut(field=KlLEACWerkingsbreedte,
                                             naam='werkingsbreedte',
                                             label='werkingsbreedte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoertuigkerendGeluidsschermelement.werkingsbreedte',
                                             definition='Dit is de afstand, op het voorvlak van een schermelement en loodrecht op de as van de weg gemeten, tussen de voorkant van het schermelement in normale positie en de plaats van het verst uitwijkend onderdeel aan de achterzijde van het schermelement bij aanrijding.',
                                             owner=self)

    @property
    def werkingsbreedte(self) -> str:
        """Dit is de afstand, op het voorvlak van een schermelement en loodrecht op de as van de weg gemeten, tussen de voorkant van het schermelement in normale positie en de plaats van het verst uitwijkend onderdeel aan de achterzijde van het schermelement bij aanrijding."""
        return self._werkingsbreedte.get_waarde()

    @werkingsbreedte.setter
    def werkingsbreedte(self, value):
        self._werkingsbreedte.set_waarde(value, owner=self)
