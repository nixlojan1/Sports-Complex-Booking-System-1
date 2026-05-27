/* =====================================================
   EQUIPMENT CATALOG
   Add / edit categories and items here freely.
   Keys are matched against the category name
   (case-insensitive, partial match supported).
===================================================== */
const EQUIPMENT_CATALOG = {

    /* ── 1. Basketball Court ───────────────────────── */
    'basketball': [
        { id: 'bball',        name: 'Basketball (size 7)',      icon: '🏀', price: 50  },
        { id: 'bball_jr',     name: 'Basketball (size 5 – Jr)', icon: '🏀', price: 40  },
        { id: 'jersey',       name: 'Jersey (per piece)',        icon: '👕', price: 30  },
        { id: 'shorts',       name: 'Basketball Shorts',         icon: '🩳', price: 25  },
        { id: 'bball_shoes',  name: 'Basketball Shoes (pair)',   icon: '👟', price: 60  },
        { id: 'cones',        name: 'Training Cones (set of 10)',icon: '🔶', price: 20  },
        { id: 'agility_lad',  name: 'Agility Ladder',           icon: '🪜', price: 25  },
        { id: 'resist_band',  name: 'Resistance Band',           icon: '🎗️', price: 15  },
        { id: 'shot_clock',   name: 'Shot Clock / Timer',        icon: '⏱️', price: 20  },
        { id: 'scoreboard',   name: 'Portable Scoreboard',       icon: '📋', price: 15  },
        { id: 'pump',         name: 'Ball Pump',                 icon: '🔧', price: 10  },
        { id: 'mouth_guard',  name: 'Mouth Guard',               icon: '🦷', price: 10  },
    ],

    /* ── 2. Tennis Court ───────────────────────────── */
    'tennis': [
        { id: 't_racket_std', name: 'Tennis Racket – Standard',  icon: '🎾', price: 60  },
        { id: 't_racket_jr',  name: 'Tennis Racket – Junior',    icon: '🎾', price: 45  },
        { id: 't_ball_3',     name: 'Tennis Ball (tube of 3)',   icon: '🎾', price: 30  },
        { id: 't_ball_6',     name: 'Tennis Ball (tube of 6)',   icon: '🎾', price: 55  },
        { id: 't_overgrip',   name: 'Overgrip Tape',             icon: '🖐️', price: 15  },
        { id: 't_wristband',  name: 'Wristband (pair)',           icon: '🤝', price: 15  },
        { id: 't_headband',   name: 'Headband',                  icon: '🎽', price: 10  },
        { id: 't_net',        name: 'Tennis Net (spare)',         icon: '🥅', price: 50  },
        { id: 't_ball_hopper',name: 'Ball Hopper / Basket',      icon: '🧺', price: 20  },
        { id: 't_towel',      name: 'Sports Towel',              icon: '🏳️', price: 10  },
        { id: 't_visor',      name: 'Sun Visor / Cap',           icon: '🧢', price: 15  },
        { id: 't_bag',        name: 'Racket Bag',                icon: '🎒', price: 25  },
    ],

    /* ── 3. Volleyball Court ───────────────────────── */
    'volley': [
        { id: 'vball_off',    name: 'Volleyball – Official',     icon: '🏐', price: 55  },
        { id: 'vball_soft',   name: 'Volleyball – Soft Touch',   icon: '🏐', price: 45  },
        { id: 'v_net',        name: 'Volleyball Net',            icon: '🥅', price: 40  },
        { id: 'v_antenna',    name: 'Net Antenna (pair)',         icon: '📡', price: 15  },
        { id: 'knee_pads',    name: 'Knee Pads (pair)',           icon: '🦵', price: 25  },
        { id: 'elbow_pads',   name: 'Elbow Pads (pair)',          icon: '🦾', price: 20  },
        { id: 'v_jersey',     name: 'Jersey (per piece)',         icon: '👕', price: 30  },
        { id: 'v_shorts',     name: 'Volleyball Shorts',          icon: '🩳', price: 25  },
        { id: 'v_shoes',      name: 'Volleyball Shoes (pair)',    icon: '👟', price: 55  },
        { id: 'v_brace',      name: 'Ankle Brace (pair)',         icon: '🦿', price: 20  },
        { id: 'v_scoreboard', name: 'Portable Scoreboard',        icon: '📋', price: 15  },
        { id: 'v_pump',       name: 'Ball Pump',                  icon: '🔧', price: 10  },
    ],

    /* ── 4. Dart ───────────────────────────────────── */
    'dart': [
        { id: 'd_steel',      name: 'Steel-Tip Darts (set of 3)', icon: '🎯', price: 30  },
        { id: 'd_soft',       name: 'Soft-Tip Darts (set of 3)',  icon: '🎯', price: 25  },
        { id: 'd_flights',    name: 'Replacement Flights (pack)', icon: '🪁', price: 10  },
        { id: 'd_shafts',     name: 'Replacement Shafts (pack)',  icon: '🔩', price: 10  },
        { id: 'd_points',     name: 'Extra Points / Tips (pack)', icon: '📌', price: 10  },
        { id: 'd_board_steel',name: 'Bristle Dartboard (spare)',  icon: '🎯', price: 50  },
        { id: 'd_board_elec', name: 'Electronic Dartboard (spare)',icon:'🎯', price: 70  },
        { id: 'd_surround',   name: 'Dartboard Surround / Ring',  icon: '🔵', price: 20  },
        { id: 'd_mat',        name: 'Throw-Line / Oche Mat',      icon: '🟫', price: 15  },
        { id: 'd_case',       name: 'Dart Case / Wallet',         icon: '🧳', price: 15  },
        { id: 'd_chalk',      name: 'Scoreboard + Chalk',         icon: '📋', price: 10  },
        { id: 'd_cabinet',    name: 'Dart Cabinet (wall mount)',  icon: '🗄️', price: 30  },
    ],

    /* ── 5. Billiard ───────────────────────────────── */
    'billiard': [
        { id: 'bil_cue_std',  name: 'Billiard Cue – Standard',   icon: '🎱', price: 40  },
        { id: 'bil_cue_pro',  name: 'Billiard Cue – Pro Grade',  icon: '🎱', price: 70  },
        { id: 'bil_chalk',    name: 'Cue Chalk (pack of 3)',      icon: '🟦', price: 10  },
        { id: 'bil_tip_tool', name: 'Cue Tip Tool / Shaper',     icon: '🔧', price: 15  },
        { id: 'bil_glove',    name: 'Billiard Glove',             icon: '🧤', price: 15  },
        { id: 'bil_bridge',   name: 'Mechanical Bridge / Spider', icon: '🕷️', price: 20  },
        { id: 'bil_rack_tri', name: 'Triangle Rack (8-ball)',     icon: '🔺', price: 10  },
        { id: 'bil_rack_dia', name: 'Diamond Rack (9-ball)',      icon: '🔷', price: 10  },
        { id: 'bil_cover',    name: 'Table Cover / Cloth',        icon: '🟢', price: 25  },
        { id: 'bil_brush',    name: 'Table Brush',                icon: '🪣', price: 10  },
        { id: 'bil_balls',    name: 'Full Ball Set (16 pcs)',     icon: '🎱', price: 60  },
        { id: 'bil_cue_rack', name: 'Wall Cue Rack (spare)',      icon: '🗄️', price: 20  },
    ],

    /* ── Fallback ───────────────────────────────────── */
    'default': [
        { id: 'gen_towel',  name: 'Sports Towel',    icon: '🏳️', price: 10 },
        { id: 'gen_bottle', name: 'Water Bottle',    icon: '💧', price: 15 },
        { id: 'gen_bag',    name: 'Sports Bag',      icon: '🎒', price: 20 },
    ]
};

