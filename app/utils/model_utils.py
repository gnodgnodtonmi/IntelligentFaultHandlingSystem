import torch
from torch import cosine_similarity

from app.views.model import uie_model, sbert_model


def extract_fault_event(sentence: str) -> dict:
    fault_event = uie_model([sentence])
    fault_event = fault_event[0]
    print(fault_event)
    res = dict()
    if len(fault_event.items()) == 0:
        return res
    res['fault_trigger'] = fault_event['故障触发词'][0]['text']
    res['fault_location'] = fault_event['故障触发词'][0]['relations']['部位'][0]['text'] \
        if '部位' in fault_event['故障触发词'][0]['relations'].keys() else None
    res['fault_adjective'] = fault_event['故障触发词'][0]['relations']['形容词'][0]['text'] \
        if '形容词' in fault_event['故障触发词'][0]['relations'].keys() else None

    return res


def text_semantic_matching(key_sentence: str,
                           query_sentence_list: list
                           ) -> dict:
    key_encode = sbert_model.encode(key_sentence)
    query_encode = sbert_model.encode(query_sentence_list)

    key_tensor = torch.tensor(key_encode)
    query_tensor = torch.tensor(query_encode)

    cos_sim = cosine_similarity(key_tensor, query_tensor)
    match_index = cos_sim.argmax().item()
    match_text = query_sentence_list[match_index]

    res = {'match_index': match_index,
           'match_text': match_text}

    return res
