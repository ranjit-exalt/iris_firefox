# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):
    def __init__(self):
        BaseTest.__init__(self)
        self.meta = ' Edit a bookmark from the bookmarks menu'
        self.test_case_id = '165475'
        self.test_suite_id = '2525'
        self.locales = ['en-US']

    def run(self):
        library_button_pattern = NavBar.LIBRARY_MENU
        bookmarks_menu_option_pattern = LibraryMenu.BOOKMARKS_OPTION
        wikipedia_soap_pattern = LocalWeb.SOAP_WIKI_TEST_SITE
        wiki_logo_pattern = LocalWeb.SOAP_WIKI_SOAP_LABEL
        star_button_pattern = LocationBar.STAR_BUTTON_UNSTARRED
        edit_bookmark_name_before_pattern = Pattern('edit_bookmark_name.png')
        edit_bookmark_name_after_pattern = Pattern('edit_bookmark_name_modified.png')
        edit_bookmark_folder_before_pattern = Pattern('edit_bookmark_folder.png')
        edit_bookmark_folder_after_pattern = Pattern('edit_bookmark_folder_modified.png')
        edit_bookmark_tags_before_pattern = Pattern('tags_before.png')
        edit_bookmark_tags_after_pattern = Pattern('edit_bookmark_tags_modified.png')
        if not Settings.is_windows():
            edit_this_bookmark_pattern = Pattern('edit_this_bookmark.png')
        else:
            edit_this_bookmark_pattern = Bookmarks.StarDialog.EDIT_THIS_BOOKMARK

        if Settings.is_linux() or Settings.is_mac():
            edit_bookmark_folder_option = Pattern('bookmark_menu_folder_option.png')

        navigate(wikipedia_soap_pattern)

        wiki_logo_exists = exists(wiki_logo_pattern, DEFAULT_SITE_LOAD_TIMEOUT)
        assert_true(self, wiki_logo_exists, 'Website is properly loaded')

        star_button_exists = exists(star_button_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, star_button_exists, 'Star button exists')

        click(star_button_pattern)
        if Settings.is_linux():
            click(wiki_logo_pattern)

        library_button_exists = exists(library_button_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, library_button_exists, 'View history, saved bookmarks and more section exists')

        click(library_button_pattern)

        bookmarks_menu_option_exists = exists(bookmarks_menu_option_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, bookmarks_menu_option_exists, 'Bookmarks menu option exists')

        click(bookmarks_menu_option_pattern)

        edit_this_bookmark_exists = exists(edit_this_bookmark_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, edit_this_bookmark_exists, 'The Bookmarks menu is correctly displayed')

        click(edit_this_bookmark_pattern)

        if not Settings.is_mac():
            edit_this_bookmark_menu_exists = exists(edit_this_bookmark_pattern, DEFAULT_UI_DELAY_LONG)
            assert_true(self, edit_this_bookmark_menu_exists,
                        'Edit This Bookmark window is displayed under the star-shaped button from the URL bar')
        else:
            edit_bookmark_name_before_exists = exists(edit_bookmark_name_before_pattern, DEFAULT_UI_DELAY_LONG)
            assert_true(self, edit_bookmark_name_before_exists,
                        'Edit This Bookmark window is displayed under the star-shaped button from the URL bar')

        edit_bookmark_name_before_exists = exists(edit_bookmark_name_before_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, edit_bookmark_name_before_exists, 'Name field exists')

        edit_bookmark_folder_before_exists = exists(edit_bookmark_folder_before_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, edit_bookmark_folder_before_exists, 'Folder field exists')

        edit_bookmark_tags_before_exists = exists(edit_bookmark_tags_before_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, edit_bookmark_tags_before_exists, 'Tags field exists')

        paste('New Name')

        type(Key.TAB)

        click(edit_bookmark_folder_before_pattern)

        if Settings.is_linux() or Settings.is_mac():
            edit_bookmark_folder_after_exists = exists(edit_bookmark_folder_option, DEFAULT_UI_DELAY_LONG)
            assert_true(self, edit_bookmark_folder_after_exists, 'Needed option from folder field exists')
            click(edit_bookmark_folder_option)
        else:
            edit_bookmark_folder_after_exists = exists(edit_bookmark_folder_after_pattern, DEFAULT_UI_DELAY_LONG)
            assert_true(self, edit_bookmark_folder_after_exists, 'Needed option from folder field exists')
            click(edit_bookmark_folder_after_pattern)

        if not Settings.is_mac():
            [type(Key.TAB) for _ in range(2)]
        else:
            type(Key.TAB)

        paste('tags, test')

        type(Key.ENTER)

        library_button_exists = exists(library_button_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, library_button_exists, 'View history, saved bookmarks and more section exists')

        click(library_button_pattern)

        bookmarks_menu_option_exists = exists(bookmarks_menu_option_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, bookmarks_menu_option_exists, 'Bookmarks menu option exists')

        click(bookmarks_menu_option_pattern)

        edit_this_bookmark_exists = exists(edit_this_bookmark_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, edit_this_bookmark_exists, 'The Bookmarks menu is correctly displayed')

        click(edit_this_bookmark_pattern)

        if not Settings.is_mac():
            edit_this_bookmark_menu_exists = exists(edit_this_bookmark_pattern, DEFAULT_UI_DELAY_LONG)
            assert_true(self, edit_this_bookmark_menu_exists,
                        'Edit This Bookmark window is displayed under the star-shaped button from the URL bar')
        else:
            edit_bookmark_name_before_exists = exists(edit_bookmark_name_after_pattern, DEFAULT_UI_DELAY_LONG)
            assert_true(self, edit_bookmark_name_before_exists,
                        'Edit This Bookmark window is displayed under the star-shaped button from the URL bar')

        edit_bookmark_name_after_exists = exists(edit_bookmark_name_after_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, edit_bookmark_name_after_exists, 'Name field was correctly saved')

        edit_bookmark_folder_after_exists = exists(edit_bookmark_folder_after_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, edit_bookmark_folder_after_exists, 'Folder field was correctly saved')

        edit_bookmark_tags_after_exists = exists(edit_bookmark_tags_after_pattern, DEFAULT_UI_DELAY_LONG)
        assert_true(self, edit_bookmark_tags_after_exists, 'Tags field was correctly saved')