/** Returns the equipment list that best matches the given category name. */
function getEquipmentForCategory(categoryName) {
    if (!categoryName) return [];
    const key = categoryName.toLowerCase().trim();
    for (const [k, items] of Object.entries(EQUIPMENT_CATALOG)) {
        if (k === 'default') continue;
        if (key.includes(k) || k.includes(key)) return items;
    }
    return EQUIPMENT_CATALOG['default'];
}


/* =====================================================
   CATEGORY MAP  (id → display name, built from DOM)
===================================================== */
const categoryMap = {};
document.querySelectorAll('.filter-btn[data-category]').forEach(btn => {
    if (btn.dataset.category !== 'all') {
        categoryMap[btn.dataset.category] = btn.textContent.trim();
    }
});


/* =====================================================
   HERO SLIDER
===================================================== */
document.addEventListener("DOMContentLoaded", () => {

    const slides = document.querySelectorAll(".slide");
    const title  = document.getElementById("heroTitle");
    const text   = document.getElementById("heroText");
    const dotsContainer = document.getElementById("dots");

    const heroData = [
        { title: "Play. Book. Enjoy.",    text: "Reserve sports facilities quickly and easily anytime." },
        { title: "Modern Sports Booking", text: "Manage schedules and reservations in one system." },
        { title: "Easy Facility Access",  text: "Book courts and venues without hassle." }
    ];

    let index = 0;

    dotsContainer.innerHTML = "";
    for (let i = 0; i < 3; i++) {
        const dot = document.createElement("div");
        dot.classList.add("dot");
        dot.addEventListener("click", () => { index = i; update(); });
        dotsContainer.appendChild(dot);
    }

    const dots = document.querySelectorAll(".dot");

    function update() {
        slides.forEach(s => s.classList.remove("active"));
        dots.forEach(d => d.classList.remove("active"));
        slides[index].classList.add("active");
        dots[index].classList.add("active");
        title.textContent = heroData[index].title;
        text.textContent  = heroData[index].text;
    }

    function next() { index = (index + 1) % 3; update(); }

    update();
    setInterval(next, 10000);
});


