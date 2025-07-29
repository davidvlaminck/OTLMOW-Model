# coding=utf-8
from ...Classes.Abstracten.PTModuleZFirmware import PTModuleZFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTDemodulatoren(PTModuleZFirmware):
    """De functie van de demodulator bestaat erin de data,ontvangen door de lus,te decoderen en in het juiste formaat door te sturen naar de centrale verwerkingseenheid,de PT-verwerkingseenheid."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTDemodulatoren'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTVerwerkingseenheid', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus', direction='u')  # u = unidirectional
