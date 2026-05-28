/* =====================================================
   EQUIPMENT CATALOG
   Keys matched case-insensitively / partially against
   the facility's category name.
===================================================== */
const EQUIPMENT_CATALOG = {

    'basketball': [
        { id: 'bball',        name: 'Basketball (size 7)',       icon: '🏀', price: 50 },
        { id: 'bball_jr',     name: 'Basketball (size 5 – Jr)',  icon: '🏀', price: 40 },
        { id: 'jersey',       name: 'Jersey (per piece)',         icon: '👕', price: 30 },
        { id: 'shorts',       name: 'Basketball Shorts',          icon: '🩳', price: 25 },
        { id: 'bball_shoes',  name: 'Basketball Shoes (pair)',    icon: '👟', price: 60 },
        { id: 'cones',        name: 'Training Cones (set of 10)', icon: '🔶', price: 20 },
        { id: 'agility_lad',  name: 'Agility Ladder',            icon: '🪜', price: 25 },
        { id: 'resist_band',  name: 'Resistance Band',            icon: '🎗️', price: 15 },
        { id: 'shot_clock',   name: 'Shot Clock / Timer',         icon: '⏱️', price: 20 },
        { id: 'scoreboard',   name: 'Portable Scoreboard',        icon: '📋', price: 15 },
        { id: 'pump',         name: 'Ball Pump',                  icon: '🔧', price: 10 },
        { id: 'mouth_guard',  name: 'Mouth Guard',                icon: '🦷', price: 10 },
    ],

    'tennis': [
        { id: 't_racket_std', name: 'Tennis Racket – Standard',  icon: '🎾', price: 60 },
        { id: 't_racket_jr',  name: 'Tennis Racket – Junior',    icon: '🎾', price: 45 },
        { id: 't_ball_3',     name: 'Tennis Ball (tube of 3)',    icon: '🎾', price: 30 },
        { id: 't_ball_6',     name: 'Tennis Ball (tube of 6)',    icon: '🎾', price: 55 },
        { id: 't_overgrip',   name: 'Overgrip Tape',              icon: '🖐️', price: 15 },
        { id: 't_wristband',  name: 'Wristband (pair)',            icon: '🤝', price: 15 },
        { id: 't_headband',   name: 'Headband',                   icon: '🎽', price: 10 },
        { id: 't_net',        name: 'Tennis Net (spare)',          icon: '🥅', price: 50 },
        { id: 't_ball_hopper',name: 'Ball Hopper / Basket',       icon: '🧺', price: 20 },
        { id: 't_towel',      name: 'Sports Towel',               icon: '🏳️', price: 10 },
        { id: 't_visor',      name: 'Sun Visor / Cap',            icon: '🧢', price: 15 },
        { id: 't_bag',        name: 'Racket Bag',                 icon: '🎒', price: 25 },
    ],

    'volley': [
        { id: 'vball_off',    name: 'Volleyball – Official',      icon: '🏐', price: 55 },
        { id: 'vball_soft',   name: 'Volleyball – Soft Touch',    icon: '🏐', price: 45 },
        { id: 'v_net',        name: 'Volleyball Net',             icon: '🥅', price: 40 },
        { id: 'v_antenna',    name: 'Net Antenna (pair)',          icon: '📡', price: 15 },
        { id: 'knee_pads',    name: 'Knee Pads (pair)',            icon: '🦵', price: 25 },
        { id: 'elbow_pads',   name: 'Elbow Pads (pair)',           icon: '🦾', price: 20 },
        { id: 'v_jersey',     name: 'Jersey (per piece)',          icon: '👕', price: 30 },
        { id: 'v_shorts',     name: 'Volleyball Shorts',           icon: '🩳', price: 25 },
        { id: 'v_shoes',      name: 'Volleyball Shoes (pair)',     icon: '👟', price: 55 },
        { id: 'v_brace',      name: 'Ankle Brace (pair)',          icon: '🦿', price: 20 },
        { id: 'v_scoreboard', name: 'Portable Scoreboard',         icon: '📋', price: 15 },
        { id: 'v_pump',       name: 'Ball Pump',                   icon: '🔧', price: 10 },
    ],

    'dart': [
        { id: 'd_steel',       name: 'Steel-Tip Darts (set of 3)', icon: '🎯', price: 30 },
        { id: 'd_soft',        name: 'Soft-Tip Darts (set of 3)',  icon: '🎯', price: 25 },
        { id: 'd_flights',     name: 'Replacement Flights (pack)', icon: '🪁', price: 10 },
        { id: 'd_shafts',      name: 'Replacement Shafts (pack)',  icon: '🔩', price: 10 },
        { id: 'd_points',      name: 'Extra Points / Tips (pack)', icon: '📌', price: 10 },
        { id: 'd_board_steel', name: 'Bristle Dartboard (spare)',  icon: '🎯', price: 50 },
        { id: 'd_board_elec',  name: 'Electronic Dartboard',       icon: '🎯', price: 70 },
        { id: 'd_surround',    name: 'Dartboard Surround / Ring',  icon: '🔵', price: 20 },
        { id: 'd_mat',         name: 'Throw-Line / Oche Mat',      icon: '🟫', price: 15 },
        { id: 'd_case',        name: 'Dart Case / Wallet',         icon: '🧳', price: 15 },
        { id: 'd_chalk',       name: 'Scoreboard + Chalk',         icon: '📋', price: 10 },
        { id: 'd_cabinet',     name: 'Dart Cabinet (wall mount)',  icon: '🗄️', price: 30 },
    ],

    'billiard': [
        { id: 'bil_cue_std',  name: 'Billiard Cue – Standard',    icon: '🎱', price: 40 },
        { id: 'bil_cue_pro',  name: 'Billiard Cue – Pro Grade',   icon: '🎱', price: 70 },
        { id: 'bil_chalk',    name: 'Cue Chalk (pack of 3)',       icon: '🟦', price: 10 },
        { id: 'bil_tip_tool', name: 'Cue Tip Tool / Shaper',      icon: '🔧', price: 15 },
        { id: 'bil_glove',    name: 'Billiard Glove',              icon: '🧤', price: 15 },
        { id: 'bil_bridge',   name: 'Mechanical Bridge / Spider',  icon: '🕷️', price: 20 },
        { id: 'bil_rack_tri', name: 'Triangle Rack (8-ball)',      icon: '🔺', price: 10 },
        { id: 'bil_rack_dia', name: 'Diamond Rack (9-ball)',       icon: '🔷', price: 10 },
        { id: 'bil_cover',    name: 'Table Cover / Cloth',         icon: '🟢', price: 25 },
        { id: 'bil_brush',    name: 'Table Brush',                 icon: '🪣', price: 10 },
        { id: 'bil_balls',    name: 'Full Ball Set (16 pcs)',      icon: '🎱', price: 60 },
        { id: 'bil_cue_rack', name: 'Wall Cue Rack (spare)',       icon: '🗄️', price: 20 },
    ],

    'default': [
        { id: 'gen_towel',  name: 'Sports Towel',  icon: '🏳️', price: 10 },
        { id: 'gen_bottle', name: 'Water Bottle',  icon: '💧',  price: 15 },
        { id: 'gen_bag',    name: 'Sports Bag',    icon: '🎒',  price: 20 },
    ]
};

