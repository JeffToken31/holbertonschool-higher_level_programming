from jinja2 import Environment, select_autoescape

def get_value(attendee, key):
    return attendee.get(key) if attendee.get(key) not in [None, ""] else "N/A"

def generate_invitations(template, attendees):
    """
    This function genere an invitation for each attendee
    """
    env = Environment(
    autoescape=select_autoescape(enabled_extensions=('html', 'htm', 'xml'), default_for_string=True, default=True,)
)
    try:
        if not isinstance(template, str):
            raise TypeError('template must be a string')
        if not isinstance(attendees, list):
            raise TypeError('template must be a list')   
        for attendee in attendees:
            if not isinstance(attendee, dict):
                raise TypeError('attendees must be a dict')
    except TypeError as e:
        print({"error": {e}})
        return
    try:
        if not template:
            raise ValueError('template is empty')
        if not attendees:
            raise ValueError('list is empty')
    except ValueError as e:
        print({"error": {e}})
        return
    
    my_template = env.from_string(template)

    for idx, attendee in enumerate(attendees, start=1):
        
        context = {
            "name": get_value(attendee, "name"),
            "event_title": get_value(attendee, "event_title"),
            "event_date": get_value(attendee, "event_date"),
            "event_location": get_value(attendee, "event_location")
        }
        text = my_template.render(context)
        
        filename = "output_{}.txt".format(idx)

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(text)
        except Exception as e:
            print({"error": {e}})
