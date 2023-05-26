from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("euacertei", 1) == "e_ietrecau"
    assert encrypt_message("euacertei", 10) == "ietrecaue"
    with pytest.raises(TypeError):
        encrypt_message(1, "euacertei")
