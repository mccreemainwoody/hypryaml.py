from hypryaml.utils.hyprctl import run_hyprctl_keyword


border_keyword = "general:col.active_border"

def test_keyword_borders_to_red():
    borders_color = "rgb(ff0000) rgb(ffff00) 45rad"
    result = run_hyprctl_keyword(border_keyword, borders_color)

    assert result.exit_code == 0
    assert result.stdout == "ok"


def test_keyword_borders_to_blue():
    borders_color = "rgb(33ccff) rgb(00ff99) 45rad"
    result = run_hyprctl_keyword(border_keyword, borders_color)

    assert result.exit_code == 0
    assert result.stdout == "ok"