/* =====================================================
   SCROLL TO HASH ON LOAD
===================================================== */
window.addEventListener("load", function () {
    if (window.location.hash) {
        const el = document.querySelector(window.location.hash);
        if (el) el.scrollIntoView({ behavior: "smooth" });
    }
});


/* =====================================================
   FACILITY FILTERS
===================================================== */
document.querySelectorAll(".filter-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        const category = btn.getAttribute("data-category");
        document.querySelectorAll(".facility-card").forEach(card => {
            card.style.display =
                (category === "all" || category === card.getAttribute("data-category"))
                ? "block" : "none";
        });
    });
});


/* =====================================================
   BOOKING MODAL — state
===================================================== */
let selectedFacilityId   = null;
let selectedCategoryName = '';
let pricePerHour         = 0;
let bookedSlots          = [];   // [{start_hour, end_hour}, ...]

/* --------------------------------------------------
   OPEN
-------------------------------------------------- */
async function openBookingModal(btn) {
    document.getElementById("bookingModal").style.display = "flex";

    selectedFacilityId = btn.dataset.id;
    pricePerHour       = parseFloat(btn.dataset.price);

    // Derive category name from the parent facility card + categoryMap
    const card           = btn.closest('.facility-card');
    const categoryId     = card ? card.dataset.category : '';
    selectedCategoryName = categoryMap[categoryId] || '';

    const today     = new Date();
    const dateInput = document.getElementById("startDate");
    dateInput.value = today.toISOString().split("T")[0];
    dateInput.min   = dateInput.value;

    // Fetch booked slots then build time pickers
    bookedSlots = await fetchBookedSlots(selectedFacilityId, dateInput.value);
    setupTime(today);

    dateInput.onchange = handleDateChange;
    document.getElementById("startTime").onchange = handleStart;
}

/* --------------------------------------------------
   FETCH BOOKED SLOTS FROM BACKEND
   Expected response: { booked_slots: [{start_hour: 9, end_hour: 11}, ...] }

   Flask route to add (only approved bookings):
   @app.route('/get_booked_slots')
   def get_booked_slots():
       facility_id = request.args.get('facility_id')
       date        = request.args.get('date')
       bookings    = Reservation.query.filter_by(
                         facility_id=facility_id,
                         booking_date=date,
                         status='approved'
                     ).all()
       slots = [{'start_hour': int(b.start_time.split(':')[0]),
                 'end_hour':   int(b.end_time.split(':')[0])}
                for b in bookings]
       return jsonify({'booked_slots': slots})
-------------------------------------------------- */
async function fetchBookedSlots(facilityId, date) {
    try {
        const res = await fetch(`/get_booked_slots?facility_id=${facilityId}&date=${date}`);
        if (!res.ok) return [];
        const data = await res.json();
        return data.booked_slots || [];
    } catch {
        return [];   // Graceful fallback — no slots blocked if endpoint is unreachable
    }
}

/* --------------------------------------------------
   HELPERS: overlap detection
-------------------------------------------------- */
/** True if `hour` falls inside any approved booking (start ≤ hour < end). */
function isHourTaken(hour) {
    return bookedSlots.some(s => hour >= s.start_hour && hour < s.end_hour);
}

