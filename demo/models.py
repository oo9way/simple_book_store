from typing import Iterable
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Book(models.Model):
    title = models.CharField("Nom", max_length=255, validators=[MinLengthValidator(10), MaxLengthValidator(15)])
    isbn = models.PositiveIntegerField(verbose_name="ISBN kodi")
    qty = models.PositiveIntegerField(verbose_name="Bazadagi soni", default=0)
    price = models.IntegerField(verbose_name="Narxi", default=0)
    image = models.ImageField(upload_to="book_images", null=True, blank=True)

    # Custom methods
    def get_total_price(self):
        return self.qty * self.price
    
    def sotuvda_bormi(self):
        if self.qty != 0:
            return True
        return False
    
    def print_hello(self):
        return f"{self.title} -- HELLO"
    
    def print_new_object_message(self):
        print(f"{self.title} kitobi qo'shildi")


    # Parent methods (boshqatdan yozilgan)
    def __str__(self) -> str:
        return self.title
    
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.print_new_object_message()
    #     self.title = self.title.upper()
    #     return super().save(*args, *kwargs)
    

class NaqdOrCard(models.TextChoices):
    NAQD = ("naqd", "Naqd",)
    CARD = ("card", "Karta", )
    LOAN = ("loan", "Nasiya", )


class Sale(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="sales", help_text="Bu yerdan kitobni tanla")
    qty = models.PositiveIntegerField("Sotilgan soni", default=0, help_text="Bu yerga sotilgan sonini kirit")
    price = models.IntegerField(verbose_name="Sotilgan narxi", default=0, editable=False)
    total_price = models.IntegerField(verbose_name="Umumiy savdo", default=0, editable=False)
    payment_type = models.CharField("To'lov turi", max_length=4, choices=NaqdOrCard.choices)
    
    created_at = models.DateTimeField("Savdo sanasi", auto_now=True)

    def clean(self) -> None:
        book = self.book
        if book.qty < self.qty:
            raise ValidationError(
                {
                    "qty": "Yetarli kitob mavjud emas"
                }
            )

        return super().clean()
    

    def save(self, *args, **kwargs) -> None:
        if not self.id:
            qty = self.qty
            book = self.book

            self.price = book.price
            self.total_price = book.price * qty

            book.qty = book.qty - qty
            book.save()


        return super().save(*args, *kwargs)
    


class Todo(models.Model):
    STATUS = {
        "not_started": "Boshlanmagan",
        "started": "Jarayonda",
        "finished": "Tugatilgan"
    }
    
    task = models.CharField("Vazifa", max_length=255)
    status = models.CharField(choices=STATUS, max_length=16, default="not_started")