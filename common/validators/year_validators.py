from django.core.validators import RegexValidator

year_validator = RegexValidator(
    regex=r"^\d{4}$", message="Year must be a four-digit number.", code="invalid_year"
)
