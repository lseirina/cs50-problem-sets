from twttr import shorten

def test_str():

    assert shorten("hello") == "hll"
    assert shorten("goodbye") == "gdby"
    assert shorten("HELLO") == "HLL"
    assert shorten("lama124") == "lm124"
    assert shorten ("app,.l") == "pp,.l"