import requests

host_link = "http://localhost:8989/"


def test_using_post():
    json_data = {"username": "Me", "password": 1234}
    r = requests.post(host_link + "using_post", json=json_data)
    # print status - should be 200
    print(r.status_code)
    # print output data
    print(r.json())


def test_project_coords():
    json_data = [47.324, 8.342]
    r = requests.post(host_link + "project_coords", json=json_data)
    print(r.json())
# TODO: task 3
def test_project_any_coords():
    json_data_3 = [[47.324, 8.342],[47.37668,8.54862]]
    # Dieser Abschnitt hier simuliert den Browser Inputfläche, deshalb hier den Browserinput definieren
    r_3 = requests.post(host_link + "project_any_coords?crs=2056", json=json_data_3)
    print(r_3.json())

# TODO: test task 3

if __name__ == "__main__":
    # Welche der Funktionen ausgeführt wird von client.py
    test_project_any_coords()
