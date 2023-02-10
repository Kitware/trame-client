import pytest
from seleniumbase import SB


@pytest.mark.parametrize(
    "server_path",
    ["examples/vue2/dynamic_template.py", "examples/vue3/dynamic_template.py"],
)
def test_dynamic_template(server, baseline_image):
    with SB() as sb:
        url = f"http://localhost:{server.port}/"
        sb.open(url)
        sb.check_window(name="init", level=3)
        sb.assert_exact_text("Static text 2", ".staticDiv")
        sb.assert_exact_text("count = 2", ".countDiv")
        sb.assert_exact_text("tts = 0", ".ttsDiv")
        assert server.get("count") == 2
        sb.click(".plusBtn")
        sb.click(".plusBtn")
        sb.assert_exact_text("Static text 2", ".staticDiv")
        assert server.get("count") == 4
        sb.assert_exact_text("count = 4", ".countDiv")
        sb.assert_exact_text("tts = 0", ".ttsDiv")
        sb.click(".updateBtn")
        sb.click(".updateBtn")
        sb.assert_exact_text("Static text 6", ".staticDiv")
        assert server.get("count") == 6
        sb.assert_exact_text("count = 6", ".countDiv")
        sb.assert_exact_text("tts = 2", ".ttsDiv")
        sb.check_window(name="final", level=3)
