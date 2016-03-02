import mock

from kivy.base import EventLoopBase

def pytest_runtest_setup(item):
    item.mock_patches = [
        mock.patch('kivy.uix.widget.Builder'),
        mock.patch.object(EventLoopBase, 'ensure_window', lambda x: None),
    ]
    for patch in item.mock_patches:
        patch.start()


def pytest_runtest_teardown(item, nextitem):
    for patch in item.mock_patches:
            patch.stop()
