# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.OntwerpwaterstandStreefpeil import OntwerpwaterstandStreefpeil
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDVWtoelaatbareSchipsafemetingen import DtcDVWtoelaatbareSchipsafemetingen, DtcDVWtoelaatbareSchipsafemetingenWaarden
from ...Datatypes.DtcOntwerpSchip import DtcOntwerpSchip, DtcOntwerpSchipWaarden
from ...Datatypes.KlKerendeKarakterSluis import KlKerendeKarakterSluis
from ...Datatypes.KlSluisCategorie import KlSluisCategorie
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...Datatypes.KwantWrdInTon import KwantWrdInTon, KwantWrdInTonWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sluis(OntwerpwaterstandStreefpeil, AIMNaamObject):
    """Waterbouwkundige constructie tussen twee waterlichamen met een verschillend waterpeil. Sluizen hebben als doel het beheersen van het waterpeil en het gecontroleerde doorlaten van schepen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Fuik', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie', direction='i')  # i = direction: incoming

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis.breedte',
                                     kardinaliteit_max='*',
                                     definition='De afstand tussen de dagkanten van de vaste constructie, uitgedrukt in meter.',
                                     owner=self)

        self._heeftStopstreep = OTLAttribuut(field=BooleanField,
                                             naam='heeftStopstreep',
                                             label='heeft stopstreep',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis.heeftStopstreep',
                                             definition='Geeft aan of er een stopstreep aanwezig is',
                                             owner=self)

        self._isMiddenhoofdAanwezig = OTLAttribuut(field=BooleanField,
                                                   naam='isMiddenhoofdAanwezig',
                                                   label='is middenhoofd aanwezig',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis.isMiddenhoofdAanwezig',
                                                   definition='Geeft aan of er een middenhoofd aanwezig is.',
                                                   owner=self)

        self._isOnderhevigAanGetijden = OTLAttribuut(field=BooleanField,
                                                     naam='isOnderhevigAanGetijden',
                                                     label='is onderhevig aan getijden',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis.isOnderhevigAanGetijden',
                                                     definition='Geeft aan of de sluis onderhevig aan getijden is.',
                                                     owner=self)

        self._kerendeKarakter = OTLAttribuut(field=KlKerendeKarakterSluis,
                                             naam='kerendeKarakter',
                                             label='kerende karakter',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis.kerendeKarakter',
                                             definition='De verschillende kerende karakters van een sluis.',
                                             owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis.lengte',
                                    kardinaliteit_max='*',
                                    definition='Lengte langs de kolkwand tussen de meest afwaartse deurkas/-kamer en de meest opwaartse deurkas/-kamer of het opwaarts hoog gefundeerd sluishoofd.',
                                    owner=self)

        self._ontwerpSchip = OTLAttribuut(field=DtcOntwerpSchip,
                                          naam='ontwerpSchip',
                                          label='ontwerp schip',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis.ontwerpSchip',
                                          kardinaliteit_max='*',
                                          definition='Schip met afmetingen dat wordt gekozen voor het ontwerp en de berekeningen van de sluis, dat representatief is voor het gemiddelde of typische scheepsverkeer dat naar verwachting de sluis zal gebruiken.',
                                          owner=self)

        self._sluiscategorie = OTLAttribuut(field=KlSluisCategorie,
                                            naam='sluiscategorie',
                                            label='sluiscategorie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis.sluiscategorie',
                                            definition='De verschillende categorieën van sluizen.',
                                            owner=self)

        self._toelaatbareSchipsafmetingen = OTLAttribuut(field=DtcDVWtoelaatbareSchipsafemetingen,
                                                         naam='toelaatbareSchipsafmetingen',
                                                         label='toelaatbare schipsafmetingen',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis.toelaatbareSchipsafmetingen',
                                                         definition='Het grootste schip dat door de sluis kan passeren',
                                                         owner=self)

        self._tonnenmaat = OTLAttribuut(field=KwantWrdInTon,
                                        naam='tonnenmaat',
                                        label='tonnenmaat',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis.tonnenmaat',
                                        definition='De maximale grootte van schepen, uitgedrukt in tonnen, die de sluis kunnen passeren zonder de capaciteit of de structuur van de sluis te overschrijden.',
                                        owner=self)

        self._vrijeHoogte = OTLAttribuut(field=KwantWrdInMeter,
                                         naam='vrijeHoogte',
                                         label='vrije hoogte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis.vrijeHoogte',
                                         definition='De verticale vrije ruimte tussen het wateroppervlak en het laagste punt van de bovenliggende constructie, zoals bruggen, balken of andere obstakels.',
                                         owner=self)

        self._waterdiepte = OTLAttribuut(field=KwantWrdInMeter,
                                         naam='waterdiepte',
                                         label='waterdiepte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis.waterdiepte',
                                         definition='De verticale afstand tussen het wateroppervlak, gemiddelde laagwaterstand (normale afwaarts pomppeil/ ALAT-waarde) , in de sluis van het laagste punt van de drempel, de sluishoofdvloer of sluiskolkvloer.',
                                         owner=self)

    @property
    def breedte(self) -> List[KwantWrdInMeterWaarden]:
        """De afstand tussen de dagkanten van de vaste constructie, uitgedrukt in meter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def heeftStopstreep(self) -> bool:
        """Geeft aan of er een stopstreep aanwezig is"""
        return self._heeftStopstreep.get_waarde()

    @heeftStopstreep.setter
    def heeftStopstreep(self, value):
        self._heeftStopstreep.set_waarde(value, owner=self)

    @property
    def isMiddenhoofdAanwezig(self) -> bool:
        """Geeft aan of er een middenhoofd aanwezig is."""
        return self._isMiddenhoofdAanwezig.get_waarde()

    @isMiddenhoofdAanwezig.setter
    def isMiddenhoofdAanwezig(self, value):
        self._isMiddenhoofdAanwezig.set_waarde(value, owner=self)

    @property
    def isOnderhevigAanGetijden(self) -> bool:
        """Geeft aan of de sluis onderhevig aan getijden is."""
        return self._isOnderhevigAanGetijden.get_waarde()

    @isOnderhevigAanGetijden.setter
    def isOnderhevigAanGetijden(self, value):
        self._isOnderhevigAanGetijden.set_waarde(value, owner=self)

    @property
    def kerendeKarakter(self) -> str:
        """De verschillende kerende karakters van een sluis."""
        return self._kerendeKarakter.get_waarde()

    @kerendeKarakter.setter
    def kerendeKarakter(self, value):
        self._kerendeKarakter.set_waarde(value, owner=self)

    @property
    def lengte(self) -> List[KwantWrdInMeterWaarden]:
        """Lengte langs de kolkwand tussen de meest afwaartse deurkas/-kamer en de meest opwaartse deurkas/-kamer of het opwaarts hoog gefundeerd sluishoofd."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def ontwerpSchip(self) -> List[DtcOntwerpSchipWaarden]:
        """Schip met afmetingen dat wordt gekozen voor het ontwerp en de berekeningen van de sluis, dat representatief is voor het gemiddelde of typische scheepsverkeer dat naar verwachting de sluis zal gebruiken."""
        return self._ontwerpSchip.get_waarde()

    @ontwerpSchip.setter
    def ontwerpSchip(self, value):
        self._ontwerpSchip.set_waarde(value, owner=self)

    @property
    def sluiscategorie(self) -> str:
        """De verschillende categorieën van sluizen."""
        return self._sluiscategorie.get_waarde()

    @sluiscategorie.setter
    def sluiscategorie(self, value):
        self._sluiscategorie.set_waarde(value, owner=self)

    @property
    def toelaatbareSchipsafmetingen(self) -> DtcDVWtoelaatbareSchipsafemetingenWaarden:
        """Het grootste schip dat door de sluis kan passeren"""
        return self._toelaatbareSchipsafmetingen.get_waarde()

    @toelaatbareSchipsafmetingen.setter
    def toelaatbareSchipsafmetingen(self, value):
        self._toelaatbareSchipsafmetingen.set_waarde(value, owner=self)

    @property
    def tonnenmaat(self) -> KwantWrdInTonWaarden:
        """De maximale grootte van schepen, uitgedrukt in tonnen, die de sluis kunnen passeren zonder de capaciteit of de structuur van de sluis te overschrijden."""
        return self._tonnenmaat.get_waarde()

    @tonnenmaat.setter
    def tonnenmaat(self, value):
        self._tonnenmaat.set_waarde(value, owner=self)

    @property
    def vrijeHoogte(self) -> KwantWrdInMeterWaarden:
        """De verticale vrije ruimte tussen het wateroppervlak en het laagste punt van de bovenliggende constructie, zoals bruggen, balken of andere obstakels."""
        return self._vrijeHoogte.get_waarde()

    @vrijeHoogte.setter
    def vrijeHoogte(self, value):
        self._vrijeHoogte.set_waarde(value, owner=self)

    @property
    def waterdiepte(self) -> KwantWrdInMeterWaarden:
        """De verticale afstand tussen het wateroppervlak, gemiddelde laagwaterstand (normale afwaarts pomppeil/ ALAT-waarde) , in de sluis van het laagste punt van de drempel, de sluishoofdvloer of sluiskolkvloer."""
        return self._waterdiepte.get_waarde()

    @waterdiepte.setter
    def waterdiepte(self, value):
        self._waterdiepte.set_waarde(value, owner=self)
