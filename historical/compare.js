// aoe2-codex compare page: the codex tree (left) and the game's tree (right) for the same civ,
// in two frames of the site's own pages, with their sidebars hidden and their scrolling linked.
(function () {
    'use strict';

    const FRAME_STYLE = '#metainfo { display: none !important; } '
        + '#techtree { width: 100vw !important; border-left: none !important; }';

    const select = document.getElementById('compare-civ');
    const sync = document.getElementById('compare-sync');
    const textsBox = document.getElementById('compare-texts');
    const textsPanel = document.getElementById('compare-texts-panel');
    const back = document.getElementById('compare-back');
    const frames = {codex: document.getElementById('pane-codex'), game: document.getElementById('pane-game')};
    const search = window.location.search;
    let civ = decodeURIComponent(window.location.hash.substring(1));
    let locked = false;

    function doc(frame) {
        try {
            return frame.contentDocument;
        } catch (e) {
            return null;
        }
    }

    function techtree(frame) {
        const d = doc(frame);
        return d ? d.getElementById('techtree') : null;
    }

    function setCiv(name) {
        civ = name;
        for (const frame of Object.values(frames)) {
            if (frame.contentWindow && doc(frame)) {
                frame.contentWindow.location.hash = name;
            }
        }
        history.replaceState(null, '', search + '#' + name);
        back.href = 'index.html' + search + '#' + name;
    }

    function copyText(frame, target) {
        const d = doc(frame);
        const source = d ? d.getElementById('civtext') : null;
        if (!source) {
            return;
        }
        target.innerHTML = source.innerHTML;
        target.querySelectorAll('[data-codex-why]').forEach(function (el) {
            el.title = el.getAttribute('data-codex-why');
        });
    }

    function fillSelect(codexSelect) {
        const options = Array.from(codexSelect.options).filter(function (o) {
            return o.value && o.value !== 'Loading…';
        });
        if (!options.length) {
            return false;
        }
        select.innerHTML = '';
        for (const o of options) {
            const option = document.createElement('option');
            option.value = o.value;
            option.textContent = o.textContent;
            select.appendChild(option);
        }
        select.value = civ || codexSelect.value;
        if (!civ) {
            setCiv(select.value);
        }
        return true;
    }

    function prepare(name) {
        const frame = frames[name];
        const d = doc(frame);
        if (!d) {
            return;
        }
        const style = d.createElement('style');
        style.textContent = FRAME_STYLE;
        d.head.appendChild(style);
        const tree = d.getElementById('techtree');
        const other = frames[name === 'codex' ? 'game' : 'codex'];
        tree.addEventListener('scroll', function () {
            const target = techtree(other);
            if (!sync.checked || locked || !target) {
                return;
            }
            locked = true;
            target.scrollLeft = tree.scrollLeft;
            requestAnimationFrame(function () {
                locked = false;
            });
        });
        const civtext = d.getElementById('civtext');
        const target = document.getElementById(name === 'codex' ? 'text-codex' : 'text-game');
        new MutationObserver(function () {
            copyText(frame, target);
        }).observe(civtext, {childList: true, subtree: true, characterData: true});
        copyText(frame, target);
        if (name === 'codex') {
            const codexSelect = d.getElementById('civselect');
            if (!fillSelect(codexSelect)) {
                const watcher = new MutationObserver(function () {
                    if (fillSelect(codexSelect)) {
                        watcher.disconnect();
                    }
                });
                watcher.observe(codexSelect, {childList: true});
            }
        }
    }

    function redraw() {
        for (const frame of Object.values(frames)) {
            if (frame.contentWindow && typeof frame.contentWindow.loadCiv === 'function') {
                frame.contentWindow.loadCiv();
            }
        }
    }

    frames.codex.addEventListener('load', function () {
        prepare('codex');
    });
    frames.game.addEventListener('load', function () {
        prepare('game');
    });
    frames.codex.src = 'index.html' + search + (civ ? '#' + civ : '');
    frames.game.src = '../index.html' + search + (civ ? '#' + civ : '');
    back.href = 'index.html' + search + (civ ? '#' + civ : '');

    select.addEventListener('change', function () {
        setCiv(select.value);
    });
    textsBox.addEventListener('change', function () {
        textsPanel.hidden = !textsBox.checked;
        // The trees size themselves to their frame's height when drawn, so draw them again.
        requestAnimationFrame(redraw);
    });
    window.addEventListener('hashchange', function () {
        const name = decodeURIComponent(window.location.hash.substring(1));
        if (name && name !== civ) {
            select.value = name;
            setCiv(name);
        }
    });
})();
