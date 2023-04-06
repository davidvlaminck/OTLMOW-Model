# coding=utf-8
from datetime import date
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.BaseClasses.DateField import DateField
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlAlgRijstrookcode import KlAlgRijstrookcode
from otlmow_model.Datatypes.KlMIVLusUitslijprichting import KlMIVLusUitslijprichting
from otlmow_model.Datatypes.KlMIVMeetpuntAfmetingen import KlMIVMeetpuntAfmetingen
from otlmow_model.Datatypes.KlMIVMeetpuntGebied import KlMIVMeetpuntGebied
from otlmow_model.Datatypes.KlServicePrioriteit import KlServicePrioriteit
from otlmow_model.BaseClasses.StringField import StringField
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVMeetpunt(AIMNaamObject, PuntGeometrie):
    """Een meetpunt van Meten-In-Vlaanderen als plaats waar beide meetlussen bij benadering in de weg ingeslepen zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie')

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

        self._uitslijprichting = OTLAttribuut(field=KlMIVLusUitslijprichting,
                                              naam='uitslijprichting',
                                              label='uitslijprichting',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt.uitslijprichting',
                                              definition='De uitlopers van de lus gaan naar links of naar rechts bekeken ten opzichte van de rijrichting.',
                                              owner=self)

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
    def uitslijprichting(self) -> str:
        """De uitlopers van de lus gaan naar links of naar rechts bekeken ten opzichte van de rijrichting."""
        return self._uitslijprichting.get_waarde()

    @uitslijprichting.setter
    def uitslijprichting(self, value):
        self._uitslijprichting.set_waarde(value, owner=self)
