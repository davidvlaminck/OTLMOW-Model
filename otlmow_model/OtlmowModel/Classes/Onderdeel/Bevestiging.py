# coding=utf-8
from ...Classes.ImplementatieElement.NietDirectioneleRelatie import NietDirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bevestiging(NietDirectioneleRelatie):
    """Deze relatie geeft aan dat twee onderdelen direct fysiek op elkaar bevestigd zijn. Dit kan zowel aan de buitenkant als aan de binnenkant zijn zoals bv. een camera aan een paal of een laagspanningsbord in een kast. Daarnaast omvat deze relatie ook situaties waarin onderdelen niet direct, maar wel structureel of functioneel met elkaar verbonden zijn op een manier die bevestiging impliceert, bv. een trap die eindigt net onder een voetgangersbrug zonder fysieke bevestiging. Deze relatie heeft geen richting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