/**
 * True if a booking from startHour→endHour would overlap any approved booking.
 * Uses standard interval-overlap test: A overlaps B when A.start < B.end && A.end > B.start
 */
function wouldOverlap(startHour, endHour) {
    return bookedSlots.some(s => startHour < s.end_hour && endHour > s.start_hour);
}

/* --------------------------------------------------
   DATE CHANGE  →  re-fetch slots & rebuild pickers
-------------------------------------------------- */
async function handleDateChange() {
    const selected = new Date(this.value);
    const today    = new Date();
    const isToday  = selected.toDateString() === today.toDateString();

    // Show a subtle loading state on the selects
    const startSel = document.getElementById("startTime");
    startSel.innerHTML = '<option disabled>Loading…</option>';

    bookedSlots = await fetchBookedSlots(selectedFacilityId, this.value);
    setupTime(isToday ? today : null);
}

/* --------------------------------------------------
   BUILD START-TIME PICKER
-------------------------------------------------- */
function setupTime(now) {
    const startSel = document.getElementById("startTime");
    const endSel   = document.getElementById("endTime");

    startSel.innerHTML = "";
    endSel.innerHTML   = "";
    endSel.disabled    = true;

    const currentHour = now ? now.getHours() : 8;

    for (let i = 8; i <= 22; i++) {
        if (now && i < currentHour) continue;   // past hours on today
        const taken = isHourTaken(i);
        const opt   = new Option(
            formatHour(i) + (taken ? '  — Booked' : ''),
            i
        );
        opt.disabled = taken;
        if (taken) opt.style.color = '#d1d5db';
        startSel.add(opt);
    }

    // Auto-select first available hour
    const firstAvail = Array.from(startSel.options).find(o => !o.disabled);
    if (firstAvail) startSel.value = firstAvail.value;
}

/* --------------------------------------------------
   BUILD END-TIME PICKER after start is chosen
-------------------------------------------------- */
function handleStart() {
    const startHour = parseInt(this.value);
    const endSel    = document.getElementById("endTime");

    endSel.disabled  = false;
    endSel.innerHTML = "";

    for (let i = startHour + 1; i <= 22; i++) {
        const overlaps = wouldOverlap(startHour, i);
        const opt = new Option(
            formatHour(i) + (overlaps ? '  — Unavailable' : ''),
            i
        );
        opt.disabled = overlaps;
        if (overlaps) opt.style.color = '#d1d5db';
        endSel.add(opt);

        // Once we hit a conflict, any later slot would cross it too — stop adding
        if (overlaps) break;
    }

    // Auto-select first available end hour
    const firstAvail = Array.from(endSel.options).find(o => !o.disabled);
    if (firstAvail) endSel.value = firstAvail.value;
}

/* --------------------------------------------------
   CALCULATE FACILITY COST
-------------------------------------------------- */
function calculateFacilityTotal() {
    const s = parseInt(document.getElementById("startTime").value);
    const e = parseInt(document.getElementById("endTime").value);
    if (!s || !e || e <= s) return 0;
    return (e - s) * pricePerHour;
}

/* --------------------------------------------------
   SUBMIT: validate → equipment popup → payment
-------------------------------------------------- */
function handleBookingSubmit(event) {
    event.preventDefault();

    const errorBox = document.getElementById("bookingError");
    errorBox.style.display = "none";
    errorBox.innerHTML = "";

    const bookingDate = document.getElementById("startDate").value;
    const start       = document.getElementById("startTime").value;
    const end         = document.getElementById("endTime").value;
    const purpose     = document.getElementById("purpose").value;
    const facilityTotal = calculateFacilityTotal();

    if (!start || !end || parseInt(end) <= parseInt(start)) {
        showError("Please select a valid time range.");
        return;
    }
    if (facilityTotal <= 0) {
        showError("Invalid booking duration.");
        return;
    }

    closeBookingModal();

    openEquipmentModal({
        facility_id:     selectedFacilityId,
        booking_date:    bookingDate,
        start_time:      formatHour(start),
        end_time:        formatHour(end),
        facility_total:  facilityTotal,
        purpose:         purpose
    });
}

function showError(msg) {
    const errorBox = document.getElementById("bookingError");
    errorBox.innerHTML = msg;
    errorBox.style.display = "block";
}

