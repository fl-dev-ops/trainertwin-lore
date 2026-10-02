from pipeline.index import accept, demo, has_list, plan, FACETS


def test_index_rules():
    demo()
    text = "After 12th, do this.\n\n1. Study engineering\n2. Aim for a strong college\n"
    assert has_list(text)
    mode, extra = plan("Just a short post about rent.")
    assert mode == "whole" and "one item" in extra
    kept = accept(
        ["hello from the post itself"],
        {"items": [{"title": "Rent", "tags": [{"facet": "nope", "label": "x"}], "span": {"start_line": 1, "end_line": 1}}]},
    )
    assert kept[0]["tags"] == []
    assert kept[0]["quote"] == "hello from the post itself"
    # valid facets accepted
    kept2 = accept(
        ["hello from the post itself"],
        {"items": [{"title": "Rent", "tags": [{"facet": "topic", "label": "rent pricing"}], "span": {"start_line": 1, "end_line": 1}}]},
    )
    assert kept2[0]["tags"] == [{"facet": "topic", "label": "rent pricing"}]
    # all valid facets
    assert set(FACETS) == {"topic", "situation", "activity"}
