from django.db import models
import telepot, pywhatkit

token = "5597818811:AAFMFHNDLhFEXYeroNpoUXIGYpswjq4Dfiw";
## Anass
rece_id1 = "5746505883"
## Imrane
rece_id2 = "5465569016"
bot = telepot.Bot(token);

class Temperature (models.Model):
    temp = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)
    counter = 0

    def __str__(self):
        return str(self.temp)

    def save(self , *args , **kwargs) :
        if self.temp < 5:
            Temperature.counter = 0
            #bot.sendMessage(rece_id, str(self.temp) + "(Excellent✅)")
        if self.temp >= 5 and self.temp < 8:
            bot.sendMessage(rece_id1, str(self.temp) + "(Danger modéré⚠️)")
            Temperature.counter += 1
        elif self.temp >= 8:
            bot.sendMessage(rece_id1, str(self.temp) + "(Niveau critique🚨)")
            Temperature.counter += 1
        if self.temp >= 5 and self.temp < 8 and Temperature.counter > 10:
            bot.sendMessage(rece_id1, str(self.temp) + "(Danger modéré⚠️)")
            bot.sendMessage(rece_id2, str(self.temp) + "(Danger modéré⚠️)")
        elif self.temp >= 8 and Temperature.counter > 10:
            bot.sendMessage(rece_id1, str(self.temp) + "(Niveau critique🚨)")
            bot.sendMessage(rece_id2, str(self.temp) + "(Niveau critique🚨)")
        return super().save(*args, **kwargs)
