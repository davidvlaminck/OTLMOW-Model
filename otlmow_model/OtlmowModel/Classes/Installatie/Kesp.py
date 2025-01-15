# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.BalkGK import BalkGK
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kesp(BalkGK):
    """Algemene benaming voor het aanduiden van een betonnen balk bovenaan grondkerende structuren, een kopbalk als het ware (wordt ook wel kaaimuurkop genoemd). Ankervoorzieningen, ladders, enz. worden in/tegen de kesp bevestigd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kesp'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Ventilatie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Leuning', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Randprofiel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wrijfbalk', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bolder', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dekzerkprofiel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fendering', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Haalkom', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ladder', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkenmerk', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voegband', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenConstructieObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StalenConstructieObject', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ComplexeGeleiding', direction='i')  # i = direction: incoming

        self._heeftKraanrail = OTLAttribuut(field=BooleanField,
                                            naam='heeftKraanrail',
                                            label='heeft kraanrail',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kesp.heeftKraanrail',
                                            definition='Geeft aan of er kraainrail aanwezig is.',
                                            owner=self)

        self._heeftRuimschouw = OTLAttribuut(field=BooleanField,
                                             naam='heeftRuimschouw',
                                             label='heeft ruimschouw',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kesp.heeftRuimschouw',
                                             definition='Geeft aan of er ruimschouw aanwezig is.',
                                             owner=self)

        self._heeftTrekput = OTLAttribuut(field=BooleanField,
                                          naam='heeftTrekput',
                                          label='heeft trekput',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kesp.heeftTrekput',
                                          definition='Geeft aan of er trekput aanwezig is.',
                                          owner=self)

    @property
    def heeftKraanrail(self) -> bool:
        """Geeft aan of er kraainrail aanwezig is."""
        return self._heeftKraanrail.get_waarde()

    @heeftKraanrail.setter
    def heeftKraanrail(self, value):
        self._heeftKraanrail.set_waarde(value, owner=self)

    @property
    def heeftRuimschouw(self) -> bool:
        """Geeft aan of er ruimschouw aanwezig is."""
        return self._heeftRuimschouw.get_waarde()

    @heeftRuimschouw.setter
    def heeftRuimschouw(self, value):
        self._heeftRuimschouw.set_waarde(value, owner=self)

    @property
    def heeftTrekput(self) -> bool:
        """Geeft aan of er trekput aanwezig is."""
        return self._heeftTrekput.get_waarde()

    @heeftTrekput.setter
    def heeftTrekput(self, value):
        self._heeftTrekput.set_waarde(value, owner=self)
