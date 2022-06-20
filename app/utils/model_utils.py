from app.views.model import uie_model


def extract_fault_event(sentence: str) -> dict:
    fault_event = uie_model([sentence])
    fault_event = fault_event[0]
    res = dict()
    if len(fault_event.items()) == 0:
        return res
    res['fault_trigger'] = fault_event['故障触发词']
    res['fault_location'] = fault_event['部位'] if '部位' in fault_event.keys() else None
    res['fault_adjective'] = fault_event['形容词'] if '形容词' in fault_event.keys() else None

    return res