function getEquipmentForCategory(categoryName) {
    if (!categoryName) return EQUIPMENT_CATALOG['default'];
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
    const slides        = document.querySelectorAll(".slide");
    const titleEl       = document.getElementById("heroTitle");
    const textEl        = document.getElementById("heroText");
    const dotsContainer = document.getElementById("dots");

    const heroData = [
        { title: "Play. Book. Enjoy.",    text: "Reserve sports facilities quickly and easily anytime." },
        { title: "Modern Sports Booking", text: "Manage schedules and reservations in one system."       },
        { title: "Easy Facility Access",  text: "Book courts and venues without hassle."                 }
    ];

    let idx = 0;

    dotsContainer.innerHTML = "";
    for (let i = 0; i < 3; i++) {
        const d = document.createElement("div");
        d.classList.add("dot");
        d.addEventListener("click", () => { idx = i; updateHero(); });
        dotsContainer.appendChild(d);
    }
    const dots = document.querySelectorAll(".dot");

    function updateHero() {
        slides.forEach(s => s.classList.remove("active"));
        dots.forEach(d => d.classList.remove("active"));
        slides[idx].classList.add("active");
        dots[idx].classList.add("active");
        titleEl.textContent = heroData[idx].title;
        textEl.textContent  = heroData[idx].text;
    }

    updateHero();
    setInterval(() => { idx = (idx + 1) % 3; updateHero(); }, 10000);
});


/* =====================================================
   SCROLL TO HASH ON LOAD
===================================================== */
window.addEventListener("load", () => {
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
        const cat = btn.getAttribute("data-category");
        document.querySelectorAll(".facility-card").forEach(card => {
            card.style.display =
                (cat === "all" || cat === card.getAttribute("data-category")) ? "block" : "none";
        });
    });
});


