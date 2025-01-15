# coding=utf-8
from datetime import date
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcExterneReferentie import DtcExterneReferentie, DtcExterneReferentieWaarden
from ...Datatypes.DteIPv4Adres import DteIPv4Adres, DteIPv4AdresWaarden
from ...Datatypes.KlRegelaarRegelaartype import KlRegelaarRegelaartype
from ...Datatypes.KlVRDisplayType import KlVRDisplayType
from ...Datatypes.KlVerkeersregelaarCoordinatiewijze import KlVerkeersregelaarCoordinatiewijze
from ...Datatypes.KlVerkeersregelaarMerk import KlVerkeersregelaarMerk
from ...Datatypes.KlVerkeersregelaarModelnaam import KlVerkeersregelaarModelnaam
from ...Datatypes.KlVerkeersregelaarVoltage import KlVerkeersregelaarVoltage
from ...Datatypes.KlVrStuurkaartCommunicatieprotocol import KlVrStuurkaartCommunicatieprotocol
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersregelaar(AIMNaamObject, PuntGeometrie):
    """Een verkeersregelaar is een programmeerbaar toestel dat de verkeerslichten op kruispunten kan regelen overeenkomstig een goedgekeurd verkeersplan. Een verkeersregelaar is bedoeld om het verkeer verkeersafhankelijk te sturen overeenkomstig het gedetecteerde verkeer. Verkeersregelaars kunnen op zichzelf werken of in groep ingeschakeld worden, zodoende op een gecoördineerde wijze de verkeersstromen te verwerken. Eveneens detecteert een verkeersregelaar defecte onderdelen, van zichzelf of van aangesloten installaties. Afhankelijk van het soort defect stuurt een verkeersregelaar een code uit opdat het euvel hersteld kan worden. Bij welbepaalde defecten worden verkeerslichten uitgeschakeld of op knipperstand gezet. Volgende documenten zijn specifiek van toepassing voor verkeersregelaars: *Koninklijk Besluit van 01.12.1975 (wegcode), aangevuld met alle officiële documenten hierover gepubliceerd; *NBN EN 12675:2000 (Verkeersregelapparaten - Functionele veiligheidseisen); *NBN EN 50556:2011 (Signalisatie voor wegverkeer; *NBN EN 12368:2006 (Verkeersregelinstallaties - Verkeerslantaars); *NBN EN 50293:2012 (Verkeersregelinstallaties - Elektromagnetische compatibiliteit)"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VerkeersregelaarModule', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectie', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Seinlantaarn', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitspaal', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Antenne', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbord', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netstabilisator', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#UPS', direction='i')  # i = direction: incoming

        self._communicatieprotocol = OTLAttribuut(field=KlVrStuurkaartCommunicatieprotocol,
                                                  naam='communicatieprotocol',
                                                  label='communicatieprotocol',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.communicatieprotocol',
                                                  definition='Gebruikte communicatieprotocol voor de stuurkaart.',
                                                  owner=self)

        self._coordinatiewijze = OTLAttribuut(field=KlVerkeersregelaarCoordinatiewijze,
                                              naam='coordinatiewijze',
                                              label='coördinatiewijze',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.coordinatiewijze',
                                              kardinaliteit_max='*',
                                              definition='Wijze waarop de coördinatie is opgezet en de eventuele rol die de verkeersregelaar hierin speelt.',
                                              owner=self)

        self._dnsNaam = OTLAttribuut(field=StringField,
                                     naam='dnsNaam',
                                     label='DNS naam',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.dnsNaam',
                                     definition='De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.',
                                     owner=self)

        self._externeReferentie = OTLAttribuut(field=DtcExterneReferentie,
                                               naam='externeReferentie',
                                               label='externe referentie',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.externeReferentie',
                                               kardinaliteit_max='*',
                                               definition='Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ...',
                                               owner=self)

        self._heeftHandbediening = OTLAttribuut(field=BooleanField,
                                                naam='heeftHandbediening',
                                                label='heeft handbediening',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.heeftHandbediening',
                                                definition='Aanduiding of de verkeersregelaar uitgerust is met een manuele regeling.',
                                                owner=self)

        self._heeftSDKaart = OTLAttribuut(field=BooleanField,
                                          naam='heeftSDKaart',
                                          label='heeft SD-kaart',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.heeftSDKaart',
                                          definition='Aanduiding of er al dan niet een SD-kaart aanwezig is op de communicatiekaart van de verkeersregelaar.',
                                          owner=self)

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='ipv4 adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.ipAdres',
                                     definition='IP-adres.',
                                     owner=self)

        self._kabelaansluitschema = OTLAttribuut(field=DtcDocument,
                                                 naam='kabelaansluitschema',
                                                 label='kabelaansluitschema',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.kabelaansluitschema',
                                                 definition='Document met het kabelaansluitschema.',
                                                 owner=self)

        self._merk = OTLAttribuut(field=KlVerkeersregelaarMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.merk',
                                  definition='Het merk van een verkeersregelaar.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlVerkeersregelaarModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.modelnaam',
                                       definition='De modelnaam/product range van een verkeersregelaar.',
                                       owner=self)

        self._programmeertool = OTLAttribuut(field=StringField,
                                             naam='programmeertool',
                                             label='programmeertool',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.programmeertool',
                                             definition='Software waarmee de verkeersregelaar geprogrammeerd kan worden.',
                                             owner=self)

        self._regelaartype = OTLAttribuut(field=KlRegelaarRegelaartype,
                                          naam='regelaartype',
                                          label='regelaartype',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.regelaartype',
                                          definition='Onderverdeling in type regelaar volgens het maximale aantal aan te sluiten seingroepen en kruispuntdetectoren.',
                                          owner=self)

        self._simkaartnummer = OTLAttribuut(field=StringField,
                                            naam='simkaartnummer',
                                            label='simkaartnummer',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.simkaartnummer',
                                            definition='Het nummer van de simkaart die aanwezig is op de communicatiekaart.',
                                            owner=self)

        self._technischeDocumentatie = OTLAttribuut(field=DtcDocument,
                                                    naam='technischeDocumentatie',
                                                    label='technische documentatie',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.technischeDocumentatie',
                                                    definition='Document met technische informatie.',
                                                    owner=self)

        self._typeDisplay = OTLAttribuut(field=KlVRDisplayType,
                                         naam='typeDisplay',
                                         label='type display',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.typeDisplay',
                                         definition='Het type van display gebruikt op de verkeersregelaar.',
                                         owner=self)

        self._voltageLampen = OTLAttribuut(field=KlVerkeersregelaarVoltage,
                                           naam='voltageLampen',
                                           label='voltage lampen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.voltageLampen',
                                           definition='Voltage van de verkeerslichten.',
                                           owner=self)

        self._vplanDatum = OTLAttribuut(field=DateField,
                                        naam='vplanDatum',
                                        label='vplan datum',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.vplanDatum',
                                        definition='Datum van het V-plan.',
                                        owner=self)

        self._vplanNummer = OTLAttribuut(field=StringField,
                                         naam='vplanNummer',
                                         label='vplan nummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersregelaar.vplanNummer',
                                         definition='Nummer van het V-plan.',
                                         owner=self)

    @property
    def communicatieprotocol(self) -> str:
        """Gebruikte communicatieprotocol voor de stuurkaart."""
        return self._communicatieprotocol.get_waarde()

    @communicatieprotocol.setter
    def communicatieprotocol(self, value):
        self._communicatieprotocol.set_waarde(value, owner=self)

    @property
    def coordinatiewijze(self) -> List[str]:
        """Wijze waarop de coördinatie is opgezet en de eventuele rol die de verkeersregelaar hierin speelt."""
        return self._coordinatiewijze.get_waarde()

    @coordinatiewijze.setter
    def coordinatiewijze(self, value):
        self._coordinatiewijze.set_waarde(value, owner=self)

    @property
    def dnsNaam(self) -> str:
        """De DNSNaam (ook "volledige domein naam" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""
        return self._dnsNaam.get_waarde()

    @dnsNaam.setter
    def dnsNaam(self, value):
        self._dnsNaam.set_waarde(value, owner=self)

    @property
    def externeReferentie(self) -> List[DtcExterneReferentieWaarden]:
        """Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ..."""
        return self._externeReferentie.get_waarde()

    @externeReferentie.setter
    def externeReferentie(self, value):
        self._externeReferentie.set_waarde(value, owner=self)

    @property
    def heeftHandbediening(self) -> bool:
        """Aanduiding of de verkeersregelaar uitgerust is met een manuele regeling."""
        return self._heeftHandbediening.get_waarde()

    @heeftHandbediening.setter
    def heeftHandbediening(self, value):
        self._heeftHandbediening.set_waarde(value, owner=self)

    @property
    def heeftSDKaart(self) -> bool:
        """Aanduiding of er al dan niet een SD-kaart aanwezig is op de communicatiekaart van de verkeersregelaar."""
        return self._heeftSDKaart.get_waarde()

    @heeftSDKaart.setter
    def heeftSDKaart(self, value):
        self._heeftSDKaart.set_waarde(value, owner=self)

    @property
    def ipAdres(self) -> DteIPv4AdresWaarden:
        """IP-adres."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def kabelaansluitschema(self) -> DtcDocumentWaarden:
        """Document met het kabelaansluitschema."""
        return self._kabelaansluitschema.get_waarde()

    @kabelaansluitschema.setter
    def kabelaansluitschema(self, value):
        self._kabelaansluitschema.set_waarde(value, owner=self)

    @property
    def merk(self) -> str:
        """Het merk van een verkeersregelaar."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam/product range van een verkeersregelaar."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def programmeertool(self) -> str:
        """Software waarmee de verkeersregelaar geprogrammeerd kan worden."""
        return self._programmeertool.get_waarde()

    @programmeertool.setter
    def programmeertool(self, value):
        self._programmeertool.set_waarde(value, owner=self)

    @property
    def regelaartype(self) -> str:
        """Onderverdeling in type regelaar volgens het maximale aantal aan te sluiten seingroepen en kruispuntdetectoren."""
        return self._regelaartype.get_waarde()

    @regelaartype.setter
    def regelaartype(self, value):
        self._regelaartype.set_waarde(value, owner=self)

    @property
    def simkaartnummer(self) -> str:
        """Het nummer van de simkaart die aanwezig is op de communicatiekaart."""
        return self._simkaartnummer.get_waarde()

    @simkaartnummer.setter
    def simkaartnummer(self, value):
        self._simkaartnummer.set_waarde(value, owner=self)

    @property
    def technischeDocumentatie(self) -> DtcDocumentWaarden:
        """Document met technische informatie."""
        return self._technischeDocumentatie.get_waarde()

    @technischeDocumentatie.setter
    def technischeDocumentatie(self, value):
        self._technischeDocumentatie.set_waarde(value, owner=self)

    @property
    def typeDisplay(self) -> str:
        """Het type van display gebruikt op de verkeersregelaar."""
        return self._typeDisplay.get_waarde()

    @typeDisplay.setter
    def typeDisplay(self, value):
        self._typeDisplay.set_waarde(value, owner=self)

    @property
    def voltageLampen(self) -> str:
        """Voltage van de verkeerslichten."""
        return self._voltageLampen.get_waarde()

    @voltageLampen.setter
    def voltageLampen(self, value):
        self._voltageLampen.set_waarde(value, owner=self)

    @property
    def vplanDatum(self) -> date:
        """Datum van het V-plan."""
        return self._vplanDatum.get_waarde()

    @vplanDatum.setter
    def vplanDatum(self, value):
        self._vplanDatum.set_waarde(value, owner=self)

    @property
    def vplanNummer(self) -> str:
        """Nummer van het V-plan."""
        return self._vplanNummer.get_waarde()

    @vplanNummer.setter
    def vplanNummer(self, value):
        self._vplanNummer.set_waarde(value, owner=self)
