# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AIMNaamObject(AIMObject):
    """Abstracte als de basisklasse voor elk OTL object dat benoemd wordt met een mensleesbare identificator."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMNaamObject.naam',
                                  definition='De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt.',
                                  owner=self)

    @property
    def naam(self) -> str:
        """De mensleesbare naam van een asset zoals dit bv. ook terug te vinden is op een etiket op het object zelf. De assetbeheerder kent deze naam toe of geeft de opdracht om deze toe te kennen. Indien een object een algemeen gangbare naam heeft zoals bv. bij een waterloop dan wordt deze gebruikt."""
        return self._naam.get_waarde()

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)
