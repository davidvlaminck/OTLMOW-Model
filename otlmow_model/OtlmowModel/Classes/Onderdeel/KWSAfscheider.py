# coding=utf-8
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...BaseClasses.BooleanField import BooleanField
from ...Datatypes.DtcAfmetingDiameterInMm import DtcAfmetingDiameterInMm, DtcAfmetingDiameterInMmWaarden
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlMateriaalKuipKWSAfscheider import KlMateriaalKuipKWSAfscheider
from ...Datatypes.KwantWrdInKubiekeMeterPerSeconde import KwantWrdInKubiekeMeterPerSeconde, KwantWrdInKubiekeMeterPerSecondeWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class KWSAfscheider(AIMNaamObject, PuntGeometrie):
    """Een toestel in een afwaterings- of rioleringsstelsel dat niet met water mengbare lichte vloeistoffen van minerale oorsprong, zoals olie en brandstoffen, door zwaartekracht en eventueel met behulp van coalescentie uit afval- of afstromend water afscheidt en tijdelijk vasthoudt vóór verdere afvoer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KWSAfscheider'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis', direction='i')  # i = direction: incoming

        self._afmeting = OTLAttribuut(field=DtcAfmetingDiameterInMm,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KWSAfscheider.afmeting',
                                      definition='De kenmerkende uitwendige afmetingen van de KWS-afscheider.',
                                      owner=self)

        self._heeftAutomatischeAfsluiter = OTLAttribuut(field=BooleanField,
                                                        naam='heeftAutomatischeAfsluiter',
                                                        label='heeft automatische afsluiter',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KWSAfscheider.heeftAutomatischeAfsluiter',
                                                        definition='Geeft aan of de KWS-afscheider een voorziening bevat die de uitlaat automatisch afsluit wanneer de maximaal toegelaten hoeveelheid afgescheiden koolwaterstoffen is bereikt.',
                                                        owner=self)

        self._heeftCoalescentiefilter = OTLAttribuut(field=BooleanField,
                                                     naam='heeftCoalescentiefilter',
                                                     label='heeft coalescentiefilter',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KWSAfscheider.heeftCoalescentiefilter',
                                                     definition='Geeft aan of de KWS-afscheider een voorziening bevat die fijne druppels koolwaterstoffen laat samenvloeien tot grotere druppels om hun afscheiding uit het water te bevorderen.',
                                                     owner=self)

        self._heeftGeintegreerdeSlibvanger = OTLAttribuut(field=BooleanField,
                                                          naam='heeftGeintegreerdeSlibvanger',
                                                          label='heeft geintegreerde slibvanger',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KWSAfscheider.heeftGeintegreerdeSlibvanger',
                                                          definition='Geeft aan of de KWS-afscheider een geïntegreerd compartiment bevat voor het afscheiden en tijdelijk opslaan van bezinkbare stoffen, zoals zand en slib.',
                                                          owner=self)

        self._heeftLekdetectie = OTLAttribuut(field=BooleanField,
                                              naam='heeftLekdetectie',
                                              label='heeft lekdetectie',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KWSAfscheider.heeftLekdetectie',
                                              definition='Geeft aan of de KWS-afscheider een voorziening bevat voor het detecteren van lekkage uit de vloeistofdichte behuizing of van vloeistof in een daarvoor bestemde tussenruimte.',
                                              owner=self)

        self._materiaalKuip = OTLAttribuut(field=KlMateriaalKuipKWSAfscheider,
                                           naam='materiaalKuip',
                                           label='materiaal kuip KWS afscheider',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KWSAfscheider.materiaalKuip',
                                           definition='Het hoofdmateriaal waaruit de vloeistofdichte kuip van de KWS-afscheider is vervaardigd.',
                                           owner=self)

        self._nominaalDebiet = OTLAttribuut(field=KwantWrdInKubiekeMeterPerSeconde,
                                            naam='nominaalDebiet',
                                            label='nominaal debiet',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KWSAfscheider.nominaalDebiet',
                                            definition='Het door de fabrikant opgegeven debiet dat de KWS-afscheider onder nominale ontwerpcondities kan behandelen met behoud van de vooropgestelde afscheidingsprestatie.',
                                            owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KWSAfscheider.technischeFiche',
                                             definition='Een document van de fabrikant waarin de technische kenmerken, prestaties, afmetingen, opbouw en gebruiksvoorwaarden van de KWS-afscheider zijn beschreven.',
                                             owner=self)

    @property
    def afmeting(self) -> DtcAfmetingDiameterInMmWaarden:
        """De kenmerkende uitwendige afmetingen van de KWS-afscheider."""
        return self._afmeting.get_waarde()

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def heeftAutomatischeAfsluiter(self) -> bool:
        """Geeft aan of de KWS-afscheider een voorziening bevat die de uitlaat automatisch afsluit wanneer de maximaal toegelaten hoeveelheid afgescheiden koolwaterstoffen is bereikt."""
        return self._heeftAutomatischeAfsluiter.get_waarde()

    @heeftAutomatischeAfsluiter.setter
    def heeftAutomatischeAfsluiter(self, value):
        self._heeftAutomatischeAfsluiter.set_waarde(value, owner=self)

    @property
    def heeftCoalescentiefilter(self) -> bool:
        """Geeft aan of de KWS-afscheider een voorziening bevat die fijne druppels koolwaterstoffen laat samenvloeien tot grotere druppels om hun afscheiding uit het water te bevorderen."""
        return self._heeftCoalescentiefilter.get_waarde()

    @heeftCoalescentiefilter.setter
    def heeftCoalescentiefilter(self, value):
        self._heeftCoalescentiefilter.set_waarde(value, owner=self)

    @property
    def heeftGeintegreerdeSlibvanger(self) -> bool:
        """Geeft aan of de KWS-afscheider een geïntegreerd compartiment bevat voor het afscheiden en tijdelijk opslaan van bezinkbare stoffen, zoals zand en slib."""
        return self._heeftGeintegreerdeSlibvanger.get_waarde()

    @heeftGeintegreerdeSlibvanger.setter
    def heeftGeintegreerdeSlibvanger(self, value):
        self._heeftGeintegreerdeSlibvanger.set_waarde(value, owner=self)

    @property
    def heeftLekdetectie(self) -> bool:
        """Geeft aan of de KWS-afscheider een voorziening bevat voor het detecteren van lekkage uit de vloeistofdichte behuizing of van vloeistof in een daarvoor bestemde tussenruimte."""
        return self._heeftLekdetectie.get_waarde()

    @heeftLekdetectie.setter
    def heeftLekdetectie(self, value):
        self._heeftLekdetectie.set_waarde(value, owner=self)

    @property
    def materiaalKuip(self) -> str:
        """Het hoofdmateriaal waaruit de vloeistofdichte kuip van de KWS-afscheider is vervaardigd."""
        return self._materiaalKuip.get_waarde()

    @materiaalKuip.setter
    def materiaalKuip(self, value):
        self._materiaalKuip.set_waarde(value, owner=self)

    @property
    def nominaalDebiet(self) -> KwantWrdInKubiekeMeterPerSecondeWaarden:
        """Het door de fabrikant opgegeven debiet dat de KWS-afscheider onder nominale ontwerpcondities kan behandelen met behoud van de vooropgestelde afscheidingsprestatie."""
        return self._nominaalDebiet.get_waarde()

    @nominaalDebiet.setter
    def nominaalDebiet(self, value):
        self._nominaalDebiet.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """Een document van de fabrikant waarin de technische kenmerken, prestaties, afmetingen, opbouw en gebruiksvoorwaarden van de KWS-afscheider zijn beschreven."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
