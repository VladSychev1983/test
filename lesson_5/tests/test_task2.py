import pytest
import requests

class TestYandexDisk:
    def setup_method(self):
        self.headers = {
            'Authorization': 'OAuth api_key_here'
        }

    @pytest.mark.parametrize(
        'key,value,statuscode',
        (
                ['pat', 'Image', 400],
                ['path', 'Image', 201],
                ['path', 'Image', 409],
        )
    )
    def test_create_folder(self, key: list[str | int], value: list[str | int], statuscode: list[str | int]):
        params = {key: value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == statuscode