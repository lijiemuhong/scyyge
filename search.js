(function () {
  'use strict';

  function isSearchPage() {
    return /(^|\/)search\.html$/i.test((window.location && window.location.pathname) || '');
  }

  function normalizeQuery(raw) {
    var q = (raw == null ? '' : String(raw));
    q = q.replace(/^\s+|\s+$/g, '');
    if (q === '' || q.toLowerCase() === 'search...') return '';
    return q;
  }

  function findQueryInput(form) {
    if (!form || !form.querySelector) return null;
    return form.querySelector('input[name="q"]') || form.querySelector('input[type="search"]') || form.querySelector('input[type="text"]');
  }

  function actionLooksLikeSearchHtml(action) {
    if (!action) return false;
    return /search\.html(\?|#|$)/i.test(action);
  }

  if (isSearchPage()) return;

  var forms = document.getElementsByTagName('form');
  for (var i = 0; i < forms.length; i++) {
    (function (form) {
      var action = form.getAttribute('action') || '';
      if (!actionLooksLikeSearchHtml(action)) return;

      form.addEventListener('submit', function (e) {
        var input = findQueryInput(form);
        var q = normalizeQuery(input ? input.value : '');
        if (!q) {
          if (e && e.preventDefault) e.preventDefault();
          if (input && input.focus) input.focus();
          return false;
        }

        var base = action.split('?')[0];
        var url = base + '?q=' + encodeURIComponent(q);
        if (e && e.preventDefault) e.preventDefault();
        window.location.href = url;
        return false;
      });
    })(forms[i]);
  }
})();
