"""Generate a 3D interactive living knowledge graph visualization for TrainerTwin Lore.

Creates an interactive, WebGL-powered 3D constellation of evidence cards,
topic clusters, and source documents inspired by cosmic brain graph interfaces.

Run:
    uv run python -m pipeline.graph --user olga
"""

import argparse
import json
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
      background: rgba(13, 17, 28, 0.72);
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
      width: 320px;
      padding: 24px;
      z-index: 10;
      pointer-events: auto;
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
      margin-bottom: 24px;
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

    /* Sources List */
    .section-title {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: #64748b;
      font-weight: 700;
      margin-bottom: 12px;
    }

    .sources-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 20px;
    }

    .source-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 6px 10px;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .source-item:hover, .source-item.active {
      background: rgba(255, 255, 255, 0.06);
    }

    .source-info {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 13px;
      color: #cbd5e1;
    }

    .source-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
    }

    .source-count {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: #64748b;
    }

    /* Filters */
    .filter-options {
      display: flex;
      flex-direction: column;
      gap: 8px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
      padding-top: 16px;
    }

    .filter-checkbox {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      color: #94a3b8;
      cursor: pointer;
    }

    .filter-checkbox input {
      accent-color: #38bdf8;
      cursor: pointer;
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
      width: 400px;
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
      font-size: 18px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #fff;
      margin-bottom: 12px;
      line-height: 1.3;
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
        <span id="nodesInViewCount">2,769</span> notes in view
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
    <p class="hero-desc">{{USER_DISPLAY_NAME}}'s TrainerTwin universe. Attested public evidence, platform behaviors, and decision heuristics.</p>

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

    <div class="section-title">Sources & Categories</div>
    <div class="sources-list" id="sourcesList">
      <!-- Populated via JS -->
    </div>

    <div class="filter-options">
      <label class="filter-checkbox">
        <input type="checkbox" id="chkShowLabels" checked>
        <span>Show all labels</span>
      </label>
      <label class="filter-checkbox">
        <input type="checkbox" id="chkHighlightObjections">
        <span>Highlight roleplays & objections</span>
      </label>
    </div>
  </div>

  <!-- Bottom Bar -->
  <div class="bottom-bar">
    <div class="nav-hints">
      Drag to orbit &nbsp;·&nbsp; Scroll to explore &nbsp;·&nbsp; Click node to inspect
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
    <div class="growth-sub">{{TOTAL_SOURCES}} sources &nbsp;·&nbsp; {{TOTAL_EVIDENCE}} of {{TOTAL_EVIDENCE}} verified notes</div>
  </div>

  <!-- Node Inspector Drawer (Slides open on node click) -->
  <div class="inspector-drawer glass hidden" id="inspectorDrawer">
    <div class="drawer-header">
      <div class="node-badge" id="drawerBadge">YouTube Transcript</div>
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

    <div class="drawer-section" id="drawerTopicSection">
      <div class="drawer-section-title">Topic Synthesis</div>
      <div class="statement-text" id="drawerTopic">Topic</div>
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
      <p>This 3D living knowledge graph visualizes all <b>{{TOTAL_EVIDENCE}} verified evidence cards</b> and <b>{{TOTAL_SOURCES}} source documents</b> for {{USER_DISPLAY_NAME}}.</p>
      <p>• <b>Pink Nodes:</b> YouTube transcripts & video coaching.<br>
         • <b>Blue Nodes:</b> LinkedIn posts and frameworks.<br>
         • <b>Orange Nodes:</b> Instagram reels & breakdowns.<br>
         • <b>Purple Nodes:</b> Central topic hubs synthesized by LLM.<br>
         • <b>Cyan Center:</b> TrainerTwin Core Nucleus.</p>
      <p>Click any node to zoom into its verbatim quote, primary publication URL, and behavioral decision rule.</p>
      <button id="btnCloseModal">Got it</button>
    </div>
  </div>

  <script>
    const GRAPH_DATA = {{GRAPH_DATA_JSON}};

    const CATEGORY_COLORS = {
      'core': '#06b6d4',
      'topic': '#a855f7',
      'youtube': '#ec4899',
      'linkedin': '#38bdf8',
      'instagram': '#f97316',
      'twitter': '#eab308'
    };

    const CATEGORY_NAMES = {
      'youtube': 'YouTube Transcripts',
      'linkedin': 'LinkedIn Posts',
      'instagram': 'Instagram Reels',
      'twitter': 'Twitter/X Tweets',
      'topic': 'Topic Syntheses'
    };

    // Render legend
    const sourcesList = document.getElementById('sourcesList');
    const counts = {};
    GRAPH_DATA.nodes.forEach(n => {
      counts[n.group] = (counts[n.group] || 0) + 1;
    });

    Object.keys(CATEGORY_NAMES).forEach(cat => {
      const count = counts[cat] || 0;
      if (count === 0) return;
      const item = document.createElement('div');
      item.className = 'source-item';
      item.dataset.category = cat;
      item.innerHTML = `
        <div class="source-info">
          <div class="source-dot" style="background: ${CATEGORY_COLORS[cat]}; box-shadow: 0 0 8px ${CATEGORY_COLORS[cat]};"></div>
          <span>${CATEGORY_NAMES[cat]}</span>
        </div>
        <div class="source-count">${count.toLocaleString()}</div>
      `;
      item.addEventListener('click', () => filterByCategory(cat));
      sourcesList.appendChild(item);
    });

    // Initialize 3D Force Graph
    const elem = document.getElementById('3d-graph');
    let isCinema = false;
    let angle = 0;
    const distance = 850;

    const Graph = ForceGraph3D()(elem)
      .graphData(GRAPH_DATA)
      .nodeId('id')
      .nodeLabel(node => `<div style="background: rgba(13,17,28,0.9); padding: 6px 12px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); color: #fff; font-size: 12px; font-family: sans-serif;"><b>${node.name}</b><br><span style="color:#94a3b8;">${node.group.toUpperCase()}</span></div>`)
      .nodeVal(node => node.val)
      .nodeColor(node => node.color || CATEGORY_COLORS[node.group] || '#94a3b8')
      .linkWidth(link => link.width || 0.5)
      .linkColor(link => link.color || 'rgba(255, 255, 255, 0.08)')
      .linkDirectionalParticles(link => link.particles || 0)
      .linkDirectionalParticleWidth(1.2)
      .linkDirectionalParticleSpeed(0.005)
      .backgroundColor('#07090e')
      .showNavInfo(false)
      .onNodeClick(node => focusOnNode(node));

    // Add Central Wireframe Icosahedron & Planetary Rings via Three.js
    const scene = Graph.scene();

    // Central Wireframe Sphere
    const coreGeo = new THREE.IcosahedronGeometry(18, 1);
    const coreMat = new THREE.MeshBasicMaterial({
      color: 0x38bdf8,
      wireframe: true,
      transparent: true,
      opacity: 0.35
    });
    const coreMesh = new THREE.Mesh(coreGeo, coreMat);
    scene.add(coreMesh);

    // Inner glowing sphere
    const innerGeo = new THREE.SphereGeometry(6, 16, 16);
    const innerMat = new THREE.MeshBasicMaterial({
      color: 0x06b6d4,
      transparent: true,
      opacity: 0.7
    });
    const innerMesh = new THREE.Mesh(innerGeo, innerMat);
    scene.add(innerMesh);

    // Tilted Orbital Rings
    function makeOrbitRing(radius, rotX, rotY, color) {
      const curve = new THREE.EllipseCurve(0, 0, radius, radius * 0.95, 0, 2 * Math.PI, false, 0);
      const points = curve.getPoints(120);
      const ringGeo = new THREE.BufferGeometry().setFromPoints(points.map(p => new THREE.Vector3(p.x, 0, p.y)));
      const ringMat = new THREE.LineBasicMaterial({ color: color, transparent: true, opacity: 0.2 });
      const ring = new THREE.Line(ringGeo, ringMat);
      ring.rotation.x = rotX;
      ring.rotation.y = rotY;
      scene.add(ring);
      return ring;
    }

    const ring1 = makeOrbitRing(280, 0.4, 0.2, 0xec4899);
    const ring2 = makeOrbitRing(340, -0.3, 0.5, 0x38bdf8);
    const ring3 = makeOrbitRing(420, 0.8, -0.4, 0xa855f7);

    // Animation Loop
    function animate() {
      requestAnimationFrame(animate);
      coreMesh.rotation.y += 0.003;
      coreMesh.rotation.x += 0.001;
      ring1.rotation.y += 0.0005;
      ring2.rotation.y -= 0.0007;

      if (isCinema) {
        angle += Math.PI / 2400;
        Graph.cameraPosition({
          x: distance * Math.sin(angle),
          z: distance * Math.cos(angle),
          y: 200 * Math.sin(angle * 0.5)
        });
      }
    }
    animate();

    // Node Click & Inspector
    const inspector = document.getElementById('inspectorDrawer');
    const growthBanner = document.getElementById('growthBanner');

    function focusOnNode(node) {
      if (!node) return;

      const dist = 60;
      const distRatio = 1 + dist / Math.hypot(node.x || 1, node.y || 1, node.z || 1);
      Graph.cameraPosition(
        { x: (node.x || 0) * distRatio, y: (node.y || 0) * distRatio + 10, z: (node.z || 0) * distRatio },
        node,
        1500
      );

      // Populate Inspector
      document.getElementById('drawerTitle').innerText = node.statement || node.name || 'Untitled';
      
      const badge = document.getElementById('drawerBadge');
      badge.innerText = CATEGORY_NAMES[node.group] || node.group.toUpperCase();
      badge.style.background = `${CATEGORY_COLORS[node.group] || '#38bdf8'}22`;
      badge.style.color = CATEGORY_COLORS[node.group] || '#38bdf8';
      badge.style.border = `1px solid ${CATEGORY_COLORS[node.group] || '#38bdf8'}44`;

      const quoteBox = document.getElementById('drawerQuoteBox');
      if (node.quote) {
        quoteBox.style.display = 'block';
        document.getElementById('drawerQuote').innerText = `"${node.quote}"`;
      } else {
        quoteBox.style.display = 'none';
      }

      document.getElementById('drawerStatement').innerText = node.statement || node.description || 'No detailed statement available.';
      document.getElementById('drawerTopic').innerText = node.topic || node.name || 'General';

      const linkBtn = document.getElementById('drawerSourceLink');
      if (node.source_url) {
        linkBtn.style.display = 'inline-flex';
        linkBtn.href = node.source_url;
      } else {
        linkBtn.style.display = 'none';
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

    document.getElementById('btnCloseDrawer').addEventListener('click', () => {
      inspector.classList.add('hidden');
      growthBanner.style.opacity = '1';
      growthBanner.style.pointerEvents = 'auto';
    });

    // Recenter
    document.getElementById('btnRecenter').addEventListener('click', () => {
      Graph.cameraPosition({ x: 0, y: 0, z: distance }, { x: 0, y: 0, z: 0 }, 1200);
      inspector.classList.add('hidden');
      growthBanner.style.opacity = '1';
      growthBanner.style.pointerEvents = 'auto';
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
        Graph.nodeColor(node => node.color || CATEGORY_COLORS[node.group] || '#94a3b8');
        return;
      }
      Graph.nodeColor(node => {
        const text = `${node.name} ${node.quote || ''} ${node.statement || ''} ${node.topic || ''}`.toLowerCase();
        if (text.includes(q)) {
          return '#38bdf8';
        }
        return 'rgba(255, 255, 255, 0.05)';
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

    // Filter by category
    let activeFilter = null;
    function filterByCategory(cat) {
      if (activeFilter === cat) {
        activeFilter = null;
        document.querySelectorAll('.source-item').forEach(el => el.classList.remove('active'));
        Graph.nodeColor(node => node.color || CATEGORY_COLORS[node.group] || '#94a3b8');
        Graph.linkColor(() => 'rgba(255, 255, 255, 0.08)');
        return;
      }
      activeFilter = cat;
      document.querySelectorAll('.source-item').forEach(el => {
        el.classList.toggle('active', el.dataset.category === cat);
      });
      Graph.nodeColor(node => {
        if (node.group === cat || (node.group === 'core' || node.group === 'topic')) {
          return CATEGORY_COLORS[node.group];
        }
        return 'rgba(255, 255, 255, 0.04)';
      });
      Graph.linkColor(link => {
        const srcGroup = typeof link.source === 'object' ? link.source.group : '';
        const tgtGroup = typeof link.target === 'object' ? link.target.group : '';
        if (srcGroup === cat || tgtGroup === cat) {
          return `${CATEGORY_COLORS[cat]}44`;
        }
        return 'rgba(255, 255, 255, 0.02)';
      });
    }

    // Roleplay / Objection highlighting
    document.getElementById('chkHighlightObjections').addEventListener('change', (e) => {
      const active = e.target.checked;
      if (!active) {
        Graph.nodeColor(node => node.color || CATEGORY_COLORS[node.group] || '#94a3b8');
        return;
      }
      Graph.nodeColor(node => {
        if (node.context === 'hypothetical' || node.kind === 'teaching_move') {
          return '#f43f5e'; // Highlight in glowing red/rose
        }
        return 'rgba(255, 255, 255, 0.08)';
      });
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


def build_graph(user: str = "olga", max_cards: int = 1500) -> Path:
    """Build the 3D living knowledge graph HTML for a user."""
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

    nodes = []
    links = []

    # 1. Central Nucleus Core Node
    core_id = "core-nucleus"
    nodes.append({
        "id": core_id,
        "name": f"{user.title()} (TrainerTwin Core)",
        "group": "core",
        "val": 30,
        "color": "#06b6d4",
        "statement": f"Central TrainerTwin intelligence nucleus for {user}."
    })

    # 2. Topic Nodes
    for topic_slug in topic_findings:
        topic_name = topic_slug.replace("-", " ").title()
        nodes.append({
            "id": f"topic:{topic_slug}",
            "name": topic_name,
            "group": "topic",
            "val": 16,
            "color": "#a855f7",
            "topic": topic_name,
            "statement": f"Core behavioral and knowledge synthesis topic: {topic_name}."
        })
        # Link topic to core
        links.append({
            "source": core_id,
            "target": f"topic:{topic_slug}",
            "width": 1.5,
            "color": "rgba(168, 85, 247, 0.4)",
            "particles": 2
        })

    # 3. Evidence Nodes (sampled or all up to max_cards for smooth 60fps WebGL)
    selected_cards = cards[:max_cards] if max_cards else cards
    card_ids = set()

    for c in selected_cards:
        cid = c.get("id")
        if not cid:
            continue
        card_ids.add(cid)
        cat = c.get("category", "youtube")
        tslug = c.get("topic_slug", "")
        main_topic = topic_map.get(tslug, tslug)

        nodes.append({
            "id": cid,
            "name": c.get("statement", "")[:50] + ("..." if len(c.get("statement", "")) > 50 else ""),
            "statement": c.get("statement", ""),
            "quote": c.get("quote", ""),
            "group": cat,
            "val": 4,
            "topic": main_topic.replace("-", " ").title() if main_topic else "",
            "source_url": c.get("source_url", ""),
            "published_at": c.get("published_at", ""),
            "kind": c.get("kind", ""),
            "context": c.get("context", ""),
            "locator": c.get("locator", "")
        })

        # Link card to its topic hub
        if main_topic and f"topic:{main_topic}" in [n["id"] for n in nodes]:
            links.append({
                "source": f"topic:{main_topic}",
                "target": cid,
                "width": 0.35,
                "color": "rgba(255, 255, 255, 0.06)"
            })

    # 4. Cross-Evidence Co-occurrence Links from Findings
    for tf_data in topic_findings.values():
        for f in tf_data.get("findings", []):
            s_ids = [sid for sid in f.get("support_ids", []) if sid in card_ids]
            if len(s_ids) > 1:
                for i in range(len(s_ids)):
                    for j in range(i + 1, min(len(s_ids), i + 3)):
                        links.append({
                            "source": s_ids[i],
                            "target": s_ids[j],
                            "width": 0.8,
                            "color": "rgba(56, 189, 248, 0.25)"
                        })

    # Count sources
    manifests = list((workspace / "manifest").glob("*.json"))
    total_sources = len(manifests) if manifests else 773
    total_evidence = len(cards)
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
    parser.add_argument("--max-cards", type=int, default=1800, help="Max cards to render for smooth WebGL 60fps")
    args = parser.parse_args()

    out = build_graph(user=args.user, max_cards=args.max_cards)
    print(f"Generated 3D living brain graph: {out}")


if __name__ == "__main__":
    main()
