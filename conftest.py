import pytest
import time
from pathlib import Path

SCREENSHOTS_DIR=Path("screenshots")
SCREENSHOTS_DIR.mkdir(exist_ok=True)

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report=outcome.get_result()

    if report.when == "call" and report.failed:
        driver=None
        if hasattr(item,"funcargs"):
            driver=item.funcargs.get("login_driver") or item.funcargs.get("drivertest")

        if driver:
            timestamp=time.strftime("%Y%m%d_%H%M%S")
            screenshot_name=f"{item.name}_{timestamp}.png"
            screenshot_path=SCREENSHOTS_DIR / screenshot_name
            driver.save_screenshot(str(screenshot_path))
            print(f"失败截图已保存：{screenshot_path}")
