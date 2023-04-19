# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Communicatieapparatuur import Communicatieapparatuur
from otlmow_model.Datatypes.KlAntenneConstructieType import KlAntenneConstructieType
from otlmow_model.Datatypes.KlAntenneFrequentierange import KlAntenneFrequentierange
from otlmow_model.Datatypes.KlAntenneMerk import KlAntenneMerk
from otlmow_model.Datatypes.KlAntenneModelnaam import KlAntenneModelnaam
from otlmow_model.Datatypes.KlAntenneUitvoeringsType import KlAntenneUitvoeringsType
from otlmow_model.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden, KwantWrdInDecimaleGradenWaarden
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Antenne(Communicatieapparatuur):
    """Toestel verbonden met een zender of ontvanger ten behoeve van het opvangen of verspreiden van signalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitspaal')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zendmast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#RHZModule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antennecoupler')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalSplitter')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar')

        self._constructieType = OTLAttribuut(field=KlAntenneConstructieType,
                                             naam='constructieType',
                                             label='constructie type',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.constructieType',
                                             definition='Het constructie type of de vorm van de antenne, die mee de wijze van ophanging bepaald.',
                                             owner=self)

        self._frequentierange = OTLAttribuut(field=KlAntenneFrequentierange,
                                             naam='frequentierange',
                                             label='frequentierange',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.frequentierange',
                                             definition='Geeft de frequentierange aan waarbinnen de antenne gebruikt kan worden.',
                                             owner=self)

        self._merk = OTLAttribuut(field=KlAntenneMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.merk',
                                  definition='Het merk van de antenne.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlAntenneModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.modelnaam',
                                       definition='De modelnaam/product range van een antenne.',
                                       owner=self)

        self._opstelhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='opstelhoogte',
                                          label='opstelhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.opstelhoogte',
                                          definition='De opstelhoogte van de antenne t.o.v. het maaiveld.',
                                          owner=self)

        self._stralingshoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                           naam='stralingshoek',
                                           label='stralingshoek',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.stralingshoek',
                                           definition='Geeft aan over welke hoek de antenne signalen kan uitstralen en ontvangen.',
                                           owner=self)

        self._uitvoeringsType = OTLAttribuut(field=KlAntenneUitvoeringsType,
                                             naam='uitvoeringsType',
                                             label='uitvoeringstype',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne.uitvoeringsType',
                                             definition='Het uitvoeringstype betreft de werkwijze van de antenne, die bepaalt onder welke richting(en) de antenne signaal uitstuurt en ontvangt.',
                                             owner=self)

    @property
    def constructieType(self) -> str:
        """Het constructie type of de vorm van de antenne, die mee de wijze van ophanging bepaald."""
        return self._constructieType.get_waarde()

    @constructieType.setter
    def constructieType(self, value):
        self._constructieType.set_waarde(value, owner=self)

    @property
    def frequentierange(self) -> str:
        """Geeft de frequentierange aan waarbinnen de antenne gebruikt kan worden."""
        return self._frequentierange.get_waarde()

    @frequentierange.setter
    def frequentierange(self, value):
        self._frequentierange.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de antenne."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam/product range van een antenne."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def opstelhoogte(self) -> KwantWrdInMeterWaarden:
        """De opstelhoogte van de antenne t.o.v. het maaiveld."""
        return self._opstelhoogte.get_waarde()

    @opstelhoogte.setter
    def opstelhoogte(self, value):
        self._opstelhoogte.set_waarde(value, owner=self)

    @property
    def stralingshoek(self) -> KwantWrdInDecimaleGradenWaarden:
        """Geeft aan over welke hoek de antenne signalen kan uitstralen en ontvangen."""
        return self._stralingshoek.get_waarde()

    @stralingshoek.setter
    def stralingshoek(self, value):
        self._stralingshoek.set_waarde(value, owner=self)

    @property
    def uitvoeringsType(self) -> str:
        """Het uitvoeringstype betreft de werkwijze van de antenne, die bepaalt onder welke richting(en) de antenne signaal uitstuurt en ontvangt."""
        return self._uitvoeringsType.get_waarde()

    @uitvoeringsType.setter
    def uitvoeringsType(self, value):
        self._uitvoeringsType.set_waarde(value, owner=self)
