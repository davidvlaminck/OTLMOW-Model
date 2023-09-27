# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlTransformatorIsolatiemedium import KlTransformatorIsolatiemedium
from otlmow_model.Datatypes.KlTransformatorTrafobeveiliging import KlTransformatorTrafobeveiliging
from otlmow_model.Datatypes.KlVerliezenType import KlVerliezenType
from otlmow_model.Datatypes.KwantWrdInKiloVolt import KwantWrdInKiloVolt, KwantWrdInKiloVoltWaarden
from otlmow_model.Datatypes.KwantWrdInKiloVoltAmpere import KwantWrdInKiloVoltAmpere, KwantWrdInKiloVoltAmpereWaarden
from otlmow_model.Datatypes.KwantWrdInProcent import KwantWrdInProcent, KwantWrdInProcentWaarden
from otlmow_model.Datatypes.KwantWrdInVolt import KwantWrdInVolt, KwantWrdInVoltWaarden
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Transformator(AIMNaamObject, PuntGeometrie):
    """Elektrische apparatuur,bestaande uit magnetisch gekoppelde spoelen,die instaat voor het transformeren van de voedingsspanning."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabine')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring')

        self._isGalvanischGescheiden = OTLAttribuut(field=BooleanField,
                                                    naam='isGalvanischGescheiden',
                                                    label='is galvanisch gescheiden',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.isGalvanischGescheiden',
                                                    definition='Geeft aan of de transformator al dan niet galvanisch gescheiden is.',
                                                    owner=self)

        self._isolatiemedium = OTLAttribuut(field=KlTransformatorIsolatiemedium,
                                            naam='isolatiemedium',
                                            label='isolatiemedium',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.isolatiemedium',
                                            definition='Wijze van onderdompeling van de magnetische kring en van de wikkelingen van de transformator.',
                                            owner=self)

        self._kortsluitspanning = OTLAttribuut(field=KwantWrdInProcent,
                                               naam='kortsluitspanning',
                                               label='kortsluitspanning',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.kortsluitspanning',
                                               definition='Kortsluitspanning van de transformator (in %).',
                                               owner=self)

        self._nominaalVermogen = OTLAttribuut(field=KwantWrdInKiloVoltAmpere,
                                              naam='nominaalVermogen',
                                              label='nominaal vermogen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.nominaalVermogen',
                                              definition='nominale vermogen van de transformator.',
                                              owner=self)

        self._nominalePrimaireSpanning = OTLAttribuut(field=KwantWrdInKiloVolt,
                                                      naam='nominalePrimaireSpanning',
                                                      label='nominale primaire spanning',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.nominalePrimaireSpanning',
                                                      definition='Nominale spanning van de primaire wikkeling in kV.',
                                                      owner=self)

        self._nominaleSecundaireSpanning = OTLAttribuut(field=KwantWrdInVolt,
                                                        naam='nominaleSecundaireSpanning',
                                                        label='nominale secundaire spanning',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.nominaleSecundaireSpanning',
                                                        definition='Nominale spanning van de secundaire wikkeling in V.',
                                                        owner=self)

        self._schakelgroep = OTLAttribuut(field=StringField,
                                          naam='schakelgroep',
                                          label='schakelgroep',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.schakelgroep',
                                          definition='Verzameling van 3 schakelcombinaties waarbij de hoofdletter de schakelwijze van de primaire weergeeft, de kleine letter(s) de schakelwijze van de secundaire weergeeft (en eventueel het feit dat het sterpunt naar buiten werd gebracht) en het getal geeft het klokgetal (of het aantal keer dat er 30° faseverschuiving tussen HS- en LS-spanning is) vb Dyn11',
                                          owner=self)

        self._typeBeveiliging = OTLAttribuut(field=KlTransformatorTrafobeveiliging,
                                             naam='typeBeveiliging',
                                             label='type beveiliging',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.typeBeveiliging',
                                             definition='Type transformatorbeveiliging.',
                                             owner=self)

        self._typeVerliezen = OTLAttribuut(field=KlVerliezenType,
                                           naam='typeVerliezen',
                                           label='type verliezen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.typeVerliezen',
                                           definition='Type verliezen.',
                                           owner=self)

    @property
    def isGalvanischGescheiden(self) -> bool:
        """Geeft aan of de transformator al dan niet galvanisch gescheiden is."""
        return self._isGalvanischGescheiden.get_waarde()

    @isGalvanischGescheiden.setter
    def isGalvanischGescheiden(self, value):
        self._isGalvanischGescheiden.set_waarde(value, owner=self)

    @property
    def isolatiemedium(self) -> str:
        """Wijze van onderdompeling van de magnetische kring en van de wikkelingen van de transformator."""
        return self._isolatiemedium.get_waarde()

    @isolatiemedium.setter
    def isolatiemedium(self, value):
        self._isolatiemedium.set_waarde(value, owner=self)

    @property
    def kortsluitspanning(self) -> KwantWrdInProcentWaarden:
        """Kortsluitspanning van de transformator (in %)."""
        return self._kortsluitspanning.get_waarde()

    @kortsluitspanning.setter
    def kortsluitspanning(self, value):
        self._kortsluitspanning.set_waarde(value, owner=self)

    @property
    def nominaalVermogen(self) -> KwantWrdInKiloVoltAmpereWaarden:
        """nominale vermogen van de transformator."""
        return self._nominaalVermogen.get_waarde()

    @nominaalVermogen.setter
    def nominaalVermogen(self, value):
        self._nominaalVermogen.set_waarde(value, owner=self)

    @property
    def nominalePrimaireSpanning(self) -> KwantWrdInKiloVoltWaarden:
        """Nominale spanning van de primaire wikkeling in kV."""
        return self._nominalePrimaireSpanning.get_waarde()

    @nominalePrimaireSpanning.setter
    def nominalePrimaireSpanning(self, value):
        self._nominalePrimaireSpanning.set_waarde(value, owner=self)

    @property
    def nominaleSecundaireSpanning(self) -> KwantWrdInVoltWaarden:
        """Nominale spanning van de secundaire wikkeling in V."""
        return self._nominaleSecundaireSpanning.get_waarde()

    @nominaleSecundaireSpanning.setter
    def nominaleSecundaireSpanning(self, value):
        self._nominaleSecundaireSpanning.set_waarde(value, owner=self)

    @property
    def schakelgroep(self) -> str:
        """Verzameling van 3 schakelcombinaties waarbij de hoofdletter de schakelwijze van de primaire weergeeft, de kleine letter(s) de schakelwijze van de secundaire weergeeft (en eventueel het feit dat het sterpunt naar buiten werd gebracht) en het getal geeft het klokgetal (of het aantal keer dat er 30° faseverschuiving tussen HS- en LS-spanning is) vb Dyn11"""
        return self._schakelgroep.get_waarde()

    @schakelgroep.setter
    def schakelgroep(self, value):
        self._schakelgroep.set_waarde(value, owner=self)

    @property
    def typeBeveiliging(self) -> str:
        """Type transformatorbeveiliging."""
        return self._typeBeveiliging.get_waarde()

    @typeBeveiliging.setter
    def typeBeveiliging(self, value):
        self._typeBeveiliging.set_waarde(value, owner=self)

    @property
    def typeVerliezen(self) -> str:
        """Type verliezen."""
        return self._typeVerliezen.get_waarde()

    @typeVerliezen.setter
    def typeVerliezen(self, value):
        self._typeVerliezen.set_waarde(value, owner=self)
