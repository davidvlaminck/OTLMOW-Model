# coding=utf-8
from ...Classes.Abstracten.AbstracteAanvullendeGeometrie import AbstracteAanvullendeGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class AanvullendeMiddellijn(AbstracteAanvullendeGeometrie, LijnGeometrie):
    """Een lijn die het midden of de centrale as van een object markeert, zoals bv. de centrale as van een gracht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AanvullendeMiddellijn'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gracht', direction='i')  # i = direction: incoming