function closeBookingModal() {
    document.getElementById("bookingModal").style.display = "none";
}

function handleOverlayClick(event) {
    const modal = document.querySelector(".modal-container.minimal");
    if (!modal.contains(event.target)) closeBookingModal();
}


/* =====================================================
   STEP 2 — EQUIPMENT POPUP
===================================================== */
function openEquipmentModal(bookingData) {

    const items = getEquipmentForCategory(selectedCategoryName);

    // Build equipment card rows
    const rows = items.map(item => `
        <div class="eq-row" id="row_${item.id}">
            <label class="eq-label">
                <input type="checkbox"
                       class="eq-check"
                       id="chk_${item.id}"
                       data-id="${item.id}"
                       data-name="${encodeURIComponent(item.name)}"
                       data-price="${item.price}">
                <span class="eq-icon">${item.icon}</span>
                <div class="eq-info">
                    <span class="eq-name">${item.name}</span>
                    <span class="eq-price">₱${item.price} / session</span>
                </div>
            </label>
            <div class="eq-qty" id="qty_row_${item.id}" style="display:none;">
                <button type="button" class="qty-btn qty-minus" data-id="${item.id}">−</button>
                <span class="qty-val" id="qty_${item.id}">1</span>
                <button type="button" class="qty-btn qty-plus"  data-id="${item.id}">+</button>
            </div>
        </div>
    `).join('');

    const categoryLabel = selectedCategoryName
        ? `<span style="background:#ecfeff;color:#0f766e;padding:4px 12px;border-radius:999px;font-size:12px;font-weight:700;">${selectedCategoryName}</span>`
        : '';

    Swal.fire({
        title: '🏅 Borrow / Rent Equipment',
        width: 480,
        showCancelButton: true,
        confirmButtonText: 'Continue to Payment →',
        cancelButtonText:  'Skip (No Equipment)',
        confirmButtonColor: '#0f766e',
        cancelButtonColor:  '#94a3b8',
        allowOutsideClick: false,

        html: `
            <div style="font-family:'Poppins',sans-serif;text-align:left;">
                <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;">
                    ${categoryLabel}
                    <span style="font-size:12px;color:#94a3b8;">Optional — select what you need</span>
                </div>

                <div id="equipList" style="
                    max-height:280px;
                    overflow-y:auto;
                    display:flex;
                    flex-direction:column;
                    gap:8px;
                    padding-right:4px;">
                    ${rows}
                </div>

                <div style="
                    margin-top:16px;
                    padding:14px 18px;
                    background:linear-gradient(135deg,#f0fdf4,#ecfeff);
                    border-radius:14px;
                    display:flex;
                    justify-content:space-between;
                    align-items:center;">
                    <span style="font-size:13px;color:#64748b;font-weight:600;">Equipment Subtotal</span>
                    <span id="equipSubtotal" style="font-size:22px;font-weight:800;color:#0f766e;">₱0</span>
                </div>
            </div>`,

        /* Attach all interactive listeners after the popup renders */
        didOpen: () => {
            const popup = Swal.getPopup();

            // Checkbox → show/hide qty row + update total
            popup.querySelectorAll('.eq-check').forEach(cb => {
                cb.addEventListener('change', function () {
                    const qtyRow = popup.querySelector(`#qty_row_${this.dataset.id}`);
                    qtyRow.style.display = this.checked ? 'flex' : 'none';
                    refreshEquipSubtotal(popup);
                });
            });

            // +/− quantity buttons
            popup.querySelectorAll('.qty-btn').forEach(btn => {
                btn.addEventListener('click', function () {
                    const valEl = popup.querySelector(`#qty_${this.dataset.id}`);
                    let val = parseInt(valEl.textContent);
                    val = this.classList.contains('qty-plus')
                        ? Math.min(val + 1, 10)
                        : Math.max(val - 1, 1);
                    valEl.textContent = val;
                    refreshEquipSubtotal(popup);
                });
            });
        },

        /* Collect selected equipment on confirm */
        preConfirm: () => {
            const popup    = Swal.getPopup();
            const selected = [];
            popup.querySelectorAll('.eq-check:checked').forEach(cb => {
                const qty      = parseInt(popup.querySelector(`#qty_${cb.dataset.id}`).textContent);
                const price    = parseFloat(cb.dataset.price);
                selected.push({
                    id:       cb.dataset.id,
                    name:     decodeURIComponent(cb.dataset.name),
                    price,
                    quantity: qty,
                    subtotal: price * qty
                });
            });
            return selected;
        }

    }).then(result => {
        // Whether confirmed (with or without equipment) or skipped
        const equipment     = result.isConfirmed ? (result.value || []) : [];
        const equipTotal    = equipment.reduce((sum, e) => sum + e.subtotal, 0);
        const grandTotal    = bookingData.facility_total + equipTotal;
        const depositAmount = grandTotal * 0.30;

        openPaymentModal({
            ...bookingData,
            equipment,
            equip_total:    equipTotal,
            total_amount:   grandTotal,
            deposit_amount: depositAmount
        });
    });
}

