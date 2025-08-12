import uuid

import allure
import pytest
from playwright.sync_api import Playwright, Page, expect

from config import Settings
from pages.main_page import MainPage


@pytest.fixture
def chromium_page(playwright: Playwright, settings: Settings) -> Page:
    expect.set_options(timeout=settings.expect_timeout)

    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(
        base_url=f"{settings.app_url}/",
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    yield page

    tracing_file = settings.tracing_dir.joinpath(f'{uuid.uuid4()}.zip')
    context.tracing.stop(path=tracing_file)
    browser.close()

    allure.attach.file(tracing_file, name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)


@pytest.fixture
def main_page(chromium_page: Page) -> MainPage:
    return MainPage(page=chromium_page)
