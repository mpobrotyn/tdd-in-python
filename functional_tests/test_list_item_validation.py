from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class ItemValdiationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty lsit item.

        # The home page refreshes, and there is an error message saying
        # that lsit items cannot be blank

        # She tries again with some text for the item, which now works

        # Perversely she now decides t osubmit a second blank list item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
