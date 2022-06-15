from django_dynamic_shields.data import ShieldsData


class TestCreateShieldsData:
    def test__create_ok_data(self):
        """Simplest normal case"""
        sd: ShieldsData = ShieldsData(label="label", message="message")
        sd_dict: dict = sd.dict
        assert sd_dict["label"] == "label"
        assert "namedLogo" not in sd_dict
