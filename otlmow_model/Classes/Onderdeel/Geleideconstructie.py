# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.AansluitendeConstructie import AansluitendeConstructie
from otlmow_model.Classes.Abstracten.EigenschappenVoertuigkering import EigenschappenVoertuigkering
from otlmow_model.Classes.Abstracten.SchokindexVoertuigkering import SchokindexVoertuigkering
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlLEACWerkingsbreedte import KlLEACWerkingsbreedte


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geleideconstructie(AansluitendeConstructie, EigenschappenVoertuigkering, SchokindexVoertuigkering):
    """Een doorlopende afschermende constructie voor voertuigen geïnstalleerd langs de weg of in de middenberm."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AansluitendeConstructie.__init__(self)
        EigenschappenVoertuigkering.__init__(self)
        SchokindexVoertuigkering.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Beginstuk')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dilatatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Eindstuk')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietConformBegin')

        self._isVerwijderbaar = OTLAttribuut(field=BooleanField,
                                             naam='isVerwijderbaar',
                                             label='is verwijderbaar',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie.isVerwijderbaar',
                                             definition='Geleideconstructie kan met minimale moeite tijdelijk worden weggenomen en teruggeplaatst worden.',
                                             owner=self)

        self._werkingsbreedte = OTLAttribuut(field=KlLEACWerkingsbreedte,
                                             naam='werkingsbreedte',
                                             label='werkingsbreedte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie.werkingsbreedte',
                                             definition='Op het voorvlak van een geleideconstructie en loodrecht op de as van de weg gemeten afstand tussen de voorkant van de geleideconstructie in normale positie en de plaats van het verst uitwijkend onderdeel aan de achterzijde van de geleideconstructie bij aanrijding.',
                                             owner=self)

    @property
    def isVerwijderbaar(self) -> bool:
        """Geleideconstructie kan met minimale moeite tijdelijk worden weggenomen en teruggeplaatst worden."""
        return self._isVerwijderbaar.get_waarde()

    @isVerwijderbaar.setter
    def isVerwijderbaar(self, value):
        self._isVerwijderbaar.set_waarde(value, owner=self)

    @property
    def werkingsbreedte(self) -> str:
        """Op het voorvlak van een geleideconstructie en loodrecht op de as van de weg gemeten afstand tussen de voorkant van de geleideconstructie in normale positie en de plaats van het verst uitwijkend onderdeel aan de achterzijde van de geleideconstructie bij aanrijding."""
        return self._werkingsbreedte.get_waarde()

    @werkingsbreedte.setter
    def werkingsbreedte(self, value):
        self._werkingsbreedte.set_waarde(value, owner=self)
