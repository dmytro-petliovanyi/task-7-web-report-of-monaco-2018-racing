from unittest.mock import patch

from my_app.functions_view import form_racers, racer_to_str
from test_my_app.conftest import racers_for_patch


@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("os.environ", return_value="some_text")
def test_racer_to_str_works_as_expected(patch_environ,
                                        patch_groper):
    result = racer_to_str("DRR")
    patch_groper.assert_called()
    assert result == "Daniel Ricciardo              | RED BULL RACING TAG HEUER     | 2:47.987"


@patch("my_app.functions_view.sort_racers", return_value=sorted(racers_for_patch))
@patch("my_app.functions_view.groper", return_value=racers_for_patch)
@patch("os.environ", return_value="some_text")
def test_form_racers_works_as_expected(patch_environ,
                                       patch_groper,
                                       patch_get_racer):
    result = form_racers()
    patch_get_racer.assert_called()
    patch_groper.assert_called()
    assert result == ['Sebastian Vettel              | FERRARI                       | 1:04.415',
                      'Daniel Ricciardo              | RED BULL RACING TAG HEUER     | 2:47.987',
                      'Lewis Hamilton                | MERCEDES                      | 6:47.54']
