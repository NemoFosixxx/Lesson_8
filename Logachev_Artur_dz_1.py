import re
def email_parse(email_address):
    parsed = re.findall(r"([^@&]+)@([\w_-][\w_\.-]*\.[\w_-]{2,})$", email_address)
    if not parsed:
        raise ValueError(f"wrong email: {email_address}")
    print(dict(zip(["username", "domain"], parsed[0])))

email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')