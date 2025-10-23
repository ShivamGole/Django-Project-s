from django.db import models

class Doctor(models.Model):
    """
    Model representing a doctor in the Health Hub system.
    This model stores information about doctors including their name, specialization, location, experience, and contact details.
    """
    name = models.CharField(max_length=100, help_text="Full name of the doctor")
    specialization = models.CharField(max_length=100, help_text="Medical specialization (e.g., Cardiology, Dermatology)")
    location = models.CharField(max_length=100, help_text="City or area where the doctor practices")
    experience = models.PositiveIntegerField(help_text="Years of experience")
    contact = models.CharField(max_length=15, help_text="Contact phone number")

    def __str__(self):
        """
        String representation of the Doctor model.
        Returns the doctor's name for easy identification in admin and queries.
        """
        return self.name

    class Meta:
        """
        Meta class for Doctor model.
        Defines verbose names for better readability in admin interface.
        """
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