/* =====================================================
   BOOKING MODAL — STATE
===================================================== */
let selectedFacilityId   = null;
let selectedCategoryName = '';
let pricePerHour         = 0;
let bookedSlots          = [];    // [{start_hour, end_hour}, ...]
let slotStart            = null;  // selected start hour (int)
let slotEnd              = null;  // selected end hour   (int, exclusive — booking ends here)
let selStep              = 'start'; // 'start' | 'end'
let pollingTimer         = null;  // setInterval handle for real-time refresh
let isSubmitting         = false; // double-submit guard

// ── VALIDATION CONSTANTS ───────────────────────────
const MIN_BOOKING_HOURS  = 1;
const MAX_BOOKING_HOURS  = 8;
const MAX_DAYS_AHEAD     = 60;   // how far in the future a user can book
const OPEN_HOUR          = 8;    // facility opens  08:00
const CLOSE_HOUR         = 22;   // facility closes 22:00
const POLL_INTERVAL_MS   = 30000; // 30-second live refresh


/* ── OPEN BOOKING MODAL ─────────────────────────── */
async function openBookingModal(btn) {
    // Reset state
    slotStart    = null;
    slotEnd      = null;
    selStep      = 'start';
    bookedSlots  = [];
    isSubmitting = false;

    selectedFacilityId   = btn.dataset.id;
    pricePerHour         = parseFloat(btn.dataset.price);
    const card           = btn.closest('.facility-card');
    const categoryId     = card ? card.dataset.category : '';
    selectedCategoryName = categoryMap[categoryId] || '';

    // Date limits
    const today    = new Date();
    const maxDate  = new Date(today);
    maxDate.setDate(maxDate.getDate() + MAX_DAYS_AHEAD);

    const dateInput  = document.getElementById("startDate");
    dateInput.value  = today.toISOString().split("T")[0];
    dateInput.min    = today.toISOString().split("T")[0];
    dateInput.max    = maxDate.toISOString().split("T")[0];

    clearField('dateError');
    clearField('bookingError');
    document.getElementById("purpose").value = "";
    setSubmitBtn(false);
    hideSummary();
    showHint('start');

    // Show modal
    document.getElementById("bookingModal").style.display = "flex";

    // Load initial slots
    await refreshSlots(dateInput.value);

    // Attach events
    dateInput.onchange = onDateChange;

    // Start live polling
    stopPolling();
    pollingTimer = setInterval(() => liveRefresh(), POLL_INTERVAL_MS);
}


/* ── DATE CHANGE ────────────────────────────────── */
async function onDateChange() {
    const val = this.value;

    clearField('dateError');

    // Date validation
    const chosen  = new Date(val + "T00:00:00");
    const today   = new Date(); today.setHours(0,0,0,0);
    const maxDate = new Date(today); maxDate.setDate(today.getDate() + MAX_DAYS_AHEAD);

    if (chosen < today) {
        setFieldError('dateError', 'Cannot book a past date.');
        return;
    }
    if (chosen > maxDate) {
        setFieldError('dateError', `Bookings only available up to ${MAX_DAYS_AHEAD} days ahead.`);
        return;
    }

    // Reset time selection when date changes
    slotStart = null;
    slotEnd   = null;
    selStep   = 'start';
    setSubmitBtn(false);
    hideSummary();
    showHint('start');

    await refreshSlots(val);
}


/* ── FETCH BOOKED SLOTS ─────────────────────────── */
async function fetchBookedSlots(facilityId, date) {
    try {
        const res = await fetch(`/get_booked_slots?facility_id=${facilityId}&date=${date}`);
        if (!res.ok) return [];
        const data = await res.json();
        return Array.isArray(data.booked_slots) ? data.booked_slots : [];
    } catch {
        return [];
    }
}


/* ── SHOW LOADER / RENDER GRID ──────────────────── */
async function refreshSlots(date) {
    showGridLoader(true);
    bookedSlots = await fetchBookedSlots(selectedFacilityId, date);
    showGridLoader(false);
    renderGrid(date);
}


/* ── LIVE REFRESH (polling) ─────────────────────── */
async function liveRefresh() {
    const date  = document.getElementById("startDate").value;
    const fresh = await fetchBookedSlots(selectedFacilityId, date);

    const changed = JSON.stringify(fresh) !== JSON.stringify(bookedSlots);
    if (!changed) return;

    bookedSlots = fresh;

    // Check if current selection was invalidated by someone else booking
    if (slotStart !== null && slotEnd !== null) {
        if (rangeHasConflict(slotStart, slotEnd)) {
            slotStart = null;
            slotEnd   = null;
            selStep   = 'start';
            setSubmitBtn(false);
            hideSummary();
            showHint('start');
            showError('⚠️ A slot you had selected was just booked by someone else. Please choose a new time.');
        }
    }

    renderGrid(date);
}


