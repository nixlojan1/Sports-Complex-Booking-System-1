/* =====================================================
   HERO SLIDER
===================================================== */
document.addEventListener("DOMContentLoaded", () => {

    const slides = document.querySelectorAll(".slide");
    const title  = document.getElementById("heroTitle");
    const text   = document.getElementById("heroText");
    const dotsContainer = document.getElementById("dots");

    const heroData = [
        { title: "Play. Book. Enjoy.",        text: "Reserve sports facilities quickly and easily anytime." },
        { title: "Modern Sports Booking",     text: "Manage schedules and reservations in one system." },
        { title: "Easy Facility Access",      text: "Book courts and venues without hassle." }
    ];

    let index = 0;

    // Build dots
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

    function next() {
        index = (index + 1) % 3;
        update();
    }

    update();
    setInterval(next, 10000);
});


/* =====================================================
   SCROLL TO HASH ON LOAD
===================================================== */
window.addEventListener("load", function () {
    if (window.location.hash) {
        const element = document.querySelector(window.location.hash);
        if (element) element.scrollIntoView({ behavior: "smooth" });
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
            const cardCategory = card.getAttribute("data-category");
            card.style.display = (category === "all" || category === cardCategory) ? "block" : "none";
        });
    });
});


/* =====================================================
   BOOKING MODAL
===================================================== */
let selectedFacilityId = null;
let pricePerHour = 0;
let computedTotal = 0;

function openBookingModal(btn) {
    document.getElementById("bookingModal").style.display = "flex";

    selectedFacilityId = btn.dataset.id;
    pricePerHour = parseFloat(btn.dataset.price);

    const today = new Date();
    const dateInput = document.getElementById("startDate");

    dateInput.value = today.toISOString().split("T")[0];
    dateInput.min = dateInput.value;

    setupTime(today);

    dateInput.onchange = handleDateChange;
    document.getElementById("startTime").onchange = handleStart;
    document.getElementById("endTime").onchange = calculateTotal;
}

function handleDateChange() {
    const selected = new Date(this.value);
    const today = new Date();
    const isToday = selected.toDateString() === today.toDateString();
    setupTime(isToday ? today : null);
}

function setupTime(now) {
    const start = document.getElementById("startTime");
    const end   = document.getElementById("endTime");

    start.innerHTML = "";
    end.innerHTML   = "";
    end.disabled    = true;

    const currentHour = now ? now.getHours() : 8;

    for (let i = 8; i <= 22; i++) {
        if (now && i < currentHour) continue;
        start.add(new Option(formatHour(i), i));
    }

    start.value = now ? currentHour : 8;
}

function handleStart() {
    const start = parseInt(this.value);
    const end   = document.getElementById("endTime");

    end.disabled = false;
    end.innerHTML = "";

    for (let i = start + 1; i <= 22; i++) {
        end.add(new Option(formatHour(i), i));
    }
}

function calculateTotal() {
    const s = parseInt(document.getElementById("startTime").value);
    const e = parseInt(document.getElementById("endTime").value);

    if (!s || !e || e <= s) return 0;

    computedTotal = (e - s) * pricePerHour;
    return computedTotal;
}

