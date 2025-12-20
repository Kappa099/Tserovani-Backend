from django.db import models

class House(models.Model):
    LISTING_TYPE_CHOICES = [
        ('rent', 'Rent'),
        ('sale', 'Sale'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('house', 'House'),
        ('land', 'Land'),
    ]

    title = models.CharField(max_length=200)          # Short title for the listing
    listing_type = models.CharField(                
        max_length=10,
        choices=LISTING_TYPE_CHOICES
    )
    property_type = models.CharField(                # House or Land
        max_length=10,
        choices=PROPERTY_TYPE_CHOICES
    )
    size = models.DecimalField(                      # Size in square meters
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    location = models.CharField(max_length=200)      # Address or area
    price = models.DecimalField(                     # Price in GEL or USD
        max_digits=12,
        decimal_places=2
    )
    contact = models.CharField(max_length=50)        # Phone/email
    description = models.TextField(blank=True)       # Extra details
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.listing_type} ({self.property_type})"