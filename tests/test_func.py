from crypto.crypto import encrypt, decrypt, validate, crack
import pytest

def test_validate_reurns_flase_for_fake_word():
    x = "wargarble"
    actual = validate(x)
    expected = False
    assert actual == expected

def test_validate_reurns_true_for_real_word():
    x = "authentic"
    actual = validate(x)
    expected = True
    assert actual == expected

def test_encrypt():
    actual = encrypt("this is a test", 6)
    expected = "znoy oy g zkyz"
    assert actual == expected

def test_wrapping_if_number_over_26():
    x = encrypt("this is a test", 27)
    y = encrypt("this is a test", 1)
    actual = x == y
    expected = True
    assert actual == expected

def test_encryption_should_allow_nonalpha_characters_but_ignore_them():
    actual = encrypt("wait! what's, going on here?", 4)
    expected = "aemx! alex'w, ksmrk sr livi?"
    assert actual == expected

def test_decryption_should_allow_nonalpha_characters_but_ignore_them():
    actual = decrypt("aemx! alex'w, ksmrk sr livi?", 4)
    expected = "wait! what's, going on here?"
    assert actual == expected

def test_encrypt_and_decrypt_work_with_caps():
    x = encrypt("Mississing", 14)
    actual = decrypt(x, 14)
    expected = "Mississing"
    assert actual == expected

def test_decrypt():
    actual = decrypt("znoy oy g zkyz", 6)
    expected = "this is a test"
    assert actual == expected

def test_crack():
    x = "Wh kog hvs psgh ct hwasg, wh kog hvs kcfgh ct hwasg."
    actual = crack(x)
    expected = "It was the best of times, it was the worst of times.", 14
    assert actual == expected