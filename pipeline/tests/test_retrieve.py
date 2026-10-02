from unittest.mock import MagicMock
from pipeline.retrieve import extract_keywords, score_and_select_items, slice_verbatim_text, route_query_with_jev


def test_extract_keywords():
    tokens = extract_keywords("How does Olga handle a client who says 'I will wait'?")
    assert "client" in tokens
    assert "wait" in tokens
    assert "how" not in tokens
    assert "who" not in tokens


def test_score_and_select_items():
    items = [
        {
            "item_id": "1",
            "path": "video1.md",
            "title": "Handling Stalling Clients",
            "quote": "when client stalls",
            "tags": [{"facet": "situation", "label": "client wants to wait and see"}],
        },
        {
            "item_id": "2",
            "path": "video1.md",
            "title": "Another clip from same video",
            "quote": "waiting for prices to drop",
            "tags": [{"facet": "situation", "label": "client wants to wait and see"}],
        },
        {
            "item_id": "3",
            "path": "video1.md",
            "title": "Third clip from same video",
            "quote": "waiting again",
            "tags": [{"facet": "situation", "label": "client wants to wait and see"}],
        },
        {
            "item_id": "4",
            "path": "video2.md",
            "title": "Reframing Investor Waiting Mindset",
            "quote": "market drop discussion",
            "tags": [{"facet": "situation", "label": "client stalling"}],
        },
    ]

    aliases = ["client wants to wait and see", "client stalling"]
    query = "Client waiting for market drop"

    selected = score_and_select_items(items, query, aliases, max_clips=3, max_per_file=2)
    # Must enforce max 2 clips from video1.md
    video1_count = sum(1 for it in selected if it["path"] == "video1.md")
    assert video1_count <= 2
    assert len(selected) == 3


def test_route_query_with_jev():
    mock_jev = MagicMock()
    mock_jev.decide.return_value = {
        "matched_concept": {
            "type": "choice",
            "choice": "client-wants-to-wait-and-see",
            "confidence": 0.95,
        }
    }

    taxonomy = {
        "situation": {
            "client-wants-to-wait-and-see": {
                "preferred": "client wants to wait and see",
                "aliases": ["client stalling", "waiting for bottom"],
            }
        }
    }

    cid, aliases, conf = route_query_with_jev("Client says they will wait", taxonomy, mock_jev)
    assert cid == "client-wants-to-wait-and-see"
    assert "client stalling" in aliases
    assert conf == 0.95
