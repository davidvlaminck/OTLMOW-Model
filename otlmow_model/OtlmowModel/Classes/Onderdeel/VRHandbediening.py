# coding=utf-8
from ...Classes.Abstracten.VRModuleZFirmware import VRModuleZFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRHandbediening(VRModuleZFirmware):
    """Module voor het met de hand bedienen van de verkeersregelaar (bv. in stappen doorlopen van het V-plan, alles op rood zetten, alles op knipper zetten,...), dit kan enkel ingeschakeld worden door een sleutel aanwezig in het sleutelcontact."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRHandbediening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
