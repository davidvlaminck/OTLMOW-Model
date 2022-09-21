# coding=utf-8
from otlmow_model.Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BiFlashInstallatie(NaampadObject, PuntGeometrie):
    """Het geheel van twee bi-flashsteunen, seinlantaarns, retroreflecterende verkeersborden en hun aansluiting, beveiligingsapparatuur en sturing op een bepaalde locatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BiFlashInstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        NaampadObject.__init__(self)
        PuntGeometrie.__init__(self)
