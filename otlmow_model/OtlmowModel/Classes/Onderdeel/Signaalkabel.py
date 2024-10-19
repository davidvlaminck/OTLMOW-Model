# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Kabel import Kabel
from ...Datatypes.KlSignaalkabelAdersEnSectie import KlSignaalkabelAdersEnSectie
from ...Datatypes.KlSignaalkabelType import KlSignaalkabelType
from ...Datatypes.KlSignaalkabelTypeSpecificatie import KlSignaalkabelTypeSpecificatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Signaalkabel(Kabel):
    """Kabel die primair zorgt voor het uitwisselen van digitale en analoge stuursignalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalkabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#OmhullendeInrichting', direction='i')  # i = direction: incoming

        self._aantalAdersEnSectie = OTLAttribuut(field=KlSignaalkabelAdersEnSectie,
                                                 naam='aantalAdersEnSectie',
                                                 label='aders specificatie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalkabel.aantalAdersEnSectie',
                                                 definition='Aantal en sectie van de ader(s) in de signalisatiekabel.',
                                                 owner=self)

        self._type = OTLAttribuut(field=KlSignaalkabelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalkabel.type',
                                  definition='Geeft aan wat voor stuurkabel gebruikt wordt.',
                                  owner=self)

        self._typeSpecificatie = OTLAttribuut(field=KlSignaalkabelTypeSpecificatie,
                                              naam='typeSpecificatie',
                                              label='type specificatie',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalkabel.typeSpecificatie',
                                              definition='Een verdere specificatie van het type van de signalisatiekabel volgens een vaste lijst om bv. de brandklasse mee te geven.',
                                              owner=self)

    @property
    def aantalAdersEnSectie(self) -> str:
        """Aantal en sectie van de ader(s) in de signalisatiekabel."""
        return self._aantalAdersEnSectie.get_waarde()

    @aantalAdersEnSectie.setter
    def aantalAdersEnSectie(self, value):
        self._aantalAdersEnSectie.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Geeft aan wat voor stuurkabel gebruikt wordt."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def typeSpecificatie(self) -> str:
        """Een verdere specificatie van het type van de signalisatiekabel volgens een vaste lijst om bv. de brandklasse mee te geven."""
        return self._typeSpecificatie.get_waarde()

    @typeSpecificatie.setter
    def typeSpecificatie(self, value):
        self._typeSpecificatie.set_waarde(value, owner=self)
