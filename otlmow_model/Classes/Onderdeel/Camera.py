# coding=utf-8
from typing import List
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.DtcCameraBeeldverwerking import DtcCameraBeeldverwerking, DtcCameraBeeldverwerkingWaarden
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.DteIPv4Adres import DteIPv4Adres, DteIPv4AdresWaarden
from otlmow_model.Datatypes.KlCameraMerk import KlCameraMerk
from otlmow_model.Datatypes.KlCameraModelnaam import KlCameraModelnaam
from otlmow_model.Datatypes.KlSensorOpstelwijze import KlSensorOpstelwijze
from otlmow_model.Datatypes.KlServicePrioriteit import KlServicePrioriteit
from otlmow_model.Datatypes.KlSpectrum import KlSpectrum
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Camera(SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een CCTV-camera, closed-circuit television camera, kortweg camera, produceert beelden of opnames voor bewaking van een regio vanop afstand. Het is een element dat beelden neemt van een locatie en deze doorgeeft naar verschillende partijen om zo de werkelijke situatie te kunnen inschatten vanop afstand. Deze camera kan van het analoge type zijn of digitaal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestigingsbeugel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FieldOfView', deprecated='2.4.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Meetstation')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wilddetectiezone')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zoutbijlaadplaats')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AIDModule')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer')

        self._beeldverwerkingsinstelling = OTLAttribuut(field=DtcCameraBeeldverwerking,
                                                        naam='beeldverwerkingsinstelling',
                                                        label='beeldverwerkingsinstelling',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.beeldverwerkingsinstelling',
                                                        usagenote='Wanneer de camera de beeldverwerking niet zelf doet maar enkel beelden  verstuurt voor verwerking in een externe eenheid, moet die externe eenheid als aparte asset aangemaakt worden indien het specifieke type bestaat in de OTL of moet een instantie van Software gebruikt worden wanneer geen specifieke externe verwerkingseenheid voorzien is. Dit attribuut kan dus enkel gebruikt worden indien de camera of een verwerkingseenheid van de camera zelf de analyse doet en die analyse doorstuurt naar een asset die met de analyse werkt en niet met de beelden.',
                                                        kardinaliteit_max='*',
                                                        definition='Geeft aan welke types beeldverwerking die camera zelf uitvoert dus zonder gebruik te maken van een externe verwerkingseenheid.',
                                                        owner=self)

        self._configBestandAid = OTLAttribuut(field=DtcDocument,
                                              naam='configBestandAid',
                                              label='configuratie bestand AID',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.configBestandAid',
                                              usagenote='Attribuut uit gebruik sinds versie 2.3.0 ',
                                              deprecated_version='2.3.0',
                                              definition='Het bestand met de configuratie van de AID component die deel is van de camera.',
                                              owner=self)

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.',
                                     owner=self)

        self._heeftAid = OTLAttribuut(field=BooleanField,
                                      naam='heeftAid',
                                      label='heeft AID',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.heeftAid',
                                      usagenote='Attribuut uit gebruik sinds versie 2.3.0 ',
                                      deprecated_version='2.3.0',
                                      definition='Een AID-camera is een CCTV-camera met geintegreerde AID-module. Deze camera genereert naast een camerabeeld ook metadata ivm wat zich afspeelt op het beeld. Een voorbeeld hiervan is gestopte voertuigen.',
                                      owner=self)

        self._heeftSpitsstrook = OTLAttribuut(field=BooleanField,
                                              naam='heeftSpitsstrook',
                                              label='heeft spitsstrook',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.heeftSpitsstrook',
                                              usagenote='Attribuut uit gebruik sinds versie 2.3.0 ',
                                              deprecated_version='2.3.0',
                                              definition='Locatie-eigenschap van een camera. Dit attribuut geeft aan of de camera ingezet wordt om een spitsstrook te schouwen.',
                                              owner=self)

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ip adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.ipAdres',
                                     definition='Het IP-adres van de camera.',
                                     owner=self)

        self._isPtz = OTLAttribuut(field=BooleanField,
                                   naam='isPtz',
                                   label='is PTZ',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.isPtz',
                                   definition='Een PTZ-camera is een CCTV-camera met bijhorend de mogelijkheid om te pannen, tilten en zoomen. Dit vanop afstand met behulp van een verstelbare lens en een motor die in twee assen draaibeweging toelaat.',
                                   owner=self)

        self._merk = OTLAttribuut(field=KlCameraMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.merk',
                                  definition='Het merk van de camera.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlCameraModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.modelnaam',
                                       definition='De modelnaam van de camera.',
                                       owner=self)

        self._opstelhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='opstelhoogte',
                                          label='opstelhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.opstelhoogte',
                                          usagenote='De plaats waar de draagconstructie in de grond bevestigd is, bepaalt van waar gemeten wordt voor het bepalen van de opstelhoogte. Wanneer een camera die een brugdek overziet, bevestigd is aan een paal die naast de brug staat, wordt de hoogte gemeten vanaf de basis van de paal en niet vanaf het brugdek. ',
                                          definition='De hoogte waarop de camera bevestigd is, gemeten ten opzichte van het maaiveld waarin de draagconstructie voor de camera verankerd is.',
                                          owner=self)

        self._opstelwijze = OTLAttribuut(field=KlSensorOpstelwijze,
                                         naam='opstelwijze',
                                         label='opstelwijze',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.opstelwijze',
                                         definition='De manier waarop de camera is opgesteld, bv. via dwarsligger,...',
                                         owner=self)

        self._servicePrioriteit = OTLAttribuut(field=KlServicePrioriteit,
                                               naam='servicePrioriteit',
                                               label='service prioriteit',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.servicePrioriteit',
                                               definition='Het prioriteitsniveau dat aangeeft hoe dringend iets moet onderhouden/gerepareerd worden.',
                                               owner=self)

        self._spectrum = OTLAttribuut(field=KlSpectrum,
                                      naam='spectrum',
                                      label='spectrum',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.spectrum',
                                      definition='De golflengte van de invallende straling.',
                                      owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera.technischeFiche',
                                             usagenote='Bestanden van het type pdf.',
                                             kardinaliteit_max='*',
                                             definition="Technische fiche van dit element met opsplitsing tussen CCTV, AID en PTZ-camera's.",
                                             owner=self)

    @property
    def beeldverwerkingsinstelling(self) -> List[DtcCameraBeeldverwerkingWaarden]:
        """Geeft aan welke types beeldverwerking die camera zelf uitvoert dus zonder gebruik te maken van een externe verwerkingseenheid."""
        return self._beeldverwerkingsinstelling.get_waarde()

    @beeldverwerkingsinstelling.setter
    def beeldverwerkingsinstelling(self, value):
        self._beeldverwerkingsinstelling.set_waarde(value, owner=self)

    @property
    def configBestandAid(self) -> DtcDocumentWaarden:
        """Het bestand met de configuratie van de AID component die deel is van de camera."""
        return self._configBestandAid.get_waarde()

    @configBestandAid.setter
    def configBestandAid(self, value):
        self._configBestandAid.set_waarde(value, owner=self)

    @property
    def dnsNaam(self) -> str:
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.get_waarde()

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def heeftAid(self) -> bool:
        """Een AID-camera is een CCTV-camera met geintegreerde AID-module. Deze camera genereert naast een camerabeeld ook metadata ivm wat zich afspeelt op het beeld. Een voorbeeld hiervan is gestopte voertuigen."""
        return self._heeftAid.get_waarde()

    @heeftAid.setter
    def heeftAid(self, value):
        self._heeftAid.set_waarde(value, owner=self)

    @property
    def heeftSpitsstrook(self) -> bool:
        """Locatie-eigenschap van een camera. Dit attribuut geeft aan of de camera ingezet wordt om een spitsstrook te schouwen."""
        return self._heeftSpitsstrook.get_waarde()

    @heeftSpitsstrook.setter
    def heeftSpitsstrook(self, value):
        self._heeftSpitsstrook.set_waarde(value, owner=self)

    @property
    def ipAdres(self) -> DteIPv4AdresWaarden:
        """Het IP-adres van de camera."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def isPtz(self) -> bool:
        """Een PTZ-camera is een CCTV-camera met bijhorend de mogelijkheid om te pannen, tilten en zoomen. Dit vanop afstand met behulp van een verstelbare lens en een motor die in twee assen draaibeweging toelaat."""
        return self._isPtz.get_waarde()

    @isPtz.setter
    def isPtz(self, value):
        self._isPtz.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de camera."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de camera."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def opstelhoogte(self) -> KwantWrdInMeterWaarden:
        """De hoogte waarop de camera bevestigd is, gemeten ten opzichte van het maaiveld waarin de draagconstructie voor de camera verankerd is."""
        return self._opstelhoogte.get_waarde()

    @opstelhoogte.setter
    def opstelhoogte(self, value):
        self._opstelhoogte.set_waarde(value, owner=self)

    @property
    def opstelwijze(self) -> str:
        """De manier waarop de camera is opgesteld, bv. via dwarsligger,..."""
        return self._opstelwijze.get_waarde()

    @opstelwijze.setter
    def opstelwijze(self, value):
        self._opstelwijze.set_waarde(value, owner=self)

    @property
    def servicePrioriteit(self) -> str:
        """Het prioriteitsniveau dat aangeeft hoe dringend iets moet onderhouden/gerepareerd worden."""
        return self._servicePrioriteit.get_waarde()

    @servicePrioriteit.setter
    def servicePrioriteit(self, value):
        self._servicePrioriteit.set_waarde(value, owner=self)

    @property
    def spectrum(self) -> str:
        """De golflengte van de invallende straling."""
        return self._spectrum.get_waarde()

    @spectrum.setter
    def spectrum(self, value):
        self._spectrum.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> List[DtcDocumentWaarden]:
        """Technische fiche van dit element met opsplitsing tussen CCTV, AID en PTZ-camera's."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