function handleBookingSubmit(event) {
    event.preventDefault();

    const errorBox    = document.getElementById("bookingError");
    errorBox.style.display = "none";
    errorBox.innerHTML = "";

    const bookingDate = document.getElementById("startDate").value;
    const start       = document.getElementById("startTime").value;
    const end         = document.getElementById("endTime").value;
    const purpose     = document.getElementById("purpose").value;
    const total       = calculateTotal();

    if (!start || !end || end <= start) { showError("Please select a valid time range."); return; }
    if (total <= 0)                       { showError("Invalid booking duration.");         return; }

    const deposit = total * 0.30;

    closeBookingModal();

    openPaymentModal({
        facility_id:    selectedFacilityId,
        booking_date:   bookingDate,
        start_time:     formatHour(start),
        end_time:       formatHour(end),
        total_amount:   total,
        deposit_amount: deposit,
        purpose:        purpose
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
   PAYMENT FLOW (GCASH)
===================================================== */
function openPaymentModal(bookingData) {

    let savedRef  = "";
    let savedFile = null;

    // Step 1 – show QR / GCash details
    function step1() {
        Swal.fire({
            title: "Gcash Details",
            width: 440,
            showCancelButton: true,
            confirmButtonText: "Continue",
            cancelButtonText: "Close",
            confirmButtonColor: "#1e88e5",
            cancelButtonColor: "#aaa",
            html: `
                <div style="font-family:Arial;text-align:center;">
                    <div style="background:#f8f9fb;padding:18px;border-radius:14px;margin-bottom:15px;">
                        <img src="/static/images/qr.png"
                             style="width:170px;height:170px;border-radius:12px;object-fit:cover;">
                        <p style="font-size:12px;color:#666;margin-top:10px;">Scan QR using GCash</p>
                    </div>
                    <div style="text-align:left;font-size:14px;background:#fff;border:1px solid #eee;padding:12px;border-radius:10px;margin-bottom:12px;">
                        <p><b>GCash Name:</b> Sports Complex</p>
                        <p><b>GCash Number:</b> 09464217995</p>
                    </div>
                    <div style="text-align:left;background:#e3f2fd;padding:12px;border-radius:10px;">
                        <p><b>Total:</b> ₱${bookingData.total_amount}</p>
                        <p><b>Deposit (30%):</b> ₱${bookingData.deposit_amount.toFixed(2)}</p>
                    </div>
                </div>`
        }).then(res => { if (res.isConfirmed) step2(); });
    }

    // Step 2 – reference number + screenshot
    function step2() {
        Swal.fire({
            title: "Reference Details",
            width: 420,
            showCancelButton: true,
            confirmButtonText: "Submit Booking",
            cancelButtonText: "Back",
            confirmButtonColor: "#1e88e5",
            cancelButtonColor: "#aaa",
            html: `
                <div style="font-family:Arial;text-align:left;">
                    <label style="font-size:13px;font-weight:bold;">GCash Reference Number</label>
                    <input id="gcashRef"
                           placeholder="Enter reference number"
                           value="${savedRef}"
                           style="width:100%;padding:10px;border-radius:8px;border:1px solid #ddd;margin-bottom:12px;">
                    <label style="font-size:13px;font-weight:bold;">Upload Screenshot</label>
                    <input id="gcashReceipt" type="file" accept="image/*"
                           style="width:100%;padding:8px;border-radius:8px;border:1px solid #ddd;">
                </div>`,
            preConfirm: () => {
                const ref  = document.getElementById("gcashRef").value;
                const file = document.getElementById("gcashReceipt").files[0];
                if (!ref)  { Swal.showValidationMessage("Reference number is required"); return false; }
                if (!file) { Swal.showValidationMessage("Please upload screenshot");      return false; }
                savedRef  = ref;
                savedFile = file;
                return true;
            }
        }).then(async res => {

            if (res.isConfirmed) {
                const formData = new FormData();
                formData.append("facility_id",        bookingData.facility_id);
                formData.append("booking_date",        bookingData.booking_date);
                formData.append("start_time",          bookingData.start_time);
                formData.append("end_time",            bookingData.end_time);
                formData.append("total_amount",        bookingData.total_amount);
                formData.append("deposit_amount",      bookingData.deposit_amount);
                formData.append("purpose",             bookingData.purpose);
                formData.append("gcash_reference",     savedRef);
                formData.append("payment_screenshot",  savedFile);

                try {
                    const response = await fetch("/create_reservation", { method: "POST", body: formData });
                    const data     = await response.json();

                    if (data.status === "success") {
                        Swal.fire({ icon: "success", title: "Booking Submitted", text: "Waiting for admin approval", confirmButtonColor: "#1e88e5" });
                    } else {
                        Swal.fire({ icon: "error", title: "Booking Failed", text: data.message || "Something went wrong" });
                    }
                } catch (err) {
                    Swal.fire({ icon: "error", title: "Server Error", text: "Unable to submit reservation" });
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

    // User bubble
    const userDiv = document.createElement("div");
    userDiv.className   = "user-msg";
    userDiv.textContent = message;
    chat.appendChild(userDiv);

    input.value = "";
    chat.scrollTop = chat.scrollHeight;

    // Typing indicator
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
            cancelButtonText: "Cancel"
        }).then(result => {
            if (result.isConfirmed) window.location.href = logoutUrl;
        });
    });
}


/* =====================================================
   HELPERS
===================================================== */
function formatHour(h) {
    h = parseInt(h);
    const ampm = h >= 12 ? "PM" : "AM";
    const hour = h % 12 || 12;
    return hour + ":00 " + ampm;
}
