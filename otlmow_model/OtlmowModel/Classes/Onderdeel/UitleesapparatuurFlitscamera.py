# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class UitleesapparatuurFlitscamera(NaampadObject, PuntGeometrie):
    """Apparatuur die door de lokale politie wordt gebruikt voor het uitlezen van beelden die gemaakt zijn door niet-digitale, onbemande flitscamera’s."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UitleesapparatuurFlitscamera'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
