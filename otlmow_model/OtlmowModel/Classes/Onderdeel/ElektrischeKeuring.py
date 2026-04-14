# coding=utf-8
from datetime import date
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AbstracteAanvullendeGeometrie import AbstracteAanvullendeGeometrie
from ...Classes.Abstracten.KeuringObject import KeuringObject
from ...BaseClasses.DateField import DateField
from ...Datatypes.KlKeuringsresultaat import KlKeuringsresultaat


# Generated with OTLClassCreator. To modify: extend, do not edit
class ElektrischeKeuring(AbstracteAanvullendeGeometrie, KeuringObject):
    """Een formele controle en beoordeling waarbij wordt nagegaan of de elektrische installatie voldoet aan de geldende wettelijke, normatieve en veiligheidsvereisten, met als doel de elektrische veiligheid en conformiteit te waarborgen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ElektrischeKeuring'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftKeuring', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ForfaitaireAansluiting', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftKeuring', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftKeuring', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', direction='i')  # i = direction: incoming

        self._geldigTot = OTLAttribuut(field=DateField,
                                       naam='geldigTot',
                                       label='geldig tot',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ElektrischeKeuring.geldigTot',
                                       definition='De datum tot en met welke de elektrische keuring als geldig wordt beschouwd, conform de geldende regelgeving of het keuringsverslag, waarna een herkeuring vereist is.',
                                       owner=self)

        self._resultaat = OTLAttribuut(field=KlKeuringsresultaat,
                                       naam='resultaat',
                                       label='resultaat',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ElektrischeKeuring.resultaat',
                                       definition='De uitkomst van de keuring of de asset al dan niet voldoet aan de vastgelegde criteria, normen of voorschriften.',
                                       owner=self)

    @property
    def geldigTot(self) -> date:
        """De datum tot en met welke de elektrische keuring als geldig wordt beschouwd, conform de geldende regelgeving of het keuringsverslag, waarna een herkeuring vereist is."""
        return self._geldigTot.get_waarde()

    @geldigTot.setter
    def geldigTot(self, value):
        self._geldigTot.set_waarde(value, owner=self)

    @property
    def resultaat(self) -> str:
        """De uitkomst van de keuring of de asset al dan niet voldoet aan de vastgelegde criteria, normen of voorschriften."""
        return self._resultaat.get_waarde()

    @resultaat.setter
    def resultaat(self, value):
        self._resultaat.set_waarde(value, owner=self)
