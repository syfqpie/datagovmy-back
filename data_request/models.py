from django.db import models
from django.core.exceptions import ValidationError
from data_catalogue.models import DataCatalogueMeta


# Create your models here.
class DataRequest(models.Model):
    STATUS_CHOICES = [
        ("submitted", "Submitted"),
        ("under_review", "Under Review"),
        ("rejected", "Rejected"),
        ("in_progress", "In Progress"),
        ("data_published", "Data Published"),
    ]
    ticket_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    institution = models.CharField(max_length=255, blank=True, null=True)
    dataset_title = models.CharField(max_length=255)  # translatable
    dataset_description = models.TextField()  # translatable
    agency = models.CharField(max_length=255)
    purpose_of_request = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="submitted"
    )
    rejection_reason = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.ticket_id} ({self.dataset_title})"

    def clean(self) -> None:
        if self.status == "rejected" and not self.rejection_reason:
            raise ValidationError(
                {
                    "rejection_reason": 'Rejection reason is required when the status is "rejected".'
                }
            )

        if self.status == "data_published":
            linked_catalogues_count = DataCatalogueMeta.objects.filter(
                data_request=self
            ).count()
            if linked_catalogues_count < 1:
                raise ValidationError(
                    'At least one data catalogue must be linked when the status is "data_published".'
                )

        return super().clean()
