from playwright.sync_api import Page, expect


def test_home_page_ui(page: Page):
    page.goto("http://127.0.0.1:5000/")

    expect(page).to_have_title("MyTemplate")
    expect(page.get_by_text("MyTemplate").first).to_be_visible()