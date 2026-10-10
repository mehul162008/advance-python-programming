class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email")


class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS")


email = EmailNotification()
sms = SMSNotification()

email.send()
sms.send()