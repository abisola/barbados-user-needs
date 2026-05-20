/* Renders the shared admin sidebar. Each /mda/*.html page sets data-active on body. */

(function () {
  const active = document.body.getAttribute('data-active') || '';

  const nav = [
    { label: 'Overview', items: [
      { id: 'dashboard', label: 'Dashboard', href: 'dashboard.html', icon: 'grid' }
    ]},
    { label: 'Money', items: [
      { id: 'payments',       label: 'Payments',       href: 'payments.html',       icon: 'list'      },
      { id: 'reconciliation', label: 'Reconciliation', href: 'reconciliation.html', icon: 'scale'     },
      { id: 'refunds',        label: 'Refunds & disputes', href: 'refunds.html',    icon: 'refund'    },
      { id: 'reports',        label: 'Reports',        href: 'reports.html',        icon: 'chart'     }
    ]},
    { label: 'Configuration', items: [
      { id: 'services', label: 'Services & fees', href: 'services.html', icon: 'tag'   },
      { id: 'users',    label: 'Users & audit',   href: 'users.html',    icon: 'people'}
    ]}
  ];

  const icons = {
    grid:  '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    list:  '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>',
    scale: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v18"/><path d="m16 6 4 6h-8z"/><path d="m4 12 4-6 4 6z"/><path d="M2 21h20"/></svg>',
    refund:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7v6h6"/><path d="M21 17a9 9 0 0 0-15-6.7L3 13"/></svg>',
    chart: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>',
    tag:   '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.59 13.41 13.42 20.58a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>',
    people:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
  };

  const sidebar = document.createElement('aside');
  sidebar.className = 'admin-sidebar';
  sidebar.innerHTML = `
    <a href="dashboard.html" class="block" aria-label="gov.bb Pay Admin">
      <p class="brand">gov.bb Pay</p>
      <p class="brand-sub">MDA Admin · Alpha</p>
    </a>
    <div class="org">
      <p class="org-name">Barbados Licensing Authority</p>
      <p class="org-meta">MDA ID: BLA-009 · TSA sub-account ending 4421</p>
    </div>
    <nav aria-label="Admin sections">
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
      <p style="font-weight:700;">Sandra Cumberbatch</p>
      <p style="opacity:.7;">Finance Lead · BLA</p>
      <p style="margin-top:.5rem;"><a href="login.html">Sign out</a></p>
    </div>
  `;

  document.body.prepend(sidebar);
})();
