from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    content = models.CharField(max_length=300, verbose_name='محتوا')
    done = models.BooleanField(default=False, verbose_name='انجام شده')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['done']),
        ]

        ordering = ['-created']

        verbose_name = 'کار'
        verbose_name_plural = 'کار ها'

    def __str__(self) -> str:
        mess = self.content[:10]
        return f'{mess}...' if len(self.content) > 10 else mess