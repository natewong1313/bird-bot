import requests, time, datetime, json

#modified from https://github.com/lovvskillz/python-discord-webhook 

class DiscordWebhook:
    def __init__(self, url, **kwargs):
        self.url = url
        self.content = kwargs.get("content")
        self.username = kwargs.get("username")
        self.avatar_url = kwargs.get("avatar_url")
        self.tts = kwargs.get("tts", False)
        self.files = kwargs.get("files", dict())
        self.embeds = kwargs.get("embeds", [])
        self.proxies = kwargs.get("proxies", None)

    def add_file(self, file, filename):
        self.files["_{}".format(filename)] = (filename, file)

    def add_embed(self, embed):
        self.embeds.append(embed.__dict__ if isinstance(embed, DiscordEmbed) else embed)

    def remove_embed(self, index):
        self.embeds.pop(index)

    def get_embeds(self):
        return self.embeds

    def set_proxies(self, proxies):
        self.proxies = proxies

    @property
    def json(self):
        data = dict()
        embeds = self.embeds
        self.embeds = list()
        for embed in embeds:
            self.add_embed(embed)
        for key, value in self.__dict__.items():
            if value and key not in ["url", "files", "filename"]:
                data[key] = value
        embeds_empty = all(not embed for embed in data["embeds"]) if "embeds" in data else True
        return data

    def execute(self):
        if bool(self.files) is False:
            response = requests.post(self.url, json=self.json, proxies=self.proxies)
        else:
            self.files["payload_json"] = (None, json.dumps(self.json))
            response = requests.post(self.url, files=self.files, proxies=self.proxies)


class DiscordEmbed:
    def __init__(self, **kwargs):
        self.title = kwargs.get("title")
        self.description = kwargs.get("description")
        self.url = kwargs.get("url")
        self.timestamp = kwargs.get("timestamp")
        self.color = kwargs.get("color")
        self.footer = kwargs.get("footer")
        self.image = kwargs.get("image")
        self.thumbnail = kwargs.get("thumbnail")
        self.video = kwargs.get("video")
        self.provider = kwargs.get("provider")
        self.author = kwargs.get("author")
        self.fields = kwargs.get("fields", [])

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_url(self, url):
        self.url = url

    def set_timestamp(self, timestamp=str(datetime.datetime.utcfromtimestamp(time.time()))):
        self.timestamp = timestamp

    def set_color(self, color):
        self.color = color

    def set_footer(self, **kwargs):
        self.footer = {
            "text": kwargs.get("text"),
            "icon_url": kwargs.get("icon_url"),
            "proxy_icon_url": kwargs.get("proxy_icon_url")
        }

    def set_image(self, **kwargs):
        self.image = {
            "url": kwargs.get("url"),
            "proxy_url": kwargs.get("proxy_url"),
            "height": kwargs.get("height"),
            "width": kwargs.get("width"),
        }

    def set_thumbnail(self, **kwargs):
        self.thumbnail = {
            "url": kwargs.get("url"),
            "proxy_url": kwargs.get("proxy_url"),
            "height": kwargs.get("height"),
            "width": kwargs.get("width"),
        }

    def set_video(self, **kwargs):
        self.video = {
            "url": kwargs.get("url"),
            "height": kwargs.get("height"),
            "width": kwargs.get("width"),
        }

    def set_provider(self, **kwargs):
        self.provider = {
            "name": kwargs.get("name"),
            "url": kwargs.get("url"),
        }

    def set_author(self, **kwargs):
        self.author = {
            "name": kwargs.get("name"),
            "url": kwargs.get("url"),
            "icon_url": kwargs.get("icon_url"),
            "proxy_icon_url": kwargs.get("proxy_icon_url"),
        }

    def add_embed_field(self, **kwargs):
        self.fields.append({
            "name": kwargs.get("name"),
            "value": kwargs.get("value"),
            "inline": kwargs.get("inline", True)
        })

    def del_embed_field(self, index):
        self.fields.pop(index)

    def get_embed_fields(self):
        return self.fields