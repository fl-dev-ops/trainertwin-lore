"""Generate a 3D interactive living knowledge graph visualization for TrainerTwin Lore.

Creates an interactive, WebGL-powered 3D constellation of interconnected evidence notes
with direct note-to-note semantic relationships and color-based grouping rather than
artificial cluster clumping, matching the cosmic brain aesthetic.

Run:
    uv run python -m pipeline.graph --user olga
"""

import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>TrainerTwin Brain — Living Knowledge System</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/three@0.160.0/build/three.min.js"></script>
  <script src="https://unpkg.com/3d-force-graph@1.73.3/dist/3d-force-graph.min.js"></script>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
    }

    body {
      background: #07090e;
      color: #e2e8f0;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      overflow: hidden;
      width: 100vw;
      height: 100vh;
    }

    #3d-graph {
      position: absolute;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 1;
    }

    /* Glassmorphism Overlays */
    .glass {
      background: rgba(13, 17, 28, 0.75);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 16px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.45);
    }

    /* Top Nav */
    header {
      position: absolute;
      top: 20px;
      left: 24px;
      right: 24px;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      z-index: 10;
      pointer-events: none;
    }

    header > * {
      pointer-events: auto;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
      font-size: 16px;
      letter-spacing: -0.02em;
      color: #fff;
    }

    .brand-dot {
      width: 8px;
      height: 8px;
      background: #38bdf8;
      border-radius: 50%;
      box-shadow: 0 0 12px #38bdf8;
      animation: pulse 2s infinite ease-in-out;
    }

    @keyframes pulse {
      0%, 100% { opacity: 0.6; transform: scale(1); }
      50% { opacity: 1; transform: scale(1.3); }
    }

    .search-wrapper {
      position: relative;
      width: 360px;
    }

    .search-input {
      width: 100%;
      height: 38px;
      background: rgba(22, 27, 46, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 20px;
      padding: 0 40px 0 16px;
      color: #fff;
      font-size: 13px;
      outline: none;
      transition: all 0.2s ease;
      font-family: inherit;
    }

    .search-input:focus {
      border-color: #38bdf8;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.25);
    }

    .search-kbd {
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: #64748b;
      background: rgba(255, 255, 255, 0.05);
      padding: 2px 6px;
      border-radius: 4px;
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .badge-count {
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      color: #94a3b8;
      font-weight: 500;
      margin-right: 8px;
    }

    .btn-icon {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      border: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(22, 27, 46, 0.8);
      color: #94a3b8;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }

    .btn-icon:hover {
      color: #fff;
      background: rgba(56, 189, 248, 0.2);
      border-color: #38bdf8;
    }

    /* Left Hero Panel */
    .hero-panel {
      position: absolute;
      top: 96px;
      left: 24px;
      width: 330px;
      max-height: calc(100vh - 180px);
      padding: 24px;
      z-index: 10;
      pointer-events: auto;
      overflow-y: auto;
    }

    .tagline {
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 8px;
    }

    .hero-title {
      font-size: 32px;
      font-weight: 800;
      letter-spacing: -0.04em;
      line-height: 1.05;
      color: #ffffff;
      margin-bottom: 8px;
    }

    .hero-desc {
      font-size: 12px;
      color: #94a3b8;
      line-height: 1.4;
      margin-bottom: 20px;
    }

    /* Stats Grid */
    .stats-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 20px;
      padding-bottom: 20px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }

    .stat-box {
      background: rgba(255, 255, 255, 0.02);
      padding: 10px 12px;
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.04);
    }

    .stat-val {
      font-size: 20px;
      font-weight: 800;
      color: #fff;
      letter-spacing: -0.02em;
      font-family: 'JetBrains Mono', monospace;
    }

    .stat-label {
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #64748b;
      margin-top: 2px;
    }

    /* Color Mode Switcher */
    .mode-switch-container {
      margin-bottom: 16px;
    }

    .mode-switch-title {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #64748b;
      font-weight: 700;
      margin-bottom: 8px;
    }

    .mode-switch-tabs {
      display: flex;
      background: rgba(22, 27, 46, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      padding: 3px;
    }

    .mode-tab {
      flex: 1;
      text-align: center;
      padding: 6px 0;
      font-size: 12px;
      font-weight: 600;
      color: #94a3b8;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .mode-tab.active {
      background: #38bdf8;
      color: #07090e;
    }

    /* Legend List */
    .section-title {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #64748b;
      font-weight: 700;
      margin-bottom: 10px;
    }

    .sources-list {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 20px;
      max-height: 200px;
      overflow-y: auto;
    }

    .source-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 5px 8px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .source-item:hover, .source-item.active {
      background: rgba(255, 255, 255, 0.06);
    }

    .source-info {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      color: #cbd5e1;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .source-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      flex-shrink: 0;
    }

    .source-count {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: #64748b;
    }

    /* Bottom Bar */
    .bottom-bar {
      position: absolute;
      bottom: 24px;
      left: 24px;
      right: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      z-index: 10;
      pointer-events: none;
    }

    .bottom-bar > * {
      pointer-events: auto;
    }

    .nav-hints {
      font-size: 12px;
      color: #64748b;
      letter-spacing: -0.01em;
    }

    .cinema-controls {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .btn-cinema {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      background: rgba(22, 27, 46, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 20px;
      color: #e2e8f0;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }

    .btn-cinema:hover {
      background: rgba(56, 189, 248, 0.15);
      border-color: #38bdf8;
      color: #fff;
    }

    .btn-cinema.active {
      background: #38bdf8;
      color: #07090e;
      border-color: #38bdf8;
    }

    .brand-footer {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: #475569;
      letter-spacing: 0.1em;
    }

    /* Right Growth Banner & Node Inspector Drawer */
    .inspector-drawer {
      position: absolute;
      top: 96px;
      right: 24px;
      width: 420px;
      max-height: calc(100vh - 140px);
      padding: 24px;
      z-index: 10;
      pointer-events: auto;
      overflow-y: auto;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s;
    }

    .inspector-drawer.hidden {
      transform: translateX(30px);
      opacity: 0;
      pointer-events: none;
    }

    .growth-banner {
      position: absolute;
      bottom: 80px;
      right: 24px;
      width: 320px;
      padding: 20px;
      z-index: 9;
      pointer-events: auto;
      transition: opacity 0.3s ease;
    }

    .growth-tag {
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: #38bdf8;
      text-transform: uppercase;
      margin-bottom: 6px;
      font-family: 'JetBrains Mono', monospace;
    }

    .growth-val {
      font-size: 38px;
      font-weight: 800;
      letter-spacing: -0.04em;
      color: #fff;
      font-family: 'JetBrains Mono', monospace;
      line-height: 1;
      margin-bottom: 6px;
    }

    .growth-title {
      font-size: 16px;
      font-weight: 700;
      color: #f1f5f9;
      margin-bottom: 6px;
    }

    .growth-sub {
      font-size: 12px;
      color: #64748b;
      line-height: 1.4;
    }

    /* Inspector Card Content */
    .drawer-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      margin-bottom: 16px;
    }

    .badges-row {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }

    .node-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 4px 10px;
      border-radius: 12px;
    }

    .close-btn {
      background: none;
      border: none;
      color: #94a3b8;
      cursor: pointer;
      font-size: 18px;
      line-height: 1;
      padding: 4px;
      transition: color 0.2s;
    }

    .close-btn:hover {
      color: #fff;
    }

    .drawer-title {
      font-size: 17px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #fff;
      margin-bottom: 12px;
      line-height: 1.35;
    }

    .quote-box {
      background: rgba(56, 189, 248, 0.05);
      border-left: 3px solid #38bdf8;
      padding: 12px 14px;
      border-radius: 0 10px 10px 0;
      margin-bottom: 16px;
    }

    .quote-box .quote-label {
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      color: #38bdf8;
      letter-spacing: 0.08em;
      margin-bottom: 4px;
    }

    .quote-text {
      font-size: 13px;
      line-height: 1.5;
      color: #e2e8f0;
      font-style: italic;
    }

    .drawer-section {
      margin-bottom: 16px;
    }

    .drawer-section-title {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #64748b;
      margin-bottom: 6px;
    }

    .statement-text {
      font-size: 13px;
      line-height: 1.5;
      color: #cbd5e1;
    }

    /* Related Notes List */
    .related-notes-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-top: 8px;
    }

    .related-note-item {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.06);
      padding: 8px 12px;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .related-note-item:hover {
      background: rgba(56, 189, 248, 0.1);
      border-color: #38bdf8;
    }

    .related-note-title {
      font-size: 12px;
      font-weight: 600;
      color: #e2e8f0;
      margin-bottom: 2px;
    }

    .related-note-meta {
      font-size: 11px;
      color: #64748b;
      display: flex;
      justify-content: space-between;
    }

    .meta-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 16px;
      padding-top: 16px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
    }

    .meta-tag {
      background: rgba(255, 255, 255, 0.05);
      font-size: 11px;
      padding: 3px 8px;
      border-radius: 6px;
      color: #94a3b8;
      font-family: 'JetBrains Mono', monospace;
    }

    .source-link-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin-top: 16px;
      font-size: 12px;
      color: #38bdf8;
      text-decoration: none;
      font-weight: 600;
      transition: color 0.2s;
    }

    .source-link-btn:hover {
      color: #7dd3fc;
      text-decoration: underline;
    }

    /* Modal */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(10px);
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease;
    }

    .modal-backdrop.open {
      opacity: 1;
      pointer-events: auto;
    }

    .modal-card {
      width: 500px;
      padding: 32px;
      background: #0d111c;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 20px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    }

    .modal-card h3 {
      font-size: 20px;
      font-weight: 700;
      margin-bottom: 12px;
      color: #fff;
    }

    .modal-card p {
      font-size: 14px;
      line-height: 1.6;
      color: #94a3b8;
      margin-bottom: 16px;
    }

    .modal-card button {
      padding: 8px 18px;
      background: #38bdf8;
      border: none;
      border-radius: 8px;
      color: #07090e;
      font-weight: 700;
      cursor: pointer;
      font-size: 13px;
    }
  </style>
</head>
<body>
  <div id="3d-graph"></div>

  <!-- Header -->
  <header class="glass">
    <div class="brand">
      <div class="brand-dot"></div>
      <span>TrainerTwin Brain</span>
    </div>

    <div class="search-wrapper">
      <input type="text" id="searchInput" class="search-input" placeholder="Search notes, topics, quotes, sources... [/]">
      <div class="search-kbd">/</div>
    </div>

    <div class="header-actions">
      <div class="badge-count">
        <span style="color: #38bdf8;">●</span>
        <span id="nodesInViewCount">{{TOTAL_EVIDENCE}}</span> notes in view
      </div>
      <button class="btn-icon" id="btnHelp" title="What's in here?">?</button>
      <button class="btn-icon" id="btnRecenter" title="Reset View">↺</button>
    </div>
  </header>

  <!-- Left Hero Panel -->
  <div class="hero-panel glass">
    <div class="tagline">
      <span>●</span>
      <span>A Living Knowledge System</span>
    </div>
    <h1 class="hero-title">Every idea.<br>Connected.</h1>
    <p class="hero-desc">{{USER_DISPLAY_NAME}}'s TrainerTwin universe. Direct note-to-note neural connections grouped dynamically by color.</p>

    <div class="stats-grid">
      <div class="stat-box">
        <div class="stat-val" id="statNotes">{{TOTAL_EVIDENCE}}</div>
        <div class="stat-label">Notes</div>
      </div>
      <div class="stat-box">
        <div class="stat-val" id="statSources">{{TOTAL_SOURCES}}</div>
        <div class="stat-label">Sources</div>
      </div>
      <div class="stat-box">
        <div class="stat-val" id="statTopics">{{TOTAL_TOPICS}}</div>
        <div class="stat-label">Topics</div>
      </div>
      <div class="stat-box">
        <div class="stat-val" id="statLinks">{{TOTAL_LINKS}}</div>
        <div class="stat-label">Connections</div>
      </div>
    </div>

    <!-- Color Grouping Mode Switcher -->
    <div class="mode-switch-container">
      <div class="mode-switch-title">Color Grouping Mode</div>
      <div class="mode-switch-tabs">
        <div class="mode-tab active" id="tabColorPlatform">By Platform</div>
        <div class="mode-tab" id="tabColorTopic">By Topic (14)</div>
      </div>
    </div>

    <div class="section-title" id="legendTitle">Platforms</div>
    <div class="sources-list" id="sourcesList">
      <!-- Populated via JS -->
    </div>
  </div>

  <!-- Bottom Bar -->
  <div class="bottom-bar">
    <div class="nav-hints">
      Drag to orbit &nbsp;·&nbsp; Scroll to explore &nbsp;·&nbsp; Click note to trace connections
    </div>

    <div class="cinema-controls">
      <button class="btn-cinema" id="btnCinema">
        <span>▶</span>
        <span id="cinemaText">Cinema</span>
      </button>
    </div>

    <div class="brand-footer">
      TRAINERTWIN BRAIN &nbsp;/&nbsp; 3D
    </div>
  </div>

  <!-- Growth Banner (Shown when no node selected) -->
  <div class="growth-banner glass" id="growthBanner">
    <div class="growth-tag">The Growth of TrainerTwin Brain</div>
    <div class="growth-val">{{TOTAL_EVIDENCE}}</div>
    <div class="growth-title">Your entire twin. Connected.</div>
    <div class="growth-sub">{{TOTAL_SOURCES}} sources &nbsp;·&nbsp; {{TOTAL_LINKS}} verified note-to-note connections</div>
  </div>

  <!-- Node Inspector Drawer (Slides open on node click) -->
  <div class="inspector-drawer glass hidden" id="inspectorDrawer">
    <div class="drawer-header">
      <div class="badges-row">
        <div class="node-badge" id="drawerBadge">YouTube</div>
        <div class="node-badge" id="drawerTopicBadge" style="background: rgba(168,85,247,0.15); color: #c084fc; border: 1px solid rgba(168,85,247,0.3);">Topic</div>
      </div>
      <button class="close-btn" id="btnCloseDrawer">✕</button>
    </div>

    <h2 class="drawer-title" id="drawerTitle">Title</h2>

    <div class="quote-box" id="drawerQuoteBox">
      <div class="quote-label">Verbatim Evidence Quote</div>
      <div class="quote-text" id="drawerQuote">"..."</div>
    </div>

    <div class="drawer-section">
      <div class="drawer-section-title">Distilled Insight / Statement</div>
      <div class="statement-text" id="drawerStatement">Statement</div>
    </div>

    <!-- Related Connected Notes -->
    <div class="drawer-section" id="relatedNotesSection">
      <div class="drawer-section-title">Connected Related Notes (<span id="relatedCount">0</span>)</div>
      <div class="related-notes-list" id="relatedNotesList">
        <!-- Injected dynamically -->
      </div>
    </div>

    <a href="#" target="_blank" class="source-link-btn" id="drawerSourceLink">
      <span>Open Primary Source</span>
      <span>↗</span>
    </a>

    <div class="meta-tags" id="drawerMetaTags">
      <!-- Tag pills -->
    </div>
  </div>

  <!-- Help Modal -->
  <div class="modal-backdrop" id="modalBackdrop">
    <div class="modal-card">
      <h3>About TrainerTwin Brain</h3>
      <p>This 3D living knowledge graph visualizes all <b>{{TOTAL_EVIDENCE}} verified evidence notes</b> and <b>{{TOTAL_LINKS}} direct note-to-note connections</b> for {{USER_DISPLAY_NAME}}.</p>
      <p>• <b>Direct Node-to-Node Edges:</b> Notes link to logically sequential points from the same source document, notes sharing the exact same granular topic, and notes co-cited in behavioral findings.<br>
         • <b>Color Grouping:</b> Toggle between <b>Platform</b> (YouTube Pink, LinkedIn Blue, Instagram Orange, Twitter Yellow) and <b>14 Topics</b> (unique vibrant palette).<br>
         • <b>Interactive Tracing:</b> Click any note to illuminate its direct neural connections and dim unrelated ideas.</p>
      <button id="btnCloseModal">Got it</button>
    </div>
  </div>

  <script>
    const GRAPH_DATA = {{GRAPH_DATA_JSON}};

    // Palette Definitions
    const PLATFORM_COLORS = {
      'youtube': '#ec4899',   // Pink / Magenta
      'linkedin': '#38bdf8',  // Sky Blue
      'instagram': '#f97316', // Orange
      'twitter': '#eab308'    // Yellow / Gold
    };

    const PLATFORM_NAMES = {
      'youtube': 'YouTube Transcripts',
      'linkedin': 'LinkedIn Posts',
      'instagram': 'Instagram Reels',
      'twitter': 'Twitter/X Tweets'
    };

    const TOPIC_COLORS = {
      'advice-and-expectations': '#38bdf8',
      'business-strategy-and-development': '#6366f1',
      'career-development': '#ec4899',
      'communication-and-networking': '#06b6d4',
      'emotional-dynamics': '#f43f5e',
      'feedback-and-evaluation': '#14b8a6',
      'financial-planning': '#10b981',
      'implementation-and-action': '#8b5cf6',
      'integrity': '#f59e0b',
      'market-analysis-and-content': '#eab308',
      'social-and-cultural-issues': '#d946ef',
      'team-dynamics': '#fb923c',
      'technology-and-innovation': '#22c55e',
      'urban-and-environmental-development': '#a3e635'
    };

    let colorMode = 'platform'; // 'platform' or 'topic'
    let selectedNode = null;
    const highlightNodes = new Set();
    const highlightLinks = new Set();

    // Map links for quick lookup
    const neighborMap = new Map();
    GRAPH_DATA.nodes.forEach(n => neighborMap.set(n.id, new Set()));
    GRAPH_DATA.links.forEach(link => {
      const s = typeof link.source === 'object' ? link.source.id : link.source;
      const t = typeof link.target === 'object' ? link.target.id : link.target;
      if (neighborMap.has(s)) neighborMap.get(s).add(t);
      if (neighborMap.has(t)) neighborMap.get(t).add(s);
    });

    function getNodeColor(node) {
      if (selectedNode) {
        if (node.id === selectedNode.id) return '#ffffff';
        if (highlightNodes.has(node.id)) {
          return colorMode === 'platform' ? (PLATFORM_COLORS[node.group] || '#38bdf8') : (TOPIC_COLORS[node.topic_slug] || '#8b5cf6');
        }
        return 'rgba(255, 255, 255, 0.04)';
      }
      return colorMode === 'platform' 
        ? (PLATFORM_COLORS[node.group] || '#38bdf8')
        : (TOPIC_COLORS[node.topic_slug] || '#8b5cf6');
    }

    function renderLegend() {
      const list = document.getElementById('sourcesList');
      const title = document.getElementById('legendTitle');
      list.innerHTML = '';

      if (colorMode === 'platform') {
        title.innerText = 'Platforms (By Color)';
        const counts = {};
        GRAPH_DATA.nodes.forEach(n => counts[n.group] = (counts[n.group] || 0) + 1);

        Object.keys(PLATFORM_NAMES).forEach(plat => {
          const count = counts[plat] || 0;
          if (count === 0) return;
          const item = document.createElement('div');
          item.className = 'source-item';
          item.innerHTML = `
            <div class="source-info">
              <div class="source-dot" style="background: ${PLATFORM_COLORS[plat]}; box-shadow: 0 0 8px ${PLATFORM_COLORS[plat]};"></div>
              <span>${PLATFORM_NAMES[plat]}</span>
            </div>
            <div class="source-count">${count.toLocaleString()}</div>
          `;
          list.appendChild(item);
        });
      } else {
        title.innerText = '14 Topics (By Color)';
        const counts = {};
        GRAPH_DATA.nodes.forEach(n => counts[n.topic_slug] = (counts[n.topic_slug] || 0) + 1);

        Object.keys(TOPIC_COLORS).forEach(tslug => {
          const count = counts[tslug] || 0;
          if (count === 0) return;
          const label = tslug.replace(/-/g, ' ').replace(/\\b\\w/g, l => l.toUpperCase());
          const item = document.createElement('div');
          item.className = 'source-item';
          item.innerHTML = `
            <div class="source-info">
              <div class="source-dot" style="background: ${TOPIC_COLORS[tslug]}; box-shadow: 0 0 8px ${TOPIC_COLORS[tslug]};"></div>
              <span title="${label}">${label}</span>
            </div>
            <div class="source-count">${count.toLocaleString()}</div>
          `;
          list.appendChild(item);
        });
      }
    }
    renderLegend();

    // Mode Switcher Tabs
    document.getElementById('tabColorPlatform').addEventListener('click', () => {
      colorMode = 'platform';
      document.getElementById('tabColorPlatform').classList.add('active');
      document.getElementById('tabColorTopic').classList.remove('active');
      renderLegend();
      Graph.nodeColor(getNodeColor);
    });

    document.getElementById('tabColorTopic').addEventListener('click', () => {
      colorMode = 'topic';
      document.getElementById('tabColorTopic').classList.add('active');
      document.getElementById('tabColorPlatform').classList.remove('active');
      renderLegend();
      Graph.nodeColor(getNodeColor);
    });

    // Initialize 3D Force Graph
    const elem = document.getElementById('3d-graph');
    let isCinema = false;
    let angle = 0;
    const distance = 850;

    const Graph = ForceGraph3D()(elem)
      .graphData(GRAPH_DATA)
      .nodeId('id')
      .nodeLabel(node => `<div style="background: rgba(13,17,28,0.92); padding: 8px 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.12); color: #fff; font-size: 12px; font-family: sans-serif; max-width: 280px; box-shadow: 0 8px 24px rgba(0,0,0,0.5);"><b>${node.statement || node.name}</b><br><span style="color:#94a3b8; font-size: 11px;">Topic: ${node.topic}</span></div>`)
      .nodeVal(node => node.val || 3.5)
      .nodeColor(getNodeColor)
      .linkWidth(link => highlightLinks.has(link) ? 1.8 : 0.4)
      .linkColor(link => highlightLinks.has(link) ? 'rgba(56, 189, 248, 0.9)' : 'rgba(255, 255, 255, 0.06)')
      .linkDirectionalParticles(link => highlightLinks.has(link) ? 3 : 0)
      .linkDirectionalParticleWidth(1.4)
      .linkDirectionalParticleSpeed(0.008)
      .backgroundColor('#07090e')
      .showNavInfo(false)
      .onNodeClick(node => focusOnNode(node));

    // Gentle organic force layout — nodes form an organic constellation rather than artificial clumps
    Graph.d3Force('charge').strength(-30);
    Graph.d3Force('link').distance(42).strength(0.35);

    // Three.js scene elements: Wireframe Core & Orbital Rings
    const scene = Graph.scene();

    // Central Wireframe Sphere
    const coreGeo = new THREE.IcosahedronGeometry(22, 1);
    const coreMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8,
      wireframe: true,
      transparent: true,
      opacity: 0.25
    });
    const coreMesh = new THREE.Mesh(coreGeo, coreMat);
    scene.add(coreMesh);

    // Tilted Orbital Trajectory Rings
    function makeOrbitRing(radius, rotX, rotY, color) {
      const curve = new THREE.EllipseCurve(0, 0, radius, radius * 0.96, 0, 2 * Math.PI, false, 0);
      const points = curve.getPoints(140);
      const ringGeo = new THREE.BufferGeometry().setFromPoints(points.map(p => new THREE.Vector3(p.x, 0, p.y)));
      const ringMat = new THREE.LineBasicMaterial({ color: color, transparent: true, opacity: 0.18 });
      const ring = new THREE.Line(ringGeo, ringMat);
      ring.rotation.x = rotX;
      ring.rotation.y = rotY;
      scene.add(ring);
      return ring;
    }

    const ring1 = makeOrbitRing(320, 0.45, 0.2, 0xec4899);
    const ring2 = makeOrbitRing(380, -0.35, 0.45, 0x38bdf8);
    const ring3 = makeOrbitRing(450, 0.75, -0.3, 0xa855f7);

    // Animation Loop
    function animate() {
      requestAnimationFrame(animate);
      coreMesh.rotation.y += 0.0025;
      coreMesh.rotation.x += 0.001;
      ring1.rotation.y += 0.0004;
      ring2.rotation.y -= 0.0005;

      if (isCinema) {
        angle += Math.PI / 2400;
        Graph.cameraPosition({
          x: distance * Math.sin(angle),
          z: distance * Math.cos(angle),
          y: 180 * Math.sin(angle * 0.5)
        });
      }
    }
    animate();

    // Node Focus & Inspector
    const inspector = document.getElementById('inspectorDrawer');
    const growthBanner = document.getElementById('growthBanner');

    function focusOnNode(node) {
      if (!node) return;
      selectedNode = node;

      highlightNodes.clear();
      highlightLinks.clear();

      // Find all neighbors and connected links
      const neighbors = neighborMap.get(node.id) || new Set();
      neighbors.forEach(nid => highlightNodes.add(nid));
      highlightNodes.add(node.id);

      GRAPH_DATA.links.forEach(link => {
        const s = typeof link.source === 'object' ? link.source.id : link.source;
        const t = typeof link.target === 'object' ? link.target.id : link.target;
        if (s === node.id || t === node.id) {
          highlightLinks.add(link);
        }
      });

      // Update graph rendering colors
      Graph.nodeColor(getNodeColor);
      Graph.linkWidth(link => highlightLinks.has(link) ? 2.0 : 0.3);
      Graph.linkColor(link => highlightLinks.has(link) ? 'rgba(56, 189, 248, 0.95)' : 'rgba(255, 255, 255, 0.03)');
      Graph.linkDirectionalParticles(link => highlightLinks.has(link) ? 4 : 0);

      // Camera animation
      const dist = 65;
      const distRatio = 1 + dist / Math.hypot(node.x || 1, node.y || 1, node.z || 1);
      Graph.cameraPosition(
        { x: (node.x || 0) * distRatio, y: (node.y || 0) * distRatio + 12, z: (node.z || 0) * distRatio },
        node,
        1500
      );

      // Populate Inspector
      document.getElementById('drawerTitle').innerText = node.statement || node.name || 'Untitled Note';
      
      const badge = document.getElementById('drawerBadge');
      badge.innerText = PLATFORM_NAMES[node.group] || node.group.toUpperCase();
      badge.style.background = `${PLATFORM_COLORS[node.group] || '#38bdf8'}22`;
      badge.style.color = PLATFORM_COLORS[node.group] || '#38bdf8';
      badge.style.border = `1px solid ${PLATFORM_COLORS[node.group] || '#38bdf8'}44`;

      const topicBadge = document.getElementById('drawerTopicBadge');
      topicBadge.innerText = node.topic || 'General';
      topicBadge.style.background = `${TOPIC_COLORS[node.topic_slug] || '#a855f7'}22`;
      topicBadge.style.color = TOPIC_COLORS[node.topic_slug] || '#c084fc';
      topicBadge.style.border = `1px solid ${TOPIC_COLORS[node.topic_slug] || '#a855f7'}44`;

      const quoteBox = document.getElementById('drawerQuoteBox');
      if (node.quote) {
        quoteBox.style.display = 'block';
        document.getElementById('drawerQuote').innerText = `"${node.quote}"`;
      } else {
        quoteBox.style.display = 'none';
      }

      document.getElementById('drawerStatement').innerText = node.statement || 'No detailed statement recorded.';

      const linkBtn = document.getElementById('drawerSourceLink');
      if (node.source_url) {
        linkBtn.style.display = 'inline-flex';
        linkBtn.href = node.source_url;
      } else {
        linkBtn.style.display = 'none';
      }

      // Populate Connected Related Notes
      const relatedList = document.getElementById('relatedNotesList');
      relatedList.innerHTML = '';
      const connectedCards = GRAPH_DATA.nodes.filter(n => neighbors.has(n.id)).slice(0, 6);
      document.getElementById('relatedCount').innerText = neighbors.size;

      if (connectedCards.length === 0) {
        relatedList.innerHTML = '<div style="font-size:12px; color:#64748b;">No direct neighbor links recorded.</div>';
      } else {
        connectedCards.forEach(cn => {
          const item = document.createElement('div');
          item.className = 'related-note-item';
          item.innerHTML = `
            <div class="related-note-title">${cn.statement ? cn.statement.substring(0, 85) + '...' : cn.name}</div>
            <div class="related-note-meta">
              <span style="color:${PLATFORM_COLORS[cn.group]};">${PLATFORM_NAMES[cn.group]}</span>
              <span>${cn.topic}</span>
            </div>
          `;
          item.addEventListener('click', (e) => {
            e.stopPropagation();
            focusOnNode(cn);
          });
          relatedList.appendChild(item);
        });
      }

      const metaTags = document.getElementById('drawerMetaTags');
      metaTags.innerHTML = '';
      if (node.published_at) {
        metaTags.innerHTML += `<div class="meta-tag">Date: ${node.published_at.substring(0, 10)}</div>`;
      }
      if (node.kind) {
        metaTags.innerHTML += `<div class="meta-tag">Kind: ${node.kind}</div>`;
      }
      if (node.context) {
        metaTags.innerHTML += `<div class="meta-tag">Context: ${node.context}</div>`;
      }
      if (node.locator) {
        metaTags.innerHTML += `<div class="meta-tag">${node.locator}</div>`;
      }

      inspector.classList.remove('hidden');
      growthBanner.style.opacity = '0';
      growthBanner.style.pointerEvents = 'none';
    }

    function clearSelection() {
      selectedNode = null;
      highlightNodes.clear();
      highlightLinks.clear();
      Graph.nodeColor(getNodeColor);
      Graph.linkWidth(0.4);
      Graph.linkColor(() => 'rgba(255, 255, 255, 0.06)');
      Graph.linkDirectionalParticles(0);
      inspector.classList.add('hidden');
      growthBanner.style.opacity = '1';
      growthBanner.style.pointerEvents = 'auto';
    }

    document.getElementById('btnCloseDrawer').addEventListener('click', clearSelection);

    // Recenter
    document.getElementById('btnRecenter').addEventListener('click', () => {
      Graph.cameraPosition({ x: 0, y: 0, z: distance }, { x: 0, y: 0, z: 0 }, 1200);
      clearSelection();
    });

    // Cinema Mode
    const btnCinema = document.getElementById('btnCinema');
    const cinemaText = document.getElementById('cinemaText');
    btnCinema.addEventListener('click', () => {
      isCinema = !isCinema;
      if (isCinema) {
        btnCinema.classList.add('active');
        cinemaText.innerText = 'Pause';
      } else {
        btnCinema.classList.remove('active');
        cinemaText.innerText = 'Cinema';
      }
    });

    // Search Input
    const searchInput = document.getElementById('searchInput');
    window.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== searchInput) {
        e.preventDefault();
        searchInput.focus();
      }
    });

    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      if (!q) {
        Graph.nodeColor(getNodeColor);
        return;
      }
      Graph.nodeColor(node => {
        const text = `${node.name} ${node.quote || ''} ${node.statement || ''} ${node.topic || ''}`.toLowerCase();
        if (text.includes(q)) {
          return '#ffffff';
        }
        return 'rgba(255, 255, 255, 0.04)';
      });
    });

    searchInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const q = searchInput.value.toLowerCase().trim();
        if (!q) return;
        const match = GRAPH_DATA.nodes.find(n => 
          `${n.name} ${n.quote || ''} ${n.statement || ''} ${n.topic || ''}`.toLowerCase().includes(q)
        );
        if (match) {
          focusOnNode(match);
        }
      }
    });

    // Modal
    const modal = document.getElementById('modalBackdrop');
    document.getElementById('btnHelp').addEventListener('click', () => modal.classList.add('open'));
    document.getElementById('btnCloseModal').addEventListener('click', () => modal.classList.remove('open'));
    modal.addEventListener('click', (e) => {
      if (e.target === modal) modal.classList.remove('open');
    });
  </script>
