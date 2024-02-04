from page_objects.registration_page import RegistrationPage


def test_register_new_user(browser, base_url):
    registration = RegistrationPage(browser, base_url)
    registration.open_registration_page()
    registration.input_first_name("David")
    registration.input_last_name("Smith")
    registration.input_email("david_smith@testik.com")
    registration.input_password("password")
    registration.confirm_privacy_policy()
    registration.select_continue_button()
    registration.confirm_registration()
