# coding=utf-8
from datetime import date
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from otlmow_model.OtlmowModel.BaseClasses.DateField import DateField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlAansluitingMIVMeetpunt import KlAansluitingMIVMeetpunt
from ...Datatypes.KlAlgRijstrookcode import KlAlgRijstrookcode
from ...Datatypes.KlMIVLusUitslijprichting import KlMIVLusUitslijprichting
from ...Datatypes.KlMIVMeetpuntAfmetingen import KlMIVMeetpuntAfmetingen
from ...Datatypes.KlMIVMeetpuntGebied import KlMIVMeetpuntGebied
from ...Datatypes.KlMIVWegdek import KlMIVWegdek
from ...Datatypes.KlServicePrioriteit import KlServicePrioriteit
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVMeetpunt(NaampadObject, PuntGeometrie):
    """Een meetpunt van Meten-In-Vlaanderen als plaats waar beide meetlussen bij benadering in de weg ingeslepen zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie', direction='o', deprecated='2.9.0')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus', direction='i', deprecated='2.9.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalkabel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVModule', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus', direction='u')  # u = unidirectional

        self._aansluiting = OTLAttribuut(field=KlAansluitingMIVMeetpunt,
                                         naam='aansluiting',
                                         label='aansluiting',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.aansluiting',
                                         usagenote='Deze eigenschap is tijdelijk toegevoegd in het kader van het verweven van Legacy data en OTL data. De informatie in deze eigenschap zal op termijn moeten worden bijgehouden  in het type Datakabel',
                                         definition='LEGACY-ATTRIBUUT zie usageNote! De aansluiting van de meetlussen op het verwerkingssysteem.',
                                         owner=self)

        self._afmetingen = OTLAttribuut(field=KlMIVMeetpuntAfmetingen,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.afmetingen',
                                        usagenote='De lengte van een lus wordt gemeten parallel aan de rijweg. De breedte dwars op de rijweg. Beide lussen van een MIV meetpunt moeten altijd dezelfde afmetingen hebben.',
                                        definition='De afmetingen van de lussen als lengte en breedte volgens een lijst van vaste afmetingen',
                                        owner=self)

        self._bemetenGebied = OTLAttribuut(field=KlMIVMeetpuntGebied,
                                           naam='bemetenGebied',
                                           label='bemeten gebied',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.bemetenGebied',
                                           definition='Het type gebied waarin de lussen van het meetpunt zich bevinden en waarvoor passerend verkeer gemeten wordt.',
                                           owner=self)

        self._datumHerslijpen = OTLAttribuut(field=DateField,
                                             naam='datumHerslijpen',
                                             label='datum herslijpen',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.datumHerslijpen',
                                             definition='De datum waarop de lussen van het meetpunt laatst herslepen zijn.',
                                             owner=self)

        self._isBedekt = OTLAttribuut(field=BooleanField,
                                      naam='isBedekt',
                                      label='is bedekt',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.isBedekt',
                                      definition='Geeft aan of de lussen bedekt zijn door een toplaag. De bedekking door een toplaag zorgt er voor dat de lus niet zichtbaar is met het blote oog.',
                                      owner=self)

        self._logischeGroepVerkeerscentrum = OTLAttribuut(field=StringField,
                                                          naam='logischeGroepVerkeerscentrum',
                                                          label='logische groep Verkeerscentrum',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.logischeGroepVerkeerscentrum',
                                                          definition='Identificator voor de verzameling van alle naast elkaar gelegen meetpunten op een weg in dezelfde rijrichting, toegekend door het Verkeerscentrum.',
                                                          owner=self)

        self._meetrapport = OTLAttribuut(field=DtcDocument,
                                         naam='meetrapport',
                                         label='meetrapport',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.meetrapport',
                                         usagenote='Bestanden van het type pdf.',
                                         definition='De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen.',
                                         owner=self)

        self._rijstrook = OTLAttribuut(field=KlAlgRijstrookcode,
                                       naam='rijstrook',
                                       label='rijstrook',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.rijstrook',
                                       usagenote='Rijstroken worden genummerd van traag naar snel, te beginnen bij 1. De rechterstrook wordt geacht het traagste verkeer te bevatten. Indien de pechstrook ook een luspaar heeft, krijgt de betrokken rijstrook het cijfer 0.',
                                       definition='De rijstrook waarin het luspaar van het meetpunt ingeslepen is, aangeduid met een oplopend cijfer te beginnen van 1 voor de traagste rijstrook.',
                                       owner=self)

        self._servicePrioriteit = OTLAttribuut(field=KlServicePrioriteit,
                                               naam='servicePrioriteit',
                                               label='service prioriteit',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.servicePrioriteit',
                                               definition='Het prioriteitsniveau dat aangeeft hoe dringend iets moet onderhouden/gerepareerd worden.',
                                               owner=self)

        self._trekput = OTLAttribuut(field=BooleanField,
                                     naam='trekput',
                                     label='trekput',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.trekput',
                                     usagenote='Deze eigenschap is tijdelijk toegevoegd in het kader van het verweven van Legacy data en OTL data. De informatie in deze eigenschap zal op termijn moeten worden bijgehouden  in het type Technische put.',
                                     definition='LEGACY-ATTRIBUUT zie usageNote! Een trekput is een ondergrondse put waarin kabels van meetlussen op snelwegen samenkomen voor verbinding en onderhoud, zonder het wegdek open te breken.',
                                     owner=self)

        self._uitslijprichting = OTLAttribuut(field=KlMIVLusUitslijprichting,
                                              naam='uitslijprichting',
                                              label='uitslijprichting',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.uitslijprichting',
                                              definition='De uitlopers van de lus gaan naar links of naar rechts bekeken ten opzichte van de rijrichting.',
                                              owner=self)

        self._wegdek = OTLAttribuut(field=KlMIVWegdek,
                                    naam='wegdek',
                                    label='wegdek',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.wegdek',
                                    usagenote='Deze eigenschap is tijdelijk toegevoegd in het kader van het verweven van Legacy data en OTL data. De informatie in deze eigenschap zal op termijn moeten worden bijgehouden  in het type Laag.',
                                    definition='LEGACY-ATTRIBUUT zie usageNote! Het type wegdek waarin de meetlussen zijn verwerkt.',
                                    owner=self)

    @property
    def aansluiting(self) -> str:
        """LEGACY-ATTRIBUUT zie usageNote! De aansluiting van de meetlussen op het verwerkingssysteem."""
        return self._aansluiting.get_waarde()

    @aansluiting.setter
    def aansluiting(self, value):
        self._aansluiting.set_waarde(value, owner=self)

    @property
    def afmetingen(self) -> str:
        """De afmetingen van de lussen als lengte en breedte volgens een lijst van vaste afmetingen"""
        return self._afmetingen.get_waarde()

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)

    @property
    def bemetenGebied(self) -> str:
        """Het type gebied waarin de lussen van het meetpunt zich bevinden en waarvoor passerend verkeer gemeten wordt."""
        return self._bemetenGebied.get_waarde()

    @bemetenGebied.setter
    def bemetenGebied(self, value):
        self._bemetenGebied.set_waarde(value, owner=self)

    @property
    def datumHerslijpen(self) -> date:
        """De datum waarop de lussen van het meetpunt laatst herslepen zijn."""
        return self._datumHerslijpen.get_waarde()

    @datumHerslijpen.setter
    def datumHerslijpen(self, value):
        self._datumHerslijpen.set_waarde(value, owner=self)

    @property
    def isBedekt(self) -> bool:
        """Geeft aan of de lussen bedekt zijn door een toplaag. De bedekking door een toplaag zorgt er voor dat de lus niet zichtbaar is met het blote oog."""
        return self._isBedekt.get_waarde()

    @isBedekt.setter
    def isBedekt(self, value):
        self._isBedekt.set_waarde(value, owner=self)

    @property
    def logischeGroepVerkeerscentrum(self) -> str:
        """Identificator voor de verzameling van alle naast elkaar gelegen meetpunten op een weg in dezelfde rijrichting, toegekend door het Verkeerscentrum."""
        return self._logischeGroepVerkeerscentrum.get_waarde()

    @logischeGroepVerkeerscentrum.setter
    def logischeGroepVerkeerscentrum(self, value):
        self._logischeGroepVerkeerscentrum.set_waarde(value, owner=self)

    @property
    def meetrapport(self) -> DtcDocumentWaarden:
        """De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen."""
        return self._meetrapport.get_waarde()

    @meetrapport.setter
    def meetrapport(self, value):
        self._meetrapport.set_waarde(value, owner=self)

    @property
    def rijstrook(self) -> str:
        """De rijstrook waarin het luspaar van het meetpunt ingeslepen is, aangeduid met een oplopend cijfer te beginnen van 1 voor de traagste rijstrook."""
        return self._rijstrook.get_waarde()

    @rijstrook.setter
    def rijstrook(self, value):
        self._rijstrook.set_waarde(value, owner=self)

    @property
    def servicePrioriteit(self) -> str:
        """Het prioriteitsniveau dat aangeeft hoe dringend iets moet onderhouden/gerepareerd worden."""
        return self._servicePrioriteit.get_waarde()

    @servicePrioriteit.setter
    def servicePrioriteit(self, value):
        self._servicePrioriteit.set_waarde(value, owner=self)

    @property
    def trekput(self) -> bool:
        """LEGACY-ATTRIBUUT zie usageNote! Een trekput is een ondergrondse put waarin kabels van meetlussen op snelwegen samenkomen voor verbinding en onderhoud, zonder het wegdek open te breken."""
        return self._trekput.get_waarde()

    @trekput.setter
    def trekput(self, value):
        self._trekput.set_waarde(value, owner=self)

    @property
    def uitslijprichting(self) -> str:
        """De uitlopers van de lus gaan naar links of naar rechts bekeken ten opzichte van de rijrichting."""
        return self._uitslijprichting.get_waarde()

    @uitslijprichting.setter
    def uitslijprichting(self, value):
        self._uitslijprichting.set_waarde(value, owner=self)

    @property
    def wegdek(self) -> str:
        """LEGACY-ATTRIBUUT zie usageNote! Het type wegdek waarin de meetlussen zijn verwerkt."""
        return self._wegdek.get_waarde()

    @wegdek.setter
    def wegdek(self, value):
        self._wegdek.set_waarde(value, owner=self)