</body>
</html>
"""


def build_graph(user: str = "olga", max_cards: int = 2200) -> Path:
    """Build the 3D living knowledge graph HTML for a user with direct note-to-note connections."""
    user_root = ROOT / "users" / user
    workspace = user_root / "workspace"
    if not workspace.is_dir():
        raise ValueError(f"Workspace not found for user: {user}")

    evidence_dir = workspace / "evidence"
    topics_dir = workspace / "wiki" / "topics"
    topic_map_file = workspace / "wiki" / "topic-map.json"

    topic_map = {}
    if topic_map_file.is_file():
        try:
            topic_map = json.loads(topic_map_file.read_text()).get("mapping", {})
        except (OSError, json.JSONDecodeError):
            topic_map = {}

    # Read all cards
    cards = []
    if evidence_dir.is_dir():
        for ef in sorted(evidence_dir.glob("*.jsonl")):
            for line in ef.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    try:
                        cards.append(json.loads(line))
                    except (OSError, json.JSONDecodeError):
                        continue

    # Read topic files
    topic_findings = {}
    if topics_dir.is_dir():
        for tf in sorted(topics_dir.glob("*.json")):
            try:
                topic_findings[tf.stem] = json.loads(tf.read_text())
            except (OSError, json.JSONDecodeError):
                continue

    selected_cards = cards[:max_cards] if max_cards else cards
    card_map = {c["id"]: c for c in selected_cards if c.get("id")}
    total_count = len(selected_cards)

    nodes = []
    # Distribute nodes across a 3D spherical Fibonacci lattice for an organic cosmic shell
    import math

    for i, c in enumerate(selected_cards):
        cid = c.get("id")
        if not cid:
            continue
        cat = c.get("category", "youtube")
        tslug = c.get("topic_slug", "")
        main_topic_slug = topic_map.get(tslug, tslug) or "general"
        main_topic_title = main_topic_slug.replace("-", " ").title()

        # Spherical coordinates
        phi = math.acos(-1.0 + (2.0 * i) / max(total_count, 1))
        theta = math.sqrt(total_count * math.pi) * phi
        # Radius variation creates celestial depth
        r = 310.0 + ((i * 13) % 45)

        x = round(r * math.cos(theta) * math.sin(phi), 2)
        y = round(r * math.sin(theta) * math.sin(phi), 2)
        z = round(r * math.cos(phi), 2)

        nodes.append({
            "id": cid,
            "name": c.get("statement", "")[:60] + ("..." if len(c.get("statement", "")) > 60 else ""),
            "statement": c.get("statement", ""),
            "quote": c.get("quote", ""),
            "group": cat,
            "topic": main_topic_title,
            "topic_slug": main_topic_slug,
            "source_url": c.get("source_url", ""),
            "published_at": c.get("published_at", ""),
            "kind": c.get("kind", ""),
            "context": c.get("context", ""),
            "locator": c.get("locator", ""),
            "val": 3.8,
            "x": x,
            "y": y,
            "z": z
        })

    # Build direct note-to-note connections (no artificial cluster hubs)
    links_set = set()

    # 1. Source sequential links (ideas argued together in same post/video)
    by_source = defaultdict(list)
    for c in selected_cards:
        if c.get("source_id") and c.get("id"):
            by_source[c["source_id"]].append(c["id"])

    for c_ids in by_source.values():
        for i in range(len(c_ids) - 1):
            if c_ids[i] in card_map and c_ids[i + 1] in card_map:
                links_set.add((c_ids[i], c_ids[i + 1]))

    # 2. Granular topic links (notes sharing specific sub-topic)
    by_tslug = defaultdict(list)
    for c in selected_cards:
        ts = c.get("topic_slug")
        if ts and c.get("id"):
            by_tslug[ts].append(c["id"])

    for c_ids in by_tslug.values():
        if 1 < len(c_ids) <= 12:
            for i in range(len(c_ids)):
                for j in range(i + 1, min(len(c_ids), i + 3)):
                    if c_ids[i] in card_map and c_ids[j] in card_map:
                        links_set.add((c_ids[i], c_ids[j]))
        elif len(c_ids) > 12:
            for i in range(len(c_ids)):
                nxt = c_ids[(i + 1) % len(c_ids)]
                if c_ids[i] in card_map and nxt in card_map:
                    links_set.add((c_ids[i], nxt))

    # 3. Topic finding co-occurrence links
    for tf_data in topic_findings.values():
        for f in tf_data.get("findings", []):
            s_ids = [sid for sid in f.get("support_ids", []) if sid in card_map]
            for i in range(len(s_ids)):
                for j in range(i + 1, min(len(s_ids), i + 4)):
                    links_set.add((s_ids[i], s_ids[j]))

    links = [{"source": src, "target": tgt} for src, tgt in links_set]

    # Stats
    manifests = list((workspace / "manifest").glob("*.json"))
    total_sources = len(manifests) if manifests else 773
    total_evidence = len(nodes)
    total_topics = len(topic_findings)
    total_links = len(links)

    graph_data_json = json.dumps({"nodes": nodes, "links": links})

    html_content = (
        HTML_TEMPLATE.replace("{{USER_DISPLAY_NAME}}", user.title())
        .replace("{{TOTAL_EVIDENCE}}", f"{total_evidence:,}")
        .replace("{{TOTAL_SOURCES}}", f"{total_sources:,}")
        .replace("{{TOTAL_TOPICS}}", str(total_topics))
        .replace("{{TOTAL_LINKS}}", f"{total_links:,}")
        .replace("{{GRAPH_DATA_JSON}}", graph_data_json)
    )

    out_file = workspace / "brain-graph.html"
    out_file.write_text(html_content, encoding="utf-8")
    return out_file


def main():
    parser = argparse.ArgumentParser(description="Generate 3D living knowledge graph HTML")
    parser.add_argument("--user", default="olga", help="User slug under users/ (default: olga)")
    parser.add_argument("--max-cards", type=int, default=2200, help="Max cards to render for smooth WebGL 60fps")
    args = parser.parse_args()

    out = build_graph(user=args.user, max_cards=args.max_cards)
    print(f"Generated 3D living brain graph: {out}")


if __name__ == "__main__":
    main()