/** Recalculates and updates the equipment subtotal label. */
function refreshEquipSubtotal(popup) {
    let total = 0;
    popup.querySelectorAll('.eq-check:checked').forEach(cb => {
        const qty   = parseInt(popup.querySelector(`#qty_${cb.dataset.id}`).textContent);
        total += parseFloat(cb.dataset.price) * qty;
    });
    popup.querySelector('#equipSubtotal').textContent = '₱' + total.toLocaleString();
}


/* =====================================================
   STEP 3 — PAYMENT FLOW (GCASH)
===================================================== */
function openPaymentModal(bookingData) {

    let savedRef  = "";
    let savedFile = null;

    // Build equipment summary lines for the payment breakdown
    function buildEquipLines() {
        if (!bookingData.equipment || bookingData.equipment.length === 0) return '';
        const lines = bookingData.equipment.map(e =>
            `<p style="margin:2px 0;font-size:13px;">
                &nbsp;&nbsp;• ${e.name} × ${e.quantity}
                <span style="float:right;">₱${e.subtotal}</span>
            </p>`
        ).join('');
        return `
            <p style="margin-top:8px;font-weight:700;font-size:13px;">Equipment:</p>
            ${lines}
            <p style="font-size:13px;margin-top:4px;">
                Equipment Subtotal
                <span style="float:right;">₱${bookingData.equip_total}</span>
            </p>
            <hr style="border:none;border-top:1px dashed #cbd5e1;margin:8px 0;">`;
    }

    // ── Step 1: GCash QR + breakdown ──────────────────
    function step1() {
        Swal.fire({
            title: '💳 GCash Payment',
            width: 460,
            showCancelButton: true,
            confirmButtonText: 'I have paid →',
            cancelButtonText:  '← Back',
            confirmButtonColor: '#0f766e',
            cancelButtonColor:  '#94a3b8',
            allowOutsideClick: false,
            html: `
                <div style="font-family:'Poppins',sans-serif;text-align:center;">

                    <div style="background:#f8f9fb;padding:18px;border-radius:14px;margin-bottom:16px;">
                        <img src="/static/images/qr.png"
                             style="width:170px;height:170px;border-radius:12px;object-fit:cover;">
                        <p style="font-size:12px;color:#94a3b8;margin-top:8px;">Scan using GCash app</p>
                    </div>

                    <div style="text-align:left;font-size:14px;background:#fff;
                                border:1px solid #e2e8f0;padding:14px;border-radius:12px;margin-bottom:12px;">
                        <p><b>GCash Name:</b> Sports Complex</p>
                        <p style="margin-top:4px;"><b>GCash No.:</b> 09464217995</p>
                    </div>

                    <div style="text-align:left;background:linear-gradient(135deg,#f0fdf4,#ecfeff);
                                padding:14px;border-radius:12px;">
                        <p style="font-size:13px;">
                            Facility Fee
                            <span style="float:right;">₱${bookingData.facility_total}</span>
                        </p>
                        ${buildEquipLines()}
                        <p style="font-weight:800;font-size:16px;margin-top:4px;">
                            Grand Total
                            <span style="float:right;color:#0f766e;">₱${bookingData.total_amount}</span>
                        </p>
                        <p style="font-size:13px;color:#64748b;margin-top:4px;">
                            Deposit Due (30%)
                            <span style="float:right;font-weight:700;color:#0f766e;">
                                ₱${bookingData.deposit_amount.toFixed(2)}
                            </span>
                        </p>
                    </div>

                </div>`
        }).then(res => {
            if (res.isConfirmed) step2();
        });
    }

    // ── Step 2: Reference number + screenshot ─────────
    function step2() {
        Swal.fire({
            title: '🧾 Confirm Payment',
            width: 430,
            showCancelButton: true,
            confirmButtonText: 'Submit Booking ✓',
            cancelButtonText:  '← Back',
            confirmButtonColor: '#0f766e',
            cancelButtonColor:  '#94a3b8',
            allowOutsideClick: false,
            html: `
                <div style="font-family:'Poppins',sans-serif;text-align:left;">
                    <label style="font-size:13px;font-weight:600;display:block;margin-bottom:6px;">
                        GCash Reference Number
                    </label>
                    <input id="gcashRef"
                           placeholder="e.g. 1234567890"
                           value="${savedRef}"
                           style="width:100%;padding:11px 14px;border-radius:10px;
                                  border:1px solid #dbe4ee;font-size:14px;margin-bottom:14px;">

                    <label style="font-size:13px;font-weight:600;display:block;margin-bottom:6px;">
                        Upload Payment Screenshot
                    </label>
                    <input id="gcashReceipt"
                           type="file"
                           accept="image/*"
                           style="width:100%;padding:9px;border-radius:10px;border:1px solid #dbe4ee;">
                </div>`,

            preConfirm: () => {
                const ref  = document.getElementById("gcashRef").value.trim();
                const file = document.getElementById("gcashReceipt").files[0];
                if (!ref)  { Swal.showValidationMessage("Reference number is required."); return false; }
                if (!file) { Swal.showValidationMessage("Please attach a payment screenshot."); return false; }
                savedRef  = ref;
                savedFile = file;
                return true;
            }

        }).then(async res => {

            if (res.isConfirmed) {
                const formData = new FormData();
                formData.append("facility_id",       bookingData.facility_id);
                formData.append("booking_date",       bookingData.booking_date);
                formData.append("start_time",         bookingData.start_time);
                formData.append("end_time",           bookingData.end_time);
                formData.append("total_amount",       bookingData.total_amount);
                formData.append("deposit_amount",     bookingData.deposit_amount);
                formData.append("purpose",            bookingData.purpose);
                formData.append("gcash_reference",    savedRef);
                formData.append("payment_screenshot", savedFile);

                // Equipment as JSON string so Flask can parse it
                formData.append("equipment", JSON.stringify(bookingData.equipment || []));

                try {
                    const response = await fetch("/create_reservation", { method: "POST", body: formData });
                    const data     = await response.json();

                    if (data.status === "success") {
                        Swal.fire({
                            icon: "success",
                            title: "Booking Submitted! 🎉",
                            text: "Your reservation is awaiting admin approval.",
                            confirmButtonColor: "#0f766e"
                        });
                    } else {
                        Swal.fire({
                            icon: "error",
                            title: "Booking Failed",
                            text: data.message || "Something went wrong."
                        });
                    }
                } catch (err) {
                    Swal.fire({ icon: "error", title: "Server Error", text: "Unable to submit reservation." });
                    console.error(err);
                }
            }

            if (res.dismiss === Swal.DismissReason.cancel) step1();
        });
    }

    step1();
}


