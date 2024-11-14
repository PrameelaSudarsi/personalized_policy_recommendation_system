def validate_age(age: int) -> bool:
    """Validate that the age is within the allowed range (18 to 120)."""
    return 18 <= age <= 120

def validate_gender(gender: str) -> bool:
    """Validate that the gender is one of the accepted values."""
    return gender in ["Male", "Female", "Other"]

def validate_marital_status(marital_status: str) -> bool:
    """Validate that the marital status is one of the accepted values."""
    return marital_status in ["Single", "Married", "Divorced", "Widowed"]

def validate_smoking_status(smoking_status: str) -> bool:
    """Validate that the smoking status is either 'Yes' or 'No'."""
    return smoking_status in ["Yes", "No"]

def validate_drinking_status(drinking_status: str) -> bool:
    """Validate that the drinking status is either 'Yes' or 'No'."""
    return drinking_status in ["Yes", "No"]

def validate_chronic_conditions(chronic_conditions: str) -> bool:
    """Check if chronic conditions is a non-empty string. Comma-separated values are allowed."""
    return isinstance(chronic_conditions, str)

def validate_income(income: float) -> bool:
    """Validate that the income is a positive number."""
    return income > 0

def validate_occupation(occupation: str) -> bool:
    """Validate that the occupation is a non-empty string."""
    return isinstance(occupation, str) and len(occupation.strip()) > 0

def validate_dependents(dependents: int) -> bool:
    """Validate that dependents is a non-negative integer."""
    return dependents >= 0

def validate_health_status(health_status: str) -> bool:
    """Validate that the health status is one of the accepted values: 'good', 'fair', or 'poor'."""
    return health_status in ["good", "fair", "poor"]

def validate_family_health_history(family_health_history: str) -> bool:
    """Check if family health history is a string, comma-separated values allowed."""
    return isinstance(family_health_history, str)

def validate_user_data(user_data) -> bool:
    """Validate all fields in the user_data object."""
    return (
        validate_age(user_data.age) and
        validate_gender(user_data.gender) and
        validate_marital_status(user_data.marital_status) and
        validate_smoking_status(user_data.smoking_status) and
        validate_drinking_status(user_data.drinking_status) and
        validate_chronic_conditions(user_data.chronic_conditions) and
        validate_income(user_data.annual_income) and
        validate_occupation(user_data.occupation) and
        validate_dependents(user_data.dependents) and
        validate_health_status(user_data.health_status) and
        validate_family_health_history(user_data.family_health_history)
    )
