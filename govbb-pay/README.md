# gov.bb Pay – prototype

A clickable prototype for a central payment service for the Government of Barbados. Modelled on GOV.UK Pay, dressed in the alpha.gov.bb design system.

## How to view

Open `index.html` in a browser. The prototype is fully static – no server is required, but using a local server (e.g. `python3 -m http.server 8000`) avoids any `file://` quirks.

Three entry points from the index:

1. **Citizen flow** – pay for a government service end-to-end.
2. **MDA admin** – the per-MDA reconciliation and back-office dashboard.
3. **Treasury view** – the Accountant General's cross-government view of the TSA.

## Citizen flow

1. `pay.html` – category page listing the services that take payment.
2. `licence-renewal.html` – service guide for the example service (driver's licence renewal).
3. `application-id.html` → `application-licence.html` → `application-check.html` – three-step application using Trident ID for identity.
4. `payment.html` – payment page with two clear options: debit/credit card or BimPay. Switching method changes the form and the primary button.
5. `payment-bimpay.html` – mocked "approve in BimPay app" step (mobile number + QR option).
6. `payment-success.html` – tracking ID, receipt, and what-happens-next.

## MDA admin (gov.bb Pay Admin)

1. `mda/login.html` – staff sign-in.
2. `mda/dashboard.html` – today at a glance, revenue trend, recent activity, next settlement, alerts.
3. `mda/payments.html` – searchable, filterable payments list with bulk actions and CSV/PDF export.
4. `mda/payment-detail.html` – single payment with full event timeline, settlement state, refund/dispute actions.
5. `mda/reconciliation.html` – daily settlement against the Treasury Single Account (TSA) sub-account. Discrepancy alerts, settlement waterfall, batch history.
6. `mda/refunds.html` – refunds with approval workflow, plus disputes/chargebacks tab.
7. `mda/services.html` – MDA configures its services, fees, and settlement accounts. Fee changes go to Treasury for approval.
8. `mda/users.html` – users, role permissions, and full audit log.
9. `mda/reports.html` – pre-built reports (monthly revenue, TSA pack, channel mix, fraud) with scheduled exports.

## Treasury view (Accountant General's Office)

1. `treasury/dashboard.html` – government-wide hero numbers (today, MTD, YTD, TSA balance), 30-day collection trend, channel mix, top MDAs by collection, approvals snapshot.
2. `treasury/mdas.html` – every MDA collecting through gov.bb Pay (14 in this prototype) with sub-account balance, MTD gross, and reconciliation health. Drills into a specific MDA's admin view.
3. `treasury/reconciliation.html` – cross-MDA settlement of the TSA: open discrepancies, the next settlement waterfall, top MDAs by net to TSA, and recent settlement batches.
4. `treasury/approvals.html` – queue of MDA fee-change, new-service and onboarding requests awaiting Treasury approval, with an inline review panel.
5. `treasury/audit.html` – government-wide audit log across all MDA admins and Treasury actions.
6. `treasury/reports.html` – cross-government reports (Cabinet briefing, Auditor General pack, consolidated revenue) and scheduled exports.

Distinguished from the MDA admin by a gold accent throughout. The Treasury sidebar also points to the same login flow; sign-out drops back to the MDA login (where there's a one-click link back into the Treasury view).

## Design notes

- Built on the GovBB design tokens (Figtree font, `bb-*` colour palette, alpha banner, official banner, footer).
- The citizen pages follow alpha.gov.bb page chrome and patterns. The MDA admin is a sibling product – it borrows the colour palette but uses a data-dense sidebar layout suited to back-office work.
- BimPay is treated as a first-class payment option on a single page, the way Stripe/PayPal toggles work. No separate detour page before the payment form.
- All data is mocked. No payments are taken. Forms do not persist anywhere.

## What's deliberately out of scope

- Service-specific application questions beyond the licence-renewal example.
- Real OAuth/Trident ID for Staff – the MDA sign-in advances straight to the dashboard.
- Server-side persistence – everything is static HTML + a small amount of JavaScript.
