from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Lesson(models.Model):
    title = models.CharField("عنوان", max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField("توضیحات")
    code_snippet = models.TextField("کُد نمونه", blank=True)
    image = models.ImageField("عکس (اختیاری)", upload_to='lessons/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "درس"
        verbose_name_plural = "درس‌ها"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
