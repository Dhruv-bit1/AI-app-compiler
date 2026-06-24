def validate_schema(schema):

    required_sections = [
        "ui_schema",
        "api_schema",
        "db_schema",
        "auth_schema"
    ]

    errors = []

    for section in required_sections:
        if section not in schema:
            errors.append(f"Missing section: {section}")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }