class InstaStory:
    def share(self):
        print("Sharing an image story")


class WhatsAppStory:
    def share(self):
        print("Sharing a text status")


instagram = InstaStory()
whatsapp = WhatsAppStory()

instagram.share()
whatsapp.share()