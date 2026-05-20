/* Renders the Treasury sidebar. Each /treasury/*.html page sets data-active on body. */

(function () {
  const active = document.body.getAttribute('data-active') || '';

  const nav = [
    { label: 'Overview', items: [
      { id: 'dashboard', label: 'Dashboard', href: 'dashboard.html', icon: 'grid' }
    ]},
    { label: 'Government-wide', items: [
      { id: 'mdas',           label: 'Ministries & departments', href: 'mdas.html',           icon: 'building' },
      { id: 'reconciliation', label: 'TSA reconciliation',       href: 'reconciliation.html', icon: 'scale'    },
      { id: 'reports',        label: 'Reports & exports',        href: 'reports.html',        icon: 'chart'    }
    ]},
    { label: 'Governance', items: [
      { id: 'approvals', label: 'Approvals queue', href: 'approvals.html', icon: 'shield' },
      { id: 'audit',     label: 'Audit log',       href: 'audit.html',     icon: 'log'    }
    ]}
  ];

  const icons = {
    grid:    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    building:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21h18"/><path d="M5 21V7l8-4v18"/><path d="M19 21V11l-6-4"/><path d="M9 9v.01"/><path d="M9 12v.01"/><path d="M9 15v.01"/><path d="M9 18v.01"/></svg>',
    scale:   '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v18"/><path d="m16 6 4 6h-8z"/><path d="m4 12 4-6 4 6z"/><path d="M2 21h20"/></svg>',
    chart:   '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>',
    shield:  '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    log:     '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="13" x2="15" y2="13"/><line x1="9" y1="17" x2="15" y2="17"/></svg>'
  };

  const sidebar = document.createElement('aside');
  sidebar.className = 'admin-sidebar treasury-sidebar';
  sidebar.innerHTML = `
    <a href="dashboard.html" class="block" aria-label="gov.bb Pay Treasury">
      <p class="brand" style="color:#ffc726;">gov.bb Pay</p>
      <p class="brand-sub">Treasury view · Alpha</p>
    </a>
    <div class="org" style="background:rgba(255,199,38,0.10); border-left:3px solid #ffc726;">
      <p class="org-name">Accountant General's Office</p>
      <p class="org-meta">Treasury Single Account · Government of Barbados</p>
    </div>
    <nav aria-label="Treasury sections">
      ${nav.map(section => `
        <p class="section-label">${section.label}</p>
        ${section.items.map(it => `
          <a href="${it.href}" class="${active === it.id ? 'is-active' : ''}">
            ${icons[it.icon] || ''}
            <span>${it.label}</span>
          </a>`).join('')}
      `).join('')}
    </nav>
    <div class="user">
      <p style="font-weight:700;">Ingrid Blunt</p>
      <p style="opacity:.7;">Accountant General</p>
      <p style="margin-top:.5rem;"><a href="../mda/login.html">Sign out</a></p>
    </div>
  `;

  document.body.prepend(sidebar);
})();
