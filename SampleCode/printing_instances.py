from otlmow_model.Classes.Onderdeel.Bevestiging import Bevestiging
from otlmow_model.Classes.Onderdeel.Verkeersregelaar import Verkeersregelaar
from otlmow_model.Classes.Onderdeel.Wegkantkast import Wegkantkast

from otlmow_model.Helpers.RelationCreator import create_relation

if __name__ == "__main__":
    from otlmow_model.Helpers.AssetCreator import dynamic_create_instance_from_ns_and_name
    camera = dynamic_create_instance_from_ns_and_name(namespace='onderdeel', class_name='Camera')
    print(camera)

    vr = Verkeersregelaar()
    vr.assetId.identificator = '00000000-0000-0000-0000-000000000001'
    relation = create_relation(source=vr, target_typeURI=Wegkantkast.typeURI,
                               target_uuid='00000000-0000-0000-0000-000000000002', relation_type=Bevestiging)
    print(relation)


