from collections import Counter
from unittest.mock import MagicMock
from pipeline.normalize import cluster_facet, slugify, tokenize


def test_slugify():
    assert slugify("Client Panic Over Market") == "client-panic-over-market"
    assert slugify("   sales-strategy!  ") == "sales-strategy"
    assert slugify("###") == "unnamed"


def test_tokenize():
    tokens = tokenize("Clients panicking in the market")
    assert "clients" in tokens
    assert "panicking" in tokens
    assert "market" in tokens
    assert "the" not in tokens
    assert "in" not in tokens


def test_cluster_facet_exact_case_folding():
    mock_jev = MagicMock()
    # No Jev calls should be needed for exact case differences
    counts = Counter({
        "Sales Coaching": 5,
        "sales coaching": 3,
        "SALES COACHING": 2,
    })
    clusters = cluster_facet("activity", counts, mock_jev)
    assert len(clusters) == 1
    assert clusters[0]["preferred"] == "Sales Coaching"
    assert clusters[0]["count"] == 10
    mock_jev.decide.assert_not_called()


def test_cluster_facet_with_jev_mock():
    mock_jev = MagicMock()
    mock_jev.decide.return_value = {"p_0": {"type": "noul", "noul": 0.95}}

    counts = Counter({
        "lead stops responding": 8,
        "getting ghosted by clients": 2,
    })

    clusters = cluster_facet("situation", counts, mock_jev, threshold=0.70)
    assert len(clusters) == 1
    assert clusters[0]["preferred"] == "lead stops responding"
    assert "getting ghosted by clients" in clusters[0]["aliases"]
    assert clusters[0]["count"] == 10
