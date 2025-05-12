import logging
import random
import string

import pytest
from disposable_email_domains import blocklist

from module.mail import Mail


@pytest.fixture(scope="class")
def mail_client(default_setup):
    yield Mail(default_setup.config.disify_domain)


def generate_invalid_email_format():
    username = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    special_characters = ["..", "#", "$", "%", "@", "&", "^", "{", "}"]
    domain = "example.com"

    chars = list(domain)
    num_insertions = random.randint(1, 3)

    for _ in range(num_insertions):
        insert_pos = random.randint(0, len(chars))
        special_char = random.choice(special_characters)
        chars.insert(insert_pos, special_char)

    result = "".join(chars)

    return f"{username}@{result}"


def generate_valid_email(is_disposable=False):
    username = "".join(random.choices(string.ascii_letters + string.digits, k=8))

    disposable_domains = list(blocklist)
    real_domains = [
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "aol.com",
        "outlook.com",
        "icloud.com",
        "mail.com",
        "protonmail.com",
        "zoho.com",
        "gmx.com",
    ]

    if is_disposable:
        return f"{username}@{random.choice(disposable_domains)}"
    else:
        return f"{username}@{random.choice(real_domains)}"


class TestMail:
    @pytest.mark.parametrize(
        "email", [generate_valid_email(True), generate_valid_email(False)]
    )
    def test_valid_mail_format(self, mail_client, email):
        logging.info(f"Verify the email {email}...")
        res = mail_client.verify_email(email=email)

        assert res.status_code == 200, res.text
        assert res.json()["format"] is True, "expected format is True. But got False"

    @pytest.mark.parametrize(
        "email",
        [(lambda: generate_valid_email(is_disposable=True))() for _ in range(3)],
    )
    def test_disposable_mail(self, mail_client, email):
        logging.info(f"Verify the email {email}...")
        res = mail_client.verify_email(email=email)

        assert res.status_code == 200, res.text
        assert res.json()["format"] is True, "expected format is True. But got False"
        assert (
            res.json()["disposable"] is True
        ), "expected disposable is True. But got False"

    @pytest.mark.parametrize(
        "email",
        [(lambda: generate_valid_email(is_disposable=False))() for _ in range(3)],
    )
    def test_non_disposable_mail(self, mail_client, email):
        logging.info(f"Verify the email {email}...")
        res = mail_client.verify_email(email=email)

        assert res.status_code == 200, res.text
        assert res.json()["format"] is True, "expected format is True. But got False"
        assert (
            res.json()["disposable"] is False
        ), "expected disposable is False. But got True"

    @pytest.mark.parametrize(
        "email", [(lambda: generate_invalid_email_format())() for _ in range(3)]
    )
    def test_invalid_special_characters(self, mail_client, email):
        res = mail_client.verify_email(email=email)

        assert res.status_code == 200, res.text
        assert res.json()["format"] is False, res.json()["format"]
