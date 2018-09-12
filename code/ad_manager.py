from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.adimage import AdImage
from facebookads.adobjects.adcreative import AdCreative

from facebookads.api import FacebookAdsAPI

class AdManager:
    def __init__(self, access_token, app_secret, app_id, id):
        self.access_token = access_token
        self.app_secret = app_secret
        self.app_id = app_id
        self.id = id
        self.connect()

    def connect(self):
        FacebookAdsApi.init(access_token = self.access_token)

    def get_campaign(self, fields, params):
        return AdAccount(self.id).get_campaigns(
            fields = fields,
            params = params,
        )
    
    def add_image(self, image_path):
        image = AdImage(parent_id = 'act_' + self.id)
        image[AdImage.Field.filename] = image_path
        image.remote_create()
        return image[AdImage.Field.hash]