/* ── STOP POLLING ───────────────────────────────── */
function stopPolling() {
    if (pollingTimer) { clearInterval(pollingTimer); pollingTimer = null; }
}


/* ── RENDER TIME GRID ───────────────────────────── */
function renderGrid(date) {
    const grid = document.getElementById("timeGrid");
    const now  = new Date();
    const isToday = (date === now.toISOString().split("T")[0]);
    const currentHour = now.getHours();

    let html = '';

    // Slots = HOUR BLOCKS  8-9, 9-10, … 21-22  (start hours 8..21)
    for (let h = OPEN_HOUR; h < CLOSE_HOUR; h++) {

        const isPast   = isToday && h < currentHour;
        const isBooked = bookedSlots.some(s => h >= s.start_hour && h < s.end_hour);

        // Determine visual state
        let stateClass = '';
        if      (isPast)                                         stateClass = 'ts-past';
        else if (isBooked)                                       stateClass = 'ts-booked';
        else if (slotStart !== null && slotEnd !== null
                 && h === slotStart)                             stateClass = 'ts-start';
        // AFTER:
        else if (slotStart !== null && slotEnd !== null
                && h === slotEnd)        stateClass = 'ts-end';
        else if (slotStart !== null && slotEnd !== null
                 && h > slotStart && h < slotEnd)                stateClass = 'ts-range';
        else if (slotStart !== null && slotEnd === null
                 && h === slotStart)                             stateClass = 'ts-start';

        // When in 'end' step, dim slots that can't be a valid end choice
        let dimmed = '';
        if (selStep === 'end' && !isPast && !isBooked && h !== slotStart) {
            // If slot is before or equal to start, it's unreachable as end
            if (h <= slotStart) dimmed = ' ts-past';
        }

        const disabled = isPast || isBooked;
        const label    = formatHour(h);
        const subLine  = isBooked ? 'Booked' : isPast ? 'Past' : '';

        html += `
            <button type="button"
                    class="time-slot ${stateClass}${dimmed}"
                    data-hour="${h}"
                    onclick="handleSlotClick(${h})"
                    ${disabled ? 'disabled' : ''}>
                <span class="slot-hr">${label}</span>
                ${subLine ? `<span class="slot-sub">${subLine}</span>` : ''}
            </button>`;
    }

    grid.innerHTML = html;
}


/* ── SLOT CLICK HANDLER ─────────────────────────── */
function handleSlotClick(hour) {
    clearField('bookingError');

    if (selStep === 'start') {
        slotStart = hour;
        slotEnd   = null;
        selStep   = 'end';
        setSubmitBtn(false);
        hideSummary();
        showHint('end');
        renderGrid(document.getElementById("startDate").value);

    } else {
        if (hour < slotStart) {          // strictly less-than: clicking same slot resets
            shakeSlot(hour);
            showHint('end', 'Choose a time <strong>after</strong> the start.');
            return;
        }
        if (hour === slotStart) {        // same slot clicked → reset to pick start again
            slotStart = null;
            slotEnd   = null;
            selStep   = 'start';
            setSubmitBtn(false);
            hideSummary();
            showHint('start');
            renderGrid(document.getElementById("startDate").value);
            return;
        }
        // hour is the last block included; duration = hour - slotStart + 1 ... 
        // wait — keep original math: slotEnd = hour means booking covers [slotStart, hour),
        // but we NOW want the slot AT hour to be highlighted and be the last included block.
        // Simplest: keep slotEnd = hour (exclusive end of booking = hour+1 in block terms),
        // and update renderGrid to show ts-end at slotEnd (the clicked slot boundary marker).

        const durationHours = hour - slotStart;   // e.g. click 11, start 8 → 3 hours ✓

        if (durationHours > MAX_BOOKING_HOURS) {
            shakeSlot(hour);
            showError(`Maximum booking duration is ${MAX_BOOKING_HOURS} hours.`);
            return;
        }
        if (rangeHasConflict(slotStart, hour)) {
            shakeSlot(hour);
            showError('There is a booked slot within your selected range. Choose a shorter or different time.');
            return;
        }

        slotEnd = hour;   // exclusive upper bound (same as before)
        selStep = 'done';
        setSubmitBtn(true);
        showHint('done');
        renderGrid(document.getElementById("startDate").value);
        updateSummary();
    }
}

/** True if any booked slot overlaps the range [startHour, endHour). */
function rangeHasConflict(startHour, endHour) {
    return bookedSlots.some(s => startHour < s.end_hour && endHour > s.start_hour);
}

