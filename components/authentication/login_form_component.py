from components.base_component import BaseComponent
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.email = Input(page, 'login-form-email-input', 'Email')
        self.password = Input(page, 'login-form-password-input', 'Password')

    def fill(self, email: str, password: str):
        self.email.fill(email)
        self.email.check_have_value(email)

        self.password.fill(password)
        self.password.check_have_value(password)

    def check_visible(self, email: str, password: str):
        self.email.check_visible()
        self.email.check_have_value(email)

        self.password.check_visible()
        self.password.check_have_value(password)
