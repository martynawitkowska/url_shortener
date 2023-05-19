from shortener.models import URL


def test_url_gui_representation():
    url = URL(url="https://www.beano.com/posts/funniest-useless-pointless-facts", short_url="abcdefg")

    assert str(url) == "https://www.beano.com/posts/fu -> abcdefg"