function shakeSlot(hour) {
    const btn = document.querySelector(`.time-slot[data-hour="${hour}"]`);
    if (!btn) return;
    btn.classList.add('ts-shake');
    setTimeout(() => btn.classList.remove('ts-shake'), 400);
}


/* ── BOOKING SUMMARY ────────────────────────────── */
function updateSummary() {
    if (slotStart === null || slotEnd === null) { hideSummary(); return; }

    const hours = slotEnd - slotStart;
    const cost  = hours * pricePerHour;

    document.getElementById("sumRange").textContent    = `${formatHour(slotStart)} → ${formatHour(slotEnd)}`;
    document.getElementById("sumDuration").textContent = `${hours} hour${hours > 1 ? 's' : ''}`;
    document.getElementById("sumCost").textContent     = `₱${cost.toLocaleString()}`;

    document.getElementById("timeSummary").style.display = "flex";
}

function hideSummary() {
    document.getElementById("timeSummary").style.display = "none";
}


/* ── STEP HINT ──────────────────────────────────── */
function showHint(step, override) {
    const map = {
        start: 'Click a time block to set your <strong>start time</strong>',
        end:   'Now click a block to set your <strong>end time</strong>',
        done:  '<i class="fas fa-check-circle" style="color:#14b8a6"></i>&nbsp; Time selected — scroll down to continue'
    };
    document.getElementById("stepHintText").innerHTML = override || map[step] || '';
}


/* ── SUBMIT: re-validate then pass to equipment ─── */
async function handleBookingSubmit(event) {
    event.preventDefault();
    if (isSubmitting) return;

    clearField('bookingError');

    // ── 1. Date validation ──────────────────────────
    const dateVal = document.getElementById("startDate").value;
    if (!dateVal) { showError("Please select a booking date."); return; }

    const chosen  = new Date(dateVal + "T00:00:00");
    const today   = new Date(); today.setHours(0,0,0,0);
    if (chosen < today) { showError("Cannot book a past date."); return; }

    // ── 2. Time slot validation ─────────────────────
    if (slotStart === null || slotEnd === null) {
        showError("Please select a start and end time.");
        return;
    }
    if (slotEnd - slotStart < MIN_BOOKING_HOURS) {
        showError(`Minimum booking is ${MIN_BOOKING_HOURS} hour.`);
        return;
    }
    if (slotEnd - slotStart > MAX_BOOKING_HOURS) {
        showError(`Maximum booking duration is ${MAX_BOOKING_HOURS} hours.`);
        return;
    }

    // ── 3. Re-fetch slots (race-condition check) ────
    isSubmitting = true;
    setSubmitBtn(false, 'Checking availability…');

    const freshSlots = await fetchBookedSlots(selectedFacilityId, dateVal);

    if (JSON.stringify(freshSlots) !== JSON.stringify(bookedSlots)) {
        bookedSlots = freshSlots;

        if (rangeHasConflict(slotStart, slotEnd)) {
            showError('⚠️ That slot was just booked by someone else. Please choose a different time.');
            slotStart = null; slotEnd = null; selStep = 'start';
            setSubmitBtn(false);
            hideSummary();
            showHint('start');
            renderGrid(dateVal);
            isSubmitting = false;
            return;
        }
    }

    isSubmitting = false;
    setSubmitBtn(true);

    // ── 4. Past-time guard for today ───────────────
    const now = new Date();
    const isToday = (dateVal === now.toISOString().split("T")[0]);
    if (isToday && slotStart < now.getHours()) {
        showError("Selected start time has already passed. Please pick a future slot.");
        return;
    }

    // ── 5. Close modal, open equipment popup ───────
    const facilityTotal = (slotEnd - slotStart) * pricePerHour;

    closeBookingModal();

    openEquipmentModal({
        facility_id:    selectedFacilityId,
        booking_date:   dateVal,
        start_time:     formatHour(slotStart),
        end_time:       formatHour(slotEnd),
        facility_total: facilityTotal,
        purpose:        document.getElementById("purpose").value.trim()
    });
}


/* ── HELPERS ────────────────────────────────────── */
function setSubmitBtn(enabled, label) {
    const btn = document.getElementById("bookingSubmitBtn");
    btn.disabled     = !enabled;
    btn.innerHTML    = enabled
        ? '<i class="fas fa-arrow-right"></i>&nbsp; Continue to Equipment'
        : `<i class="fas fa-spinner fa-spin"></i>&nbsp; ${label || 'Continue to Equipment'}`;
}

function showGridLoader(show) {
    document.getElementById("timeGridLoader").style.display = show ? "block" : "none";
    document.getElementById("timeGrid").style.display       = show ? "none"  : "grid";
}

