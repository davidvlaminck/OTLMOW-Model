# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlDekselKaderType import KlDekselKaderType
from ...Datatypes.KlDekselKlasse import KlDekselKlasse
from ...Datatypes.KlDekselMateriaal import KlDekselMateriaal
from ...Datatypes.KlDekselRegeling import KlDekselRegeling
from ...Datatypes.KlDekselVergrendeling import KlDekselVergrendeling
from ...Datatypes.KlRioleringVorm import KlRioleringVorm
from ...Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter, KwantWrdInCentimeterWaarden
from ...Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter, KwantWrdInMillimeterWaarden
from ...Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter, KwantWrdInVierkanteMeterWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class PutBovenbouw(AIMObject, PuntGeometrie, VlakGeometrie):
    """Een combinatie van het riooldeksel met de kader en de regeling."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DrogePompkelder', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactpunt', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TechnischePut', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#InspectieputRiolering', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koker', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokersectie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', direction='o')  # o = direction: outgoing

        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.breedte',
                                     definition='Breedte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de hoogte.',
                                     owner=self)

        self._dekselklasse = OTLAttribuut(field=KlDekselKlasse,
                                          naam='dekselklasse',
                                          label='dekselklasse',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.dekselklasse',
                                          definition='Bepaalt de mate waarin het deksel van de bovenbouw belast kan worden door voertuigen.',
                                          owner=self)

        self._dekselvorm = OTLAttribuut(field=KlRioleringVorm,
                                        naam='dekselvorm',
                                        label='dekselvorm',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.dekselvorm',
                                        definition='Bepaalt de vorm van het deksel.',
                                        owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.hoogte',
                                    definition='Hoogte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de breedte.',
                                    owner=self)

        self._hoogteAfdekkingsinrichting = OTLAttribuut(field=KwantWrdInMillimeter,
                                                        naam='hoogteAfdekkingsinrichting',
                                                        label='hoogte afdekkingsinrichting',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.hoogteAfdekkingsinrichting',
                                                        definition='De afstand in millimeter gemeten tussen de bovenkant van het deksel en de bovenkant van de regeling.',
                                                        owner=self)

        self._hoogteBovenbouw = OTLAttribuut(field=KwantWrdInMillimeter,
                                             naam='hoogteBovenbouw',
                                             label='hoogte bovenbouw',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.hoogteBovenbouw',
                                             definition='De afstand in millimeter gemeten tussen de bovenkant van het deksel en de bovenkant van de regeling.',
                                             owner=self)

        self._hoogteRegeling = OTLAttribuut(field=KwantWrdInMillimeter,
                                            naam='hoogteRegeling',
                                            label='hoogte regeling',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.hoogteRegeling',
                                            definition='De afstand in millimeter gemeten tussen de onderkant van de afdekkingsinrichting tot aan de bovenkant van de afdekplaat.',
                                            owner=self)

        self._isAfgesloten = OTLAttribuut(field=BooleanField,
                                          naam='isAfgesloten',
                                          label='is afgesloten',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.isAfgesloten',
                                          definition='Bepaling of de afsluitinrichting vergrendeld is of niet.',
                                          owner=self)

        self._isScharnierend = OTLAttribuut(field=BooleanField,
                                            naam='isScharnierend',
                                            label='is scharnierend',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.isScharnierend',
                                            definition='Het deksel is al of niet bevestigd met een scharnier.',
                                            owner=self)

        self._isWaterdichtVergrendeld = OTLAttribuut(field=BooleanField,
                                                     naam='isWaterdichtVergrendeld',
                                                     label='is waterdicht vergrendeld',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.isWaterdichtVergrendeld',
                                                     definition='Geeft aan of de bovenbouw al dan niet waterdicht vergrendeld is zodat het water zich niet boven de bovenbouw kan begeven.',
                                                     owner=self)

        self._kader = OTLAttribuut(field=KlDekselKaderType,
                                   naam='kader',
                                   label='kader',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.kader',
                                   definition='Bepaalt het type van het dekselkader.',
                                   owner=self)

        self._materiaal = OTLAttribuut(field=KlDekselMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.materiaal',
                                       definition='Het materiaal waaruit het deksel van de bovenbouw is vervaardigd.',
                                       owner=self)

        self._oppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                         naam='oppervlakte',
                                         label='oppervlakte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.oppervlakte',
                                         definition='De oppervlakte van het zichtbare deel van de bovenbouw in vierkante meter.',
                                         owner=self)

        self._regeling = OTLAttribuut(field=KlDekselRegeling,
                                      naam='regeling',
                                      label='regeling',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.regeling',
                                      definition='De wijze hoe de regeling van het deksel is uitgevoerd.',
                                      owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.technischeFiche',
                                             usagenote='Bestanden van het type xlsx of pdf.',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de bovenbouw.',
                                             owner=self)

        self._vergrendeling = OTLAttribuut(field=KlDekselVergrendeling,
                                           naam='vergrendeling',
                                           label='vergrendeling',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw.vergrendeling',
                                           definition='Bepaalt het type sleutel voor het ontgrendelen van het deksel.',
                                           owner=self)

    @property
    def breedte(self) -> KwantWrdInCentimeterWaarden:
        """Breedte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de hoogte."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def dekselklasse(self) -> str:
        """Bepaalt de mate waarin het deksel van de bovenbouw belast kan worden door voertuigen."""
        return self._dekselklasse.get_waarde()

    @dekselklasse.setter
    def dekselklasse(self, value):
        self._dekselklasse.set_waarde(value, owner=self)

    @property
    def dekselvorm(self) -> str:
        """Bepaalt de vorm van het deksel."""
        return self._dekselvorm.get_waarde()

    @dekselvorm.setter
    def dekselvorm(self, value):
        self._dekselvorm.set_waarde(value, owner=self)

    @property
    def hoogte(self) -> KwantWrdInCentimeterWaarden:
        """Hoogte-afmeting van het deksel in centimeter. Bij vierkante en cirkelvormige deksels is deze waarde gelijk aan de breedte."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def hoogteAfdekkingsinrichting(self) -> KwantWrdInMillimeterWaarden:
        """De afstand in millimeter gemeten tussen de bovenkant van het deksel en de bovenkant van de regeling."""
        return self._hoogteAfdekkingsinrichting.get_waarde()

    @hoogteAfdekkingsinrichting.setter
    def hoogteAfdekkingsinrichting(self, value):
        self._hoogteAfdekkingsinrichting.set_waarde(value, owner=self)

    @property
    def hoogteBovenbouw(self) -> KwantWrdInMillimeterWaarden:
        """De afstand in millimeter gemeten tussen de bovenkant van het deksel en de bovenkant van de regeling."""
        return self._hoogteBovenbouw.get_waarde()

    @hoogteBovenbouw.setter
    def hoogteBovenbouw(self, value):
        self._hoogteBovenbouw.set_waarde(value, owner=self)

    @property
    def hoogteRegeling(self) -> KwantWrdInMillimeterWaarden:
        """De afstand in millimeter gemeten tussen de onderkant van de afdekkingsinrichting tot aan de bovenkant van de afdekplaat."""
        return self._hoogteRegeling.get_waarde()

    @hoogteRegeling.setter
    def hoogteRegeling(self, value):
        self._hoogteRegeling.set_waarde(value, owner=self)

    @property
    def isAfgesloten(self) -> bool:
        """Bepaling of de afsluitinrichting vergrendeld is of niet."""
        return self._isAfgesloten.get_waarde()

    @isAfgesloten.setter
    def isAfgesloten(self, value):
        self._isAfgesloten.set_waarde(value, owner=self)

    @property
    def isScharnierend(self) -> bool:
        """Het deksel is al of niet bevestigd met een scharnier."""
        return self._isScharnierend.get_waarde()

    @isScharnierend.setter
    def isScharnierend(self, value):
        self._isScharnierend.set_waarde(value, owner=self)

    @property
    def isWaterdichtVergrendeld(self) -> bool:
        """Geeft aan of de bovenbouw al dan niet waterdicht vergrendeld is zodat het water zich niet boven de bovenbouw kan begeven."""
        return self._isWaterdichtVergrendeld.get_waarde()

    @isWaterdichtVergrendeld.setter
    def isWaterdichtVergrendeld(self, value):
        self._isWaterdichtVergrendeld.set_waarde(value, owner=self)

    @property
    def kader(self) -> str:
        """Bepaalt het type van het dekselkader."""
        return self._kader.get_waarde()

    @kader.setter
    def kader(self, value):
        self._kader.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit het deksel van de bovenbouw is vervaardigd."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def oppervlakte(self) -> KwantWrdInVierkanteMeterWaarden:
        """De oppervlakte van het zichtbare deel van de bovenbouw in vierkante meter."""
        return self._oppervlakte.get_waarde()

    @oppervlakte.setter
    def oppervlakte(self, value):
        self._oppervlakte.set_waarde(value, owner=self)

    @property
    def regeling(self) -> str:
        """De wijze hoe de regeling van het deksel is uitgevoerd."""
        return self._regeling.get_waarde()

    @regeling.setter
    def regeling(self, value):
        self._regeling.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> List[DtcDocumentWaarden]:
        """De technische fiche van de bovenbouw."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def vergrendeling(self) -> str:
        """Bepaalt het type sleutel voor het ontgrendelen van het deksel."""
        return self._vergrendeling.get_waarde()

    @vergrendeling.setter
    def vergrendeling(self, value):
        self._vergrendeling.set_waarde(value, owner=self)
