# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.BijlageVoertuigkering import BijlageVoertuigkering
from otlmow_model.Classes.Abstracten.EigenschappenVoertuigkering import EigenschappenVoertuigkering
from otlmow_model.Classes.Abstracten.Geluidsschermelement import Geluidsschermelement
from otlmow_model.Classes.Abstracten.SchokindexVoertuigkering import SchokindexVoertuigkering
from otlmow_model.Datatypes.KlLEACWerkingsbreedte import KlLEACWerkingsbreedte


# Generated with OTLClassCreator. To modify: extend, do not edit
class VoertuigkerendGeluidsschermelement(BijlageVoertuigkering, EigenschappenVoertuigkering, Geluidsschermelement, SchokindexVoertuigkering):
    """Dit zijn schermelementen met een voet in de vorm van een T. Op de voet worden deltablocs geplaatst die een stabiliserende en voertuigkerende functie hebben."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoertuigkerendGeluidsschermelement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BevestigingGC')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementenGC')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfschermendeConstructie')

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
