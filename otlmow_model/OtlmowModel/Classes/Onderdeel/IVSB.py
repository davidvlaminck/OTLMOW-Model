# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Classes.Onderdeel.RetroreflecterendVerkeersbord import RetroreflecterendVerkeersbord
from ...Datatypes.KlAantalLampenIVSB import KlAantalLampenIVSB
from ...Datatypes.KlLampTypeIVSB import KlLampTypeIVSB
from ...Datatypes.KlTypeIVSB import KlTypeIVSB
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class IVSB(NaampadObject, RetroreflecterendVerkeersbord):
    """Een verkeersbord dat door middel van interne verlichtingselementen,zoals LED's,TL-buizen of andere lichtbronnen,van binnenuit wordt verlicht om de leesbaarheid en zichtbaarheid van de verkeersinformatie onder alle lichtomstandigheden te verbeteren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IVSB'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#IVSBGroep', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming

        self._aantalLampen = OTLAttribuut(field=KlAantalLampenIVSB,
                                          naam='aantalLampen',
                                          label='aantal lampen',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IVSB.aantalLampen',
                                          definition='Het aantal lampen die aanwezig zijn op het bord.',
                                          owner=self)

        self._lampType = OTLAttribuut(field=KlLampTypeIVSB,
                                      naam='lampType',
                                      label='lamp type',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IVSB.lampType',
                                      definition='Het type van de lamp(en) aanwezig in het inwendig verlicht signalisatiebord.',
                                      owner=self)

        self._opschrift = OTLAttribuut(field=StringField,
                                       naam='opschrift',
                                       label='opschrift',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IVSB.opschrift',
                                       definition='Tekst en symbolen die op het bord getoond worden.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlTypeIVSB,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IVSB.type',
                                  definition='Het type inwendig verlicht signalisatiebord.',
                                  owner=self)

    @property
    def aantalLampen(self) -> str:
        """Het aantal lampen die aanwezig zijn op het bord."""
        return self._aantalLampen.get_waarde()

    @aantalLampen.setter
    def aantalLampen(self, value):
        self._aantalLampen.set_waarde(value, owner=self)

    @property
    def lampType(self) -> str:
        """Het type van de lamp(en) aanwezig in het inwendig verlicht signalisatiebord."""
        return self._lampType.get_waarde()

    @lampType.setter
    def lampType(self, value):
        self._lampType.set_waarde(value, owner=self)

    @property
    def opschrift(self) -> str:
        """Tekst en symbolen die op het bord getoond worden."""
        return self._opschrift.get_waarde()

    @opschrift.setter
    def opschrift(self, value):
        self._opschrift.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type inwendig verlicht signalisatiebord."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