function showError(msg) {
    const box = document.getElementById("bookingError");
    box.innerHTML     = `<i class="fas fa-exclamation-circle"></i>&nbsp; ${msg}`;
    box.style.display = "block";
    box.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

function clearField(id) {
    const el = document.getElementById(id);
    if (el) { el.textContent = ''; el.style.display = 'none'; }
}

function setFieldError(id, msg) {
    const el = document.getElementById(id);
    if (!el) return;
    el.textContent    = msg;
    el.style.display  = "block";
}

function closeBookingModal() {
    stopPolling();
    document.getElementById("bookingModal").style.display = "none";
}

function handleOverlayClick(event) {
    if (!document.querySelector(".modal-container.minimal").contains(event.target)) {
        // Warn user if they have an in-progress selection
        if (slotStart !== null) {
            Swal.fire({
                title: 'Cancel Booking?',
                text: 'You have an unsaved time selection. Close anyway?',
                icon: 'question',
                showCancelButton: true,
                confirmButtonText: 'Yes, close',
                cancelButtonText: 'Keep editing',
                confirmButtonColor: '#ef4444',
            }).then(r => { if (r.isConfirmed) closeBookingModal(); });
        } else {
            closeBookingModal();
        }
    }
}


/* =====================================================
   STEP 2 — EQUIPMENT POPUP
===================================================== */
function openEquipmentModal(bookingData) {
    const items = getEquipmentForCategory(selectedCategoryName);

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
        </div>`).join('');

    const catLabel = selectedCategoryName
        ? `<span style="background:#ecfeff;color:#0f766e;padding:4px 12px;border-radius:999px;font-size:12px;font-weight:700;">${selectedCategoryName}</span>`
        : '';

    Swal.fire({
        title: '🏅 Borrow / Rent Equipment',
        width: 490,
        showCancelButton: true,
        confirmButtonText: 'Continue to Payment →',
        cancelButtonText:  'Skip (No Equipment)',
        confirmButtonColor: '#0f766e',
        cancelButtonColor:  '#94a3b8',
        allowOutsideClick: false,
        html: `
            <div style="font-family:'Poppins',sans-serif;text-align:left;">
                <div style="display:flex;align-items:center;gap:8px;margin-bottom:14px;">
                    ${catLabel}
                    <span style="font-size:12px;color:#94a3b8;">Optional — select what you need</span>
                </div>
                <div id="equipList"
                     style="max-height:280px;overflow-y:auto;display:flex;flex-direction:column;gap:8px;padding-right:4px;">
                    ${rows}
                </div>
                <div style="margin-top:16px;padding:14px 18px;
                            background:linear-gradient(135deg,#f0fdf4,#ecfeff);border-radius:14px;
                            display:flex;justify-content:space-between;align-items:center;">
                    <span style="font-size:13px;color:#64748b;font-weight:600;">Equipment Subtotal</span>
                    <span id="equipSubtotal" style="font-size:22px;font-weight:800;color:#0f766e;">₱0</span>
                </div>
            </div>`,

        didOpen: () => {
            const popup = Swal.getPopup();
            popup.querySelectorAll('.eq-check').forEach(cb => {
                cb.addEventListener('change', function () {
                    popup.querySelector(`#qty_row_${this.dataset.id}`).style.display =
                        this.checked ? 'flex' : 'none';
                    refreshEquipSubtotal(popup);
                });
            });
            popup.querySelectorAll('.qty-btn').forEach(btn => {
                btn.addEventListener('click', function () {
                    const el  = popup.querySelector(`#qty_${this.dataset.id}`);
                    let val   = parseInt(el.textContent);
                    val = this.classList.contains('qty-plus') ? Math.min(val + 1, 10) : Math.max(val - 1, 1);
                    el.textContent = val;
                    refreshEquipSubtotal(popup);
                });
            });
        },

        preConfirm: () => {
            const popup    = Swal.getPopup();
            const selected = [];
            popup.querySelectorAll('.eq-check:checked').forEach(cb => {
                const qty   = parseInt(popup.querySelector(`#qty_${cb.dataset.id}`).textContent);
                const price = parseFloat(cb.dataset.price);
                selected.push({
                    id: cb.dataset.id, name: decodeURIComponent(cb.dataset.name),
                    price, quantity: qty, subtotal: price * qty
                });
            });
            return selected;
        }

    }).then(result => {
        const equipment     = result.isConfirmed ? (result.value || []) : [];
        const equipTotal    = equipment.reduce((s, e) => s + e.subtotal, 0);
        const grandTotal    = bookingData.facility_total + equipTotal;
        const depositAmount = grandTotal * 0.30;

        openPaymentModal({ ...bookingData, equipment, equip_total: equipTotal,
                           total_amount: grandTotal, deposit_amount: depositAmount });
    });
}

