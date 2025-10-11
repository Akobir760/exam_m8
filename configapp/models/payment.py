from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PaymentType(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Payment(BaseModel):
    user = models.ForeignKey("configapp.AccountModel", on_delete=models.CASCADE, related_name="payments")
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, related_name="payments")

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.amount} ({self.payment_type.name})"
