from my_app.functions_view import form_racers
from test_my_app.conftest import racers_for_patch


def test_report_route(client):
    response = client.get("/report")
    response2 = client.get("/")

    assert response.status_code == 200
    assert response2.status_code == 200
    assert "Report" in response.data.decode("utf-8")
    assert "Report" in response2.data.decode("utf-8")


def test_drivers_default_route(client):
    response = client.get("/report/drivers")

    assert response.status_code == 200
    assert all(True if value in response.data.decode("utf-8") else False for value in form_racers().values()) is True


def test_drivers_desc_route(client):
    response = client.get("/report/drivers?order=desc")

    assert response.status_code == 200
    assert all(True if value in response.data.decode("utf-8") else False for value in form_racers().values()) is True


def test_drivers_asc_route(client):
    response = client.get("/report/drivers?order=asc")

    assert response.status_code == 200
    assert all(True if value in response.data.decode("utf-8") else False for value in form_racers().values()) is True


def test_drivers_single_driver(client):
    response = client.get("/report/drivers/driver_id=DRR")

    assert response.status_code == 200
    assert str(racers_for_patch[0]) in response.data.decode("utf-8")
