from django.db import models
from django.conf import settings



class regtable(models.Model):
    firstname=models.CharField(max_length=150)
    lastname=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    password=models.CharField(max_length=120) 





class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username}"


class NGO(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    organization_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    proof = models.FileField(upload_to='ngo_proofs/')
    is_approved = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.organization_name} ({'Approved' if self.is_approved else 'Pending'})"


class Product(models.Model):
    class Category(models.TextChoices):
        SELL = 'SELL', 'Sell'
        BUY = 'BUY', 'Buy'
        DONATE = 'DONATE', 'Donate'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=Category.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.category}"


class Donation(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        ACCEPTED = 'ACCEPTED', 'Accepted'
        REJECTED = 'REJECTED', 'Rejected'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='donations')
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE, related_name='donations')
    product_details = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)
    feedback = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation by {self.user} to {self.ngo} - {self.status}"


class Complaint(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='complaints')
    title = models.CharField(max_length=200)
    description = models.TextField()
    reply = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.sender}"