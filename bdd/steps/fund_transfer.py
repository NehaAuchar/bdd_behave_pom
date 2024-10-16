import time
from behave import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given("user has valid credentials to login")
def step_login(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("https://parabank.parasoft.com/parabank/openaccount.htm")
    # Find and enter the username
    context.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("demo_user")
    # Find and enter the password
    context.wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("Password")
    # Find and click on submit button
    context.driver.find_element(By.XPATH, "//input[@value='Log In']").click()


@when("user clicks on Transfer Funds")
def step_transfer_find_navigation(context):
    """
    :type context: behave.runner.Context
    """
    # Find and click on Fun Transfer link
    context.driver.find_element(By.XPATH, "//a[@href='transfer.htm']").click()


@when('user selects the "{FromAccount}" as "From" account')
def step_select_from_account(context, FromAccount):
    """
    :type context: behave.runner.Context
    :type FromAccount: str
    """
    # Find and select the account "From Account" dropdown
    from_account_dropdown = context.wait.until(EC.presence_of_element_located((By.ID, "fromAccountId")))
    time.sleep(2)
    for option in from_account_dropdown.find_elements(By.TAG_NAME, 'option'):
        if FromAccount.strip().lower() in option.text.strip().lower():
            option.click()
            break


@step('user selects the "{ToAccount}" as "To" account')
def step_select_to_account(context, ToAccount):
    """
    :type context: behave.runner.Context
    :type ToAccount: str
    """
    # Find and select the account "To Account" dropdown
    to_account_dropdown = context.wait.until(EC.presence_of_element_located((By.ID, "toAccountId")))
    time.sleep(2)
    for option in to_account_dropdown.find_elements(By.TAG_NAME, 'option'):
        if ToAccount.strip().lower() in option.text.strip().lower():
            option.click()
            break


@step('user enters the amount to be transferred as "{Amount}"')
def step_enter_amount(context, Amount):
    """
    :type context: behave.runner.Context
    :type Amount: str
    """
    # Find and enter the amount to be transferred
    context.wait.until(EC.presence_of_element_located((By.ID, "amount"))).send_keys(Amount)


@step("user clicks on confirmation button")
def step_click_confirmation(context):
    """
    :type context: behave.runner.Context
    """
    # Find and click on confirm button
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Transfer']"))).click()


@then('user should see the error message as "{Message}"')
def step_verify_message(context, Message):
    """
    :type context: behave.runner.Context
    :type Message: str
    """
    time.sleep(1)
    # Verify the fund transfer message
    verification_message = context.wait.until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Transfer Complete!')]"))).text
    assert Message in verification_message


@step("user clicks on Account Overview to check account balance")
def step_navigate_account_overview(context):
    """
    :type context: behave.runner.Context
    """
    # Click and navigate to Account Overview page
    context.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Accounts Overview"))).click()


@step('the checking account balance should be "{FromBalance} for "{FromAccount}"')
def step_verify_checking_balance(context, FromBalance, FromAccount):
    """
    :type context: behave.runner.Context
    :type CheckingBalance: str
    """
    # Get the "from account" balance and verifying it
    balance = context.wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//td[contains(a,'" + FromAccount + "')]/following-sibling::td[1]"))).text
    assert balance == FromBalance.strip('"'), f"Assertion failed: balance '{balance}' != FromBalance '{FromBalance}'"



@step('the savings account balance should "{ToBalance} for "{ToAccount}"')
def step_verify_saving_balance(context, ToBalance, ToAccount):
    """
    :type context: behave.runner.Context
    :type SavingBalance: str
    """
    # Get the "to account" balance and verifying it
    balance = context.wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//td[contains(a,'" + ToAccount + "')]/following-sibling::td[1]"))).text
    assert balance == ToBalance.strip().replace('"', ''), f"Assertion failed: balance '{balance}' != ToBalance '{ToBalance}'"


