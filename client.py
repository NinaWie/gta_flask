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


# TODO: test task 3
def test_project_to_crs():
    json_data = (4326, 47.324, 8.342)
    print("input:", json_data, "convert to le crs")
    r = requests.post(host_link + "project_to_crs", json=json_data)
    print(r.json())

if __name__ == "__main__":
    print("test using post:")
    test_using_post()
    print("test project coords:")
    test_project_coords()
    print("test project to crs:")
    test_project_to_crs()