/* =====================================================
   CONTACT FORM
===================================================== */
function sendInquiry() {
    const name    = document.getElementById("name").value;
    const email   = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    if (!name || !email || !message) {
        Swal.fire("Error", "All fields are required!", "error");
        return;
    }

    fetch("/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, message })
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === "success") {
            Swal.fire("Success", "Inquiry sent successfully!", "success");
            document.getElementById("name").value    = "";
            document.getElementById("email").value   = "";
            document.getElementById("message").value = "";
        } else {
            Swal.fire("Error", data.message, "error");
        }
    })
    .catch(() => Swal.fire("Error", "Server error occurred!", "error"));
}


/* =====================================================
   CHATBOT
===================================================== */
let chatbotOpen = false;

function toggleChatbot() {
    const popup   = document.getElementById("chatbotPopup");
    const fabIcon = document.getElementById("fabIcon");
    chatbotOpen = !chatbotOpen;

    if (chatbotOpen) {
        popup.style.display = "flex";
        setTimeout(() => popup.classList.add("open"), 10);
        fabIcon.className = "fas fa-times";
        document.getElementById("popupChatInput").focus();
    } else {
        popup.classList.remove("open");
        fabIcon.className = "fas fa-robot";
        setTimeout(() => { popup.style.display = "none"; }, 300);
    }
}