function refreshEquipSubtotal(popup) {
    let total = 0;
    popup.querySelectorAll('.eq-check:checked').forEach(cb => {
        total += parseFloat(cb.dataset.price) *
                 parseInt(popup.querySelector(`#qty_${cb.dataset.id}`).textContent);
    });
    popup.querySelector('#equipSubtotal').textContent = '₱' + total.toLocaleString();
}


/* =====================================================
   STEP 3 — PAYMENT FLOW (GCASH)
===================================================== */
function openPaymentModal(bookingData) {
    let savedRef  = "";
    let savedFile = null;

    function buildEquipLines() {
        if (!bookingData.equipment || !bookingData.equipment.length) return '';
        const lines = bookingData.equipment.map(e =>
            `<p style="margin:3px 0;font-size:13px;">
                &nbsp;• ${e.name} × ${e.quantity}
                <span style="float:right;">₱${e.subtotal.toLocaleString()}</span>
             </p>`).join('');
        return `
            <p style="margin-top:8px;font-weight:700;font-size:13px;border-top:1px dashed #e2e8f0;padding-top:8px;">
                Equipment:
            </p>
            ${lines}
            <p style="font-size:13px;margin-top:4px;color:#64748b;">
                Equipment Total
                <span style="float:right;">₱${bookingData.equip_total.toLocaleString()}</span>
            </p>
            <hr style="border:none;border-top:1px dashed #cbd5e1;margin:8px 0;">`;
    }

    // Step 1 — QR + breakdown
    function step1() {
        Swal.fire({
            title: '💳 GCash Payment',
            width: 460,
            showCancelButton: true,
            confirmButtonText: 'I have paid →',
            cancelButtonText:  'Back',
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
                            Facility Fee (${bookingData.end_time} − ${bookingData.start_time})
                            <span style="float:right;">₱${bookingData.facility_total.toLocaleString()}</span>
                        </p>
                        ${buildEquipLines()}
                        <p style="font-weight:800;font-size:17px;margin-top:6px;">
                            Grand Total
                            <span style="float:right;color:#0f766e;">₱${bookingData.total_amount.toLocaleString()}</span>
                        </p>
                        <p style="font-size:13px;color:#64748b;margin-top:4px;">
                            Deposit Due (30%)
                            <span style="float:right;font-weight:700;color:#0f766e;">
                                ₱${bookingData.deposit_amount.toFixed(2)}
                            </span>
                        </p>
                    </div>
                </div>`
        }).then(res => { if (res.isConfirmed) step2(); });
    }

    // Step 2 — reference + screenshot + final validation
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
                        GCash Reference Number <span style="color:#ef4444;">*</span>
                    </label>
                    <input id="gcashRef"
                           placeholder="e.g. 1234567890"
                           value="${savedRef}"
                           maxlength="20"
                           style="width:100%;padding:11px 14px;border-radius:10px;
                                  border:1px solid #dbe4ee;font-size:14px;margin-bottom:14px;">
                    <label style="font-size:13px;font-weight:600;display:block;margin-bottom:6px;">
                        Upload Payment Screenshot <span style="color:#ef4444;">*</span>
                    </label>
                    <input id="gcashReceipt" type="file" accept="image/*"
                           style="width:100%;padding:9px;border-radius:10px;border:1px solid #dbe4ee;">
                    <p style="font-size:11px;color:#94a3b8;margin-top:6px;">
                        Accepted: JPG, PNG, WEBP — Max 5 MB
                    </p>
                </div>`,

            preConfirm: () => {
                const ref  = document.getElementById("gcashRef").value.trim();
                const file = document.getElementById("gcashReceipt").files[0];

                if (!ref)  { Swal.showValidationMessage("Reference number is required."); return false; }
                if (!/^\d{6,20}$/.test(ref)) {
                    Swal.showValidationMessage("Enter a valid numeric reference number (6–20 digits).");
                    return false;
                }
                if (!file) { Swal.showValidationMessage("Please attach a payment screenshot."); return false; }
                if (file.size > 5 * 1024 * 1024) {
                    Swal.showValidationMessage("Screenshot must be under 5 MB.");
                    return false;
                }
                if (!['image/jpeg','image/png','image/webp'].includes(file.type)) {
                    Swal.showValidationMessage("Only JPG, PNG, or WEBP images accepted.");
                    return false;
                }

                savedRef  = ref;
                savedFile = file;
                return true;
            }

        }).then(async res => {
            if (res.isConfirmed) {
                // Disable confirm button to prevent double submission
                Swal.showLoading();

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
                formData.append("equipment",          JSON.stringify(bookingData.equipment || []));

                try {
                    const response = await fetch("/create_reservation", { method: "POST", body: formData });
                    const data     = await response.json();

                    if (data.status === "success") {
                        Swal.fire({
                            icon: "success",
                            title: "Booking Submitted! 🎉",
                            html: `<p>Your reservation is <strong>pending admin approval</strong>.</p>
                                   <p style="color:#64748b;font-size:13px;margin-top:6px;">
                                       You will be notified once it's confirmed.
                                   </p>`,
                            confirmButtonColor: "#0f766e"
                        });
                    } else {
                        Swal.fire({ icon: "error", title: "Booking Failed", text: data.message || "Something went wrong." });
                    }
                } catch (err) {
                    Swal.fire({ icon: "error", title: "Server Error", text: "Could not submit reservation. Please try again." });
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
    const name    = document.getElementById("name").value.trim();
    const email   = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();

    if (!name || !email || !message) {
        Swal.fire("Error", "All fields are required!", "error"); return;
    }
    const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRe.test(email)) {
        Swal.fire("Error", "Please enter a valid email address.", "error"); return;
    }

    fetch("/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, message })
    })
    .then(r => r.json())
    .then(data => {
        if (data.status === "success") {
            Swal.fire("Success", "Inquiry sent successfully!", "success");
            ["name","email","message"].forEach(id => document.getElementById(id).value = "");
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
    chatbotOpen   = !chatbotOpen;

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

    const chat    = document.getElementById("popupChatMessages");
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
        const res  = await fetch("/chat", { method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }) });
        const data = await res.json();
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

const popupChatInput = document.getElementById("popupChatInput");
if (popupChatInput) {
    popupChatInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter") sendPopupMessage();
    });
}


/* =====================================================
   LOGOUT CONFIRMATION
===================================================== */
const logoutBtn = document.getElementById("logoutBtn");
if (logoutBtn) {
    logoutBtn.addEventListener("click", function (e) {
        e.preventDefault();
        const url = this.href;
        Swal.fire({
            title: "Logout?",
            text: "Are you sure you want to logout?",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Yes, Logout",
            cancelButtonText: "Cancel",
            confirmButtonColor: "#ef4444"
        }).then(r => { if (r.isConfirmed) window.location.href = url; });
    });
}


/* =====================================================
   HELPERS
===================================================== */
/** Convert integer hour (8–22) → "8:00 AM" / "10:00 PM" */
function formatHour(h) {
    h = parseInt(h);
    return `${(h % 12) || 12}:00 ${h >= 12 ? 'PM' : 'AM'}`;
}


/* =====================================================
   EQUIPMENT POPUP — inline styles (self-contained)
===================================================== */
(function injectEquipStyles() {
    const s = document.createElement('style');
    s.textContent = `
        .eq-row {
            display:flex; align-items:center; justify-content:space-between;
            background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px;
            padding:12px 14px; transition:border-color .2s,background .2s;
        }
        .eq-row:has(.eq-check:checked) { background:#f0fdf4; border-color:#14b8a6; }
        .eq-label { display:flex; align-items:center; gap:12px; cursor:pointer; flex:1; min-width:0; }
        .eq-label input[type="checkbox"] {
            width:17px; height:17px; accent-color:#0f766e;
            cursor:pointer; flex-shrink:0; margin:0; padding:0; border:none;
        }
        .eq-icon   { font-size:22px; flex-shrink:0; }
        .eq-info   { display:flex; flex-direction:column; min-width:0; }
        .eq-name   { font-size:14px; font-weight:600; color:#0f172a; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
        .eq-price  { font-size:12px; color:#0f766e; font-weight:600; }
        .eq-qty    { display:flex; align-items:center; gap:8px; margin-left:12px; flex-shrink:0; }
        .qty-btn   {
            width:28px; height:28px; border-radius:8px;
            border:1px solid #14b8a6; background:white; color:#0f766e;
            font-size:16px; font-weight:700; cursor:pointer;
            display:flex; align-items:center; justify-content:center; transition:background .15s;
        }
        .qty-btn:hover { background:#14b8a6; color:white; }
        .qty-val   { font-size:15px; font-weight:700; color:#0f172a; min-width:18px; text-align:center; }
        #equipList::-webkit-scrollbar       { width:4px; }
        #equipList::-webkit-scrollbar-thumb { background:#d1d5db; border-radius:4px; }
    `;
    document.head.appendChild(s);
})();
