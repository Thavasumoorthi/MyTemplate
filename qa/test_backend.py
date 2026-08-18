from appname import create_app


def test_home_page():
    app = create_app("appname.settings.TestConfig")
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200