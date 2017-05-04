import operator
from google.cloud import language
from django.conf import settings


def extract_entities(text, salience_threshold=0.05, max_results=50):
    """ extract entities from plain text, in order of salience,
        where the salience exceeds the threshold, to a maximum limit
    """
    # return ["Wagtail", "Torchbox", "Python", "Django"]

    client = language.Client.from_service_account_json(settings.NLP_API_KEY)

    document = client.document_from_text(text)
    entity_response = document.analyze_entities()

    entity_dict = {}

    for entity in entity_response.entities:
        if entity.salience > salience_threshold:
            if entity.entity_type != 'OTHER':
                entity_dict[entity.name] = entity.salience

    sorted_entities = sorted(entity_dict.items(),
                             key=operator.itemgetter(1),
                             reverse=True)
    limited_entities = sorted_entities[:max_results]
    return [x[0] for x in limited_entities]


txt = """Unusually for the Arab
world, Moroccan elections have 
the merit of not being entirely predictable. This is 
partly because conducting public opinion polls ahead 
of voting is prohibited, but also because the 'dirty 
tricks' department of the Ministry of Interior has 
reined in its horns in recent years. King Mohammed 
VI of Morocco is understood to want a genuine political 
arena to develop, in order to balance, if not 
counterbalance the ultimate political authority the 
palace still enjoys. The 2011 general election victory 
of the Islamist-led government of the Party for 
Justice and Development (PJD) was seen as an 
experiment in affording greater executive leeway 
to a popularly elected party."""


if __name__ == "__main__":
    print extract_entities(txt)
