from datetime import date


def format_visitor_name(name):
    """
    Format a name as 'Surname, Given names' for the ticket.

    Raise ValueError if name is not text or contains no words.
    """
    if not isinstance(name, str):
        raise ValueError("Visitor name must be text.")

    parts = name.split()
    if not parts:
        raise ValueError("Visitor name cannot be empty or whitespace.")

    surname = parts[-1].title()
    given_names = ' '.join(parts[:-1]).title()
    if not given_names:
        return surname
    return surname + ', ' + given_names

def parse_group_ages(text):
    """
    Parse space-separated, non-negative whole-number ages into a list.

    Raise ValueError if the input is not text or contains invalid ages.
    """
    if not isinstance(text, str):
        raise ValueError("Group ages must be text.")

    age_values = text.split()
    if not age_values:
        raise ValueError("Enter at least one age.")

    ages = []
    for value in age_values:
        if not value.isdecimal():
            raise ValueError("Ages must be non-negative whole numbers.")
        ages.append(int(value))
    return ages

def parse_visit_date(text):
    """
    Parse a real YYYY-MM-DD date into a (year, month, day) tuple.

    Raise ValueError if the input is malformed or is not a real date.
    """
    if not isinstance(text, str):
        raise ValueError("Visit date must be text.")

    date_text = text.strip()
    parts = date_text.split('-')
    if (
        len(parts) != 3
        or len(parts[0]) != 4
        or len(parts[1]) != 2
        or len(parts[2]) != 2
        or not all(part.isdecimal() for part in parts)
    ):
        raise ValueError("Visit date must use the YYYY-MM-DD format.")

    year, month, day = (int(part) for part in parts)
    try:
        date(year, month, day)
    except ValueError as error:
        raise ValueError("Visit date must be a real calendar date.") from error

    return year, month, day

def main():
    print("==== Running format_visitor_name ====")
    value = input("Enter a visitor's full name (e.g. asha rao): ")
    print("Name on ticket:", format_visitor_name(value))

    print("\n==== Running parse_group_ages ====")
    value = input("Enter the ages in the group separated by spaces (e.g. 34 12 70): ")
    print("Group ages:", parse_group_ages(value))

    print("\n==== Running parse_visit_date ====")
    value = input("Enter the visit date as YYYY-MM-DD (e.g. 2026-11-05): ")
    print("Visit date (year, month, day):", parse_visit_date(value))

if __name__ == "__main__":
    main()
