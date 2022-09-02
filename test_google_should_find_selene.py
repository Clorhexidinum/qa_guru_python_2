from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.mark.usefixtures('open_browser')
def test_search_selene_in_google():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


@pytest.mark.usefixtures('open_browser')
def test_wrong_search_selene_in_google():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('Ответы других учеников'))

def test_conflict_merge():
    print("wow!")