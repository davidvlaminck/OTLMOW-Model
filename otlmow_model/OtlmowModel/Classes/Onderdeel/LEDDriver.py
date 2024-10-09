# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlLEDDriverMerk import KlLEDDriverMerk
from ...Datatypes.KlLEDDriverModelnaam import KlLEDDriverModelnaam
from ...Datatypes.KlLEDDriverProtocol import KlLEDDriverProtocol
from ...Datatypes.KwantWrdInMilliAmpere import KwantWrdInMilliAmpere, KwantWrdInMilliAmpereWaarden
from ...Datatypes.KwantWrdInWatt import KwantWrdInWatt, KwantWrdInWattWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class LEDDriver(SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een LED-driver is een elektronisch toestel dat de stroomtoevoer naar de LED's dimensioneert om de goede werking te verzekeren. Via de instelparameters van de driver kan uiteindelijk de lichtsterkte van de LED verlichting aangepast worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller', direction='u', deprecated='2.4.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVOpvoertransformator', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVOpvoertransformator', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVOpvoertransformator', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller', direction='i')  # i = direction: incoming

        self._maximaalVermogen = OTLAttribuut(field=KwantWrdInWatt,
                                              naam='maximaalVermogen',
                                              label='maximaal vermogen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.maximaalVermogen',
                                              definition='Maximaal afgenomen vermogen van de driver en lamp/lichtbron samen (incl. verlies/verbruik van de driver zelf).',
                                              owner=self)

        self._maximaleAanstuurstroom = OTLAttribuut(field=KwantWrdInMilliAmpere,
                                                    naam='maximaleAanstuurstroom',
                                                    label='maximale aanstuurstroom',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.maximaleAanstuurstroom',
                                                    definition='Maximale aanstuurstroom die de LED-driver kan leveren.',
                                                    owner=self)

        self._merk = OTLAttribuut(field=KlLEDDriverMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.merk',
                                  definition='Het merk van de LED-driver.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlLEDDriverModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.modelnaam',
                                       definition='De modelnaam van de LED-driver.',
                                       owner=self)

        self._protocol = OTLAttribuut(field=KlLEDDriverProtocol,
                                      naam='protocol',
                                      label='protocol',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.protocol',
                                      definition="Protocol gebruikt door de LED-driver voor het aansturen van de LED's.",
                                      owner=self)

    @property
    def maximaalVermogen(self) -> KwantWrdInWattWaarden:
        """Maximaal afgenomen vermogen van de driver en lamp/lichtbron samen (incl. verlies/verbruik van de driver zelf)."""
        return self._maximaalVermogen.get_waarde()

    @maximaalVermogen.setter
    def maximaalVermogen(self, value):
        self._maximaalVermogen.set_waarde(value, owner=self)

    @property
    def maximaleAanstuurstroom(self) -> KwantWrdInMilliAmpereWaarden:
        """Maximale aanstuurstroom die de LED-driver kan leveren."""
        return self._maximaleAanstuurstroom.get_waarde()

    @maximaleAanstuurstroom.setter
    def maximaleAanstuurstroom(self, value):
        self._maximaleAanstuurstroom.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de LED-driver."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de LED-driver."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def protocol(self) -> str:
        """Protocol gebruikt door de LED-driver voor het aansturen van de LED's."""
        return self._protocol.get_waarde()

    @protocol.setter
    def protocol(self, value):
        self._protocol.set_waarde(value, owner=self)
