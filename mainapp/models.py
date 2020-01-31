from django.db import models


class CarMaker(models.Model):

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    IS_COMMON = '1'
    NOT_COMMON = '0'

    COMMON_CHOICES = (
        (IS_COMMON, 'распространён'),
        (NOT_COMMON, 'не распространён'),
    )

    make_id = models.CharField(verbose_name="id производителя", max_length=30, primary_key=True)
    make_display = models.CharField(verbose_name="Имя производителя", max_length=30)
    make_is_common = models.CharField(verbose_name="Распространённость производителя", max_length=1,
                                      choices=COMMON_CHOICES)
    make_country = models.CharField(verbose_name="Страна производителя", max_length=30)

    def __str__(self):
        return f'{self.make_display} ({self.make_country})'
