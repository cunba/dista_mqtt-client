import math
import time
from models.messaging import Messaging
from payloads.disband_lightning_information_payload import DisbandLightningInformationPayload
from utils.topics import TopicsPublications

class DisbandActionLightning:

    def __init__(self, config):
        self.action = Messaging(config)

    def create_payload(self, lightningData, redData, greenData, blueData, disbandMac):
        payload = DisbandLightningInformationPayload(lightningData, redData, greenData, blueData, disbandMac, math.trunc(time.time()))
        return payload.to_json()

    def public_measure(self, lightningData, redData, greenData, blueData, disbandMac):
        topic = str(TopicsPublications.DISBANDS_ACTION_DISBAND_MAC_LIGHTNING)
        topic = topic.format(disbandMac = disbandMac)
        payloadJson = self.create_payload(lightningData, redData, greenData, blueData, disbandMac)
        self.action.publish(topic, payloadJson)
    