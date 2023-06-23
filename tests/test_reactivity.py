import pytest
from seleniumbase import SB


@pytest.mark.parametrize("server_path", ["examples/test/reactivity.py"])
def test_reactivity(server, baseline_image):
    with SB() as sb:
        url = f"http://127.0.0.1:{server.port}/"
        sb.open(url)
        sb.check_window(name="simple_count_1", level=3)
        sb.assert_exact_text("1", ".countValue")
        assert server.get("count") == 1
        sb.click(".plusButton")
        sb.assert_exact_text("2", ".countValue")
        assert server.get("count") == 2
        sb.click(".plusButton")
        sb.click(".plusButton")
        sb.assert_exact_text("4", ".countValue")
        assert server.get("count") == 4
        sb.click(".plusButton")
        sb.assert_exact_text("5", ".countValue")
        assert server.get("count") == 5
        sb.check_window(name="simple_count_5", level=3)