async function sendPopupMessage() {
    const input   = document.getElementById("popupChatInput");
    const message = input.value.trim();
    if (!message) return;

    const chat = document.getElementById("popupChatMessages");

    const userDiv = document.createElement("div");
    userDiv.className   = "user-msg";
    userDiv.textContent = message;
    chat.appendChild(userDiv);
    input.value = "";
    chat.scrollTop = chat.scrollHeight;

    const typingDiv = document.createElement("div");
    typingDiv.className = "typing-indicator";
    typingDiv.innerHTML = "<span></span><span></span><span></span>";
    chat.appendChild(typingDiv);
    chat.scrollTop = chat.scrollHeight;

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });
        const data = await response.json();
        chat.removeChild(typingDiv);

        const botDiv = document.createElement("div");
        botDiv.className = "bot-msg";
        botDiv.innerHTML = data.response.replace(/\n/g, "<br>");
        chat.appendChild(botDiv);
    } catch {
        chat.removeChild(typingDiv);
        const errDiv = document.createElement("div");
        errDiv.className   = "bot-msg";
        errDiv.textContent = "⚠️ Server error. Please try again later.";
        chat.appendChild(errDiv);
    }

    chat.scrollTop = chat.scrollHeight;
}

document.getElementById("popupChatInput").addEventListener("keypress", function (e) {
    if (e.key === "Enter") sendPopupMessage();
});


/* =====================================================
   LOGOUT CONFIRMATION
===================================================== */
const logoutBtn = document.getElementById("logoutBtn");
if (logoutBtn) {
    logoutBtn.addEventListener("click", function (e) {
        e.preventDefault();
        const logoutUrl = this.href;
        Swal.fire({
            title: "Logout?",
            text: "Are you sure you want to logout?",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Yes, Logout",
            cancelButtonText:  "Cancel"
        }).then(result => {
            if (result.isConfirmed) window.location.href = logoutUrl;
        });
    });
}


/* =====================================================
   HELPERS
===================================================== */
/** Converts an integer hour (8–22) to "8:00 AM" / "1:00 PM" format. */
function formatHour(h) {
    h = parseInt(h);
    const ampm = h >= 12 ? "PM" : "AM";
    const hour = h % 12 || 12;
    return `${hour}:00 ${ampm}`;
}


/* =====================================================
   EQUIPMENT POPUP — inline CSS injected once
   (Keeps all equipment styles self-contained in JS
    so style.css stays untouched)
===================================================== */
(function injectEquipStyles() {
    const style = document.createElement('style');
    style.textContent = `
        .eq-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 12px 14px;
            transition: border-color .2s, background .2s;
        }
        .eq-row:has(.eq-check:checked) {
            background: #f0fdf4;
            border-color: #14b8a6;
        }
        .eq-label {
            display: flex;
            align-items: center;
            gap: 12px;
            cursor: pointer;
            flex: 1;
            min-width: 0;
        }
        .eq-label input[type="checkbox"] {
            width: 17px;
            height: 17px;
            accent-color: #0f766e;
            cursor: pointer;
            flex-shrink: 0;
            margin: 0;
            padding: 0;
            border: none;
        }
        .eq-icon   { font-size: 24px; flex-shrink: 0; }
        .eq-info   { display: flex; flex-direction: column; min-width: 0; }
        .eq-name   { font-size: 14px; font-weight: 600; color: #0f172a; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .eq-price  { font-size: 12px; color: #0f766e; font-weight: 600; }
        .eq-qty    {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-left: 12px;
            flex-shrink: 0;
        }
        .qty-btn {
            width: 28px; height: 28px;
            border-radius: 8px;
            border: 1px solid #14b8a6;
            background: white;
            color: #0f766e;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            display: flex; align-items: center; justify-content: center;
            transition: background .15s;
        }
        .qty-btn:hover { background: #14b8a6; color: white; }
        .qty-val { font-size: 15px; font-weight: 700; color: #0f172a; min-width: 18px; text-align: center; }

        /* Scrollbar for equipment list */
        #equipList::-webkit-scrollbar       { width: 4px; }
        #equipList::-webkit-scrollbar-thumb { background: #d1d5db; border-radius: 4px; }
    `;
    document.head.appendChild(style);
})();