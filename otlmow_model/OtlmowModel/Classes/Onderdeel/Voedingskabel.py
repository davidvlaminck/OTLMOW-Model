# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Kabel import Kabel
from ...Datatypes.KlNominaleSpanning import KlNominaleSpanning
from ...Datatypes.KlVoedingskabelAdersEnSectie import KlVoedingskabelAdersEnSectie
from ...Datatypes.KlVoedingskabelType import KlVoedingskabelType
from ...Datatypes.KlVoedingskabelTypeSpecificatie import KlVoedingskabelTypeSpecificatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voedingskabel(Kabel):
    """Zorgt voor het overbrengen van een elektrisch vermogen van de ene locatie naar de andere binnen een privaat netwerk. Onder dit type vallen ook installatiedraden die beschouwd worden als kabels met slechts één ader."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BinnenverlichtingGroep', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Z30Groep', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting', direction='i')  # i = direction: incoming

        self._aantalAdersEnSectie = OTLAttribuut(field=KlVoedingskabelAdersEnSectie,
                                                 naam='aantalAdersEnSectie',
                                                 label='aantal aders en sectie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel.aantalAdersEnSectie',
                                                 definition='Aantal en sectie van de ader(s) van de kabel volgens een lijst van voorkomende types.',
                                                 owner=self)

        self._nominaleSpanning = OTLAttribuut(field=KlNominaleSpanning,
                                              naam='nominaleSpanning',
                                              label='nominale spanning',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel.nominaleSpanning',
                                              definition='De nominale spanning van de voedingskabel.',
                                              owner=self)

        self._type = OTLAttribuut(field=KlVoedingskabelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel.type',
                                  definition='Indeling van een energie- of installatiekabel of -draad op basis van de gebruikte materialen en volgens een vaste typering.',
                                  owner=self)

        self._typeSpecificatie = OTLAttribuut(field=KlVoedingskabelTypeSpecificatie,
                                              naam='typeSpecificatie',
                                              label='type specificatie',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel.typeSpecificatie',
                                              definition='Een verdere specificatie van het type van de voedingskabel volgens een vaste lijst om bv. de brandklasse mee te geven.',
                                              owner=self)

    @property
    def aantalAdersEnSectie(self) -> str:
        """Aantal en sectie van de ader(s) van de kabel volgens een lijst van voorkomende types."""
        return self._aantalAdersEnSectie.get_waarde()

    @aantalAdersEnSectie.setter
    def aantalAdersEnSectie(self, value):
        self._aantalAdersEnSectie.set_waarde(value, owner=self)

    @property
    def nominaleSpanning(self) -> str:
        """De nominale spanning van de voedingskabel."""
        return self._nominaleSpanning.get_waarde()

    @nominaleSpanning.setter
    def nominaleSpanning(self, value):
        self._nominaleSpanning.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Indeling van een energie- of installatiekabel of -draad op basis van de gebruikte materialen en volgens een vaste typering."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def typeSpecificatie(self) -> str:
        """Een verdere specificatie van het type van de voedingskabel volgens een vaste lijst om bv. de brandklasse mee te geven."""
        return self._typeSpecificatie.get_waarde()

    @typeSpecificatie.setter
    def typeSpecificatie(self, value):
        self._typeSpecificatie.set_waarde(value, owner=self)
