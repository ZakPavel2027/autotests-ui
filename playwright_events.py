from playwright.sync_api import sync_playwright, Request, Response
from http import HTTPStatus

def log_req(request: Request):
    print(f"Request: {request.url}")

def log_resp(response: Response):
    status = response.status
    text = HTTPStatus(status).phrase
    print(f'Response: {response.url} -> {status} {text}')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.on("request", log_req)
    page.on("response", log_resp)

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    page.wait_for_timeout(3000)