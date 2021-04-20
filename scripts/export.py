import sdmx
import yaml
import os
from sdg.translations import TranslationInputSdmx

msg = sdmx.read_sdmx('dsd.xml')
dsd = msg.structure[0]

for subdir, dirs, files in os.walk('translations'):
    if subdir == 'translations':
        continue
    language = os.path.split(subdir)[1]
    for filename in files:
        concept_code = os.path.splitext(filename)[0]
        filepath = os.path.join('translations', language, filename)
        with open(filepath, 'r', encoding='utf-8') as stream:
            translations = yaml.load(stream, Loader=yaml.FullLoader)

        concept = None
        dimension_matches = [dim for dim in dsd.dimensions if dim.id == concept_code]
        if len(dimension_matches) > 0:
            concept = dimension_matches[0]
        else:
            attribute_matches = [att for att in dsd.attributes if att.id == concept_code]
            if len(attribute_matches) > 0:
                concept = attribute_matches[0]

        if concept.local_representation is not None and concept.local_representation.enumerated is not None:
            for code in concept.local_representation.enumerated:
                if code.id in translations and translations[code.id] != '':
                    code.name[language] = translations[code.id]

with open(os.path.join('public', 'dsd-exported.xml'), 'wb') as f:
    f.write(sdmx.to_xml(msg, encoding='utf-8', pretty_print=True))
