from behave import given, when, then

@given('Open target main page')
def open_main(ctx):
    ctx.driver.get('https://www.target.com/')

@when('Search for {search_word}')
def search_for_word(ctx, search_word):
    ctx.app.header.search(search_word)

@when('I search for "{term}"')
def i_search_for(ctx, term):
    ctx.app.header.search(term)

@then('Verify search results are shown for {product}')
def verify_results(ctx, product):
    ctx.app.search_results_page.wait_loaded()

