// aoe2-codex: marks on the tree what the codex changed and shows why (data/codex.json, written by
// codex/tools/build_site.py). Loaded after main.js and version.js; it wraps a few of main.js's global
// functions instead of changing that file, so the original site stays as it is.
(function () {
    'use strict';

    const KINDS = {
        removed: {glyph: '−', colour: '#b3261e', label: 'Removed by the codex', key: 'removed'},
        added: {glyph: '+', colour: '#1e7d34', label: 'Added by the codex', key: 'added'},
        new: {glyph: '★', colour: '#b8860b', label: 'New or changed unique item', key: 'new or changed unique'},
        renamed: {glyph: 'R', colour: '#2b5d9e', label: 'Renamed by the codex', key: 'renamed'},
        kept: {label: 'Unique item kept from the game'},
    };
    const MARKED = ['removed', 'added', 'new', 'renamed'];
    const TOOLTIP_LENGTH = 320;

    let codex = {civs: {}};
    const load = window.loadJson;
    // Every data file waits for codex.json, so the tree is never drawn without its marks.
    const ready = new Promise(function (resolve) {
        load('data/codex.json', function (response) {
            codex = response;
            resolve();
        });
        setTimeout(resolve, 4000);
    });
    window.loadJson = function (file, callback) {
        return load(file, function (response) {
            ready.then(function () {
                callback(response);
            });
        });
    };

    function esc(text) {
        return String(text).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    function shorten(text, limit) {
        text = text.replace(/\s+/g, ' ').trim();
        return text.length <= limit ? text : text.slice(0, limit).replace(/\s+\S*$/, '') + '…';
    }

    function currentCiv() {
        const select = document.getElementById('civselect');
        return select ? select.value : '';
    }

    function changeFor(nodeId) {
        const civ = codex.civs[currentCiv()];
        return civ ? civ[nodeId] : undefined;
    }

    function labelOf(entry) {
        return entry.kinds.map(function (kind) {
            return KINDS[kind].label;
        }).join('; ');
    }

    const drawItem = window.drawItem;
    window.drawItem = function (itemToDraw, element_height, tree_height, draw) {
        drawItem(itemToDraw, element_height, tree_height, draw);
        const entry = changeFor(itemToDraw.id);
        if (!entry) {
            return;
        }
        const group = draw.findOne(`[id="${itemToDraw.id}"]`);
        const overlay = draw.findOne(`[id="${itemToDraw.id}_overlay"]`);
        if (!group || !overlay) {
            return;
        }
        const why = entry.why.join(' ');
        overlay.attr('data-codex-why', labelOf(entry) + (why ? ': ' + shorten(why, TOOLTIP_LENGTH) : '.') + ' Click for the full reason.');
        const kind = MARKED.find(function (k) {
            return entry.kinds.includes(k);
        });
        if (!kind) {
            return;
        }
        const r = element_height * 0.17;
        const cx = itemToDraw.x + element_height - r * 0.85;
        const cy = itemToDraw.y + r * 0.85;
        const badge = group.group().addClass('codex-marker').attr({'pointer-events': 'none'});
        badge.circle(r * 2).center(cx, cy).attr({fill: KINDS[kind].colour, stroke: '#fff', 'stroke-width': 1.5});
        badge.text(KINDS[kind].glyph)
            .font({size: r * 1.5, weight: 'bold'})
            .attr({fill: '#fff', 'text-anchor': 'middle', 'dominant-baseline': 'central'})
            .center(cx, cy);
    };

    const getHelpText = window.getHelpText;
    window.getHelpText = function (name, fullId, helpStringId) {
        let html = getHelpText(name, fullId, helpStringId);
        const entry = changeFor(fullId);
        if (entry) {
            html += '<div class="codex-help"><p class="codex-help__title">Codex: ' + esc(labelOf(entry)) + '</p>'
                + entry.why.map(function (why) {
                    return '<p>' + esc(why) + '</p>';
                }).join('') + '</div>';
        }
        return html;
    };

    function setMarkers(show) {
        document.body.classList.toggle('codex-no-markers', !show);
        try {
            localStorage.setItem('codexMarkers', show ? 'on' : 'off');
        } catch (e) {
            // pass
        }
    }

    function updateCompareLink() {
        const link = document.getElementById('codex-compare');
        if (link) {
            link.href = 'compare.html' + window.location.search + window.location.hash;
        }
    }

    function addTools() {
        const civinfo = document.getElementById('civinfo');
        const civtext = document.getElementById('civtext');
        if (!civinfo || !civtext) {
            return;
        }
        const tools = document.createElement('div');
        tools.id = 'codex-tools';
        const legend = MARKED.map(function (kind) {
            return `<span class="codex-legend__item"><span class="codex-badge" style="background:${KINDS[kind].colour}">`
                + `${KINDS[kind].glyph}</span> ${KINDS[kind].key}</span>`;
        }).join(' ');
        tools.innerHTML = '<a id="codex-compare" class="codex-button" href="compare.html">⇄ Compare with the game</a>'
            + '<label class="codex-toggle"><input type="checkbox" id="codex-markers"> Show the codex changes</label>'
            + `<p class="codex-legend">${legend}</p>`
            + '<p class="codex-legend">Hover over a marked item or a dotted line for the reason; click an item for the full text.</p>';
        civinfo.insertBefore(tools, civtext);
        let show = true;
        try {
            show = localStorage.getItem('codexMarkers') !== 'off';
        } catch (e) {
            // pass
        }
        const box = document.getElementById('codex-markers');
        box.checked = show;
        setMarkers(show);
        box.addEventListener('change', function () {
            setMarkers(box.checked);
        });
        updateCompareLink();
        window.addEventListener('hashchange', updateCompareLink);
        window.addEventListener('locationchange', updateCompareLink);
    }

    function addTooltip() {
        const tip = document.createElement('div');
        tip.id = 'codex-tip';
        document.body.appendChild(tip);

        function place(e) {
            const pad = 14;
            const box = tip.getBoundingClientRect();
            let x = e.clientX + pad;
            let y = e.clientY + pad;
            if (x + box.width > window.innerWidth - 8) {
                x = Math.max(8, e.clientX - box.width - pad);
            }
            if (y + box.height > window.innerHeight - 8) {
                y = Math.max(8, e.clientY - box.height - pad);
            }
            tip.style.left = x + 'px';
            tip.style.top = y + 'px';
        }

        document.addEventListener('mouseover', function (e) {
            const el = e.target.closest ? e.target.closest('[data-codex-why]') : null;
            if (!el || (el.closest('.codex-marker') && document.body.classList.contains('codex-no-markers'))) {
                tip.style.display = 'none';
                return;
            }
            tip.textContent = el.getAttribute('data-codex-why');
            tip.style.display = 'block';
            place(e);
        });
        document.addEventListener('mousemove', function (e) {
            if (tip.style.display === 'block') {
                place(e);
            }
        });
        document.addEventListener('click', function () {
            tip.style.display = 'none';
        });
    }

    function start() {
        addTools();
        addTooltip();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', start);
    } else {
        start();
    }
})();
