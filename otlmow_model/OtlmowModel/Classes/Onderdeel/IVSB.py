# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Onderdeel.RetroreflecterendVerkeersbord import RetroreflecterendVerkeersbord
from ...Datatypes.KlTypeIVSB import KlTypeIVSB


# Generated with OTLClassCreator. To modify: extend, do not edit
class IVSB(RetroreflecterendVerkeersbord):
    """Een verkeersbord dat door middel van interne verlichtingselementen, zoals LED's, TL-buizen of andere lichtbronnen, van binnenuit wordt verlicht om de leesbaarheid en zichtbaarheid van de verkeersinformatie onder alle lichtomstandigheden te verbeteren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IVSB'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming

        self._type = OTLAttribuut(field=KlTypeIVSB,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IVSB.type',
                                  definition='Het type inwendig verlicht signalisatiebord.',
                                  owner=self)

    @property
    def type(self) -> str:
        """Het type inwendig verlicht signalisatiebord."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
