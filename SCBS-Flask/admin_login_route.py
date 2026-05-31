<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Admin Login – Sports Complex</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>

<style>
:root {
  --bg:        #07090d;
  --surface:   #0d1219;
  --border:    #182030;
  --cyan:      #00e5ff;
  --cyan-dim:  rgba(0,229,255,0.10);
  --cyan-glow: rgba(0,229,255,0.25);
  --text:      #dde8f0;
  --muted:     #4e6880;
}

*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }

body {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg);
  font-family: 'DM Sans', sans-serif;
  color: var(--text);
  overflow: hidden;
}

/* ── animated grid ── */
.bg-grid {
  position: fixed; inset: 0; z-index: 0;
  background-image:
    linear-gradient(rgba(0,229,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,229,255,0.03) 1px, transparent 1px);
  background-size: 52px 52px;
  animation: drift 24s linear infinite;
}
@keyframes drift { to { background-position: 52px 52px; } }

.glow-tl {
  position: fixed; width: 480px; height: 480px; border-radius: 50%;
  background: radial-gradient(circle, rgba(0,229,255,0.08) 0%, transparent 70%);
  top: -140px; left: -140px; pointer-events: none; z-index: 0;
  animation: pulse 5s ease-in-out infinite;
}
.glow-br {
  position: fixed; width: 380px; height: 380px; border-radius: 50%;
  background: radial-gradient(circle, rgba(0,180,255,0.06) 0%, transparent 70%);
  bottom: -100px; right: -100px; pointer-events: none; z-index: 0;
  animation: pulse 6s ease-in-out 1s infinite;
}
@keyframes pulse { 0%,100%{opacity:.6} 50%{opacity:1} }

/* ── card ── */
.card {
  position: relative; z-index: 1;
  width: 90%; max-width: 420px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 22px;
  padding: 46px 40px 40px;
  box-shadow:
    0 0 0 1px rgba(0,229,255,0.04),
    0 28px 60px rgba(0,0,0,0.65),
    inset 0 1px 0 rgba(255,255,255,0.03);
  animation: rise .5s cubic-bezier(.22,.68,0,1.15) both;
}
@keyframes rise {
  from { opacity:0; transform:translateY(24px) scale(.97); }
  to   { opacity:1; transform:none; }
}
.card::before {
  content:'';
  position: absolute; top:0; left:12%; right:12%; height:2px;
  background: linear-gradient(90deg, transparent, var(--cyan), transparent);
  border-radius: 0 0 4px 4px;
}

/* ── icon ── */
.icon-wrap {
  width: 72px; height: 72px; border-radius: 18px;
  margin: 0 auto 22px;
  background: var(--cyan-dim);
  border: 1px solid rgba(0,229,255,0.2);
  display: flex; align-items: center; justify-content: center;
  font-size: 28px; color: var(--cyan);
  box-shadow: 0 0 24px rgba(0,229,255,0.12);
  transition: all .3s;
}

/* ── header ── */
.card-header { text-align: center; margin-bottom: 32px; }
.card-header h1 {
  font-family: 'Bebas Neue', sans-serif;
  font-size: 34px; letter-spacing: 2px;
  color: var(--cyan);
  text-shadow: 0 0 28px rgba(0,229,255,0.3);
  margin-bottom: 6px;
  transition: opacity .2s;
}
.card-header p { color: var(--muted); font-size: 13.5px; }

/* ── role tabs ── */
.role-tabs {
  display: flex; gap: 10px;
  margin-bottom: 26px;
}
.role-tab {
  flex: 1; padding: 11px 0;
  border-radius: 11px;
  border: 1px solid var(--border);
  background: transparent;
  color: var(--muted);
  font-family: 'DM Sans', sans-serif;
  font-size: 13.5px; font-weight: 500;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center; gap: 8px;
  transition: all .22s;
}
.role-tab i { font-size: 13px; }
.role-tab:hover {
  border-color: rgba(0,229,255,0.3);
  color: var(--cyan);
}
.role-tab.active {
  background: var(--cyan-dim);
  border-color: rgba(0,229,255,0.4);
  color: var(--cyan);
  box-shadow: 0 0 14px rgba(0,229,255,0.1);
}

#role-input { display: none; }

/* ── field ── */
.field { margin-bottom: 20px; }
.field label {
  display: block; margin-bottom: 7px;
  font-size: 12.5px; font-weight: 500;
  color: var(--muted); letter-spacing: .4px; text-transform: uppercase;
}
.input-wrap { position: relative; }

/* left icon */
.input-wrap .field-icon {
  position: absolute; left: 15px; top: 50%;
  transform: translateY(-50%);
  color: var(--muted); font-size: 13px;
  transition: color .2s;
  pointer-events: none;
  z-index: 1;
}

.input-wrap input {
  width: 100%;
  padding: 13px 44px 13px 44px;
  border-radius: 12px;
  border: 1px solid var(--border);
  background: rgba(0,0,0,0.3);
  color: var(--text);
  font-family: 'DM Sans', sans-serif;
  font-size: 14px;
  outline: none;
  transition: border-color .2s, box-shadow .2s;
}
.input-wrap input::placeholder { color: #2e4255; }
.input-wrap input:focus {
  border-color: rgba(0,229,255,0.5);
  box-shadow: 0 0 0 3px rgba(0,229,255,0.08);
}
.input-wrap:focus-within .field-icon { color: var(--cyan); }

/* eye toggle */
.eye-btn {
  position: absolute;
  right: 0; top: 0; bottom: 0;
  width: 44px;
  background: none; border: none;
  cursor: pointer;
  color: var(--muted); font-size: 13px;
  display: flex; align-items: center; justify-content: center;
  transition: color .2s;
  border-radius: 0 12px 12px 0;
}
.eye-btn:hover { color: var(--cyan); }

/* ── submit ── */
.submit-btn {
  width: 100%; margin-top: 6px;
  padding: 14px;
  border: none; border-radius: 12px;
  background: linear-gradient(90deg, #00cfff, #00e5ff);
  color: #001018;
  font-family: 'DM Sans', sans-serif;
  font-size: 14.5px; font-weight: 700;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center; gap: 9px;
  transition: transform .2s, box-shadow .2s, opacity .2s;
}
.submit-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 28px rgba(0,229,255,0.28);
}
.submit-btn:active:not(:disabled) { transform: translateY(0); }
.submit-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* ── spinner inside button ── */
.btn-spinner {
  width: 15px; height: 15px;
  border: 2px solid rgba(0,16,24,0.3);
  border-top-color: #001018;
  border-radius: 50%;
  animation: spin .7s linear infinite;
  display: none;
}
.submit-btn.loading .btn-spinner { display: block; }
.submit-btn.loading .btn-text    { display: none; }

@keyframes spin { to { transform: rotate(360deg); } }

/* ── divider ── */
.divider {
  height: 1px; margin: 28px 0 0;
  background: linear-gradient(90deg, transparent, var(--border), transparent);
}

/* ── footer ── */
.card-footer {
  text-align: center; margin-top: 18px;
  font-size: 12px; color: var(--muted);
}

/* ── role badge ── */
.role-badge {
  display: inline-flex; align-items: center; gap: 6px;
  font-size: 11.5px; color: var(--cyan);
  background: var(--cyan-dim);
  border: 1px solid rgba(0,229,255,0.18);
  border-radius: 20px; padding: 3px 12px;
  margin-bottom: 22px;
  opacity: 0; transform: translateY(4px);
  transition: opacity .25s, transform .25s;
}
.role-badge.visible { opacity:1; transform:none; }
</style>
</head>
<body>

<div class="bg-grid"></div>
<div class="glow-tl"></div>
<div class="glow-br"></div>

<div class="card">

  <div class="icon-wrap" id="portal-icon">
    <i class="fas fa-shield-halved"></i>
  </div>

  <div class="card-header">
    <h1 id="portal-title">Admin Portal</h1>
    <p id="portal-subtitle">Secure access to the administration panel</p>
  </div>

  <!-- ROLE SELECTOR -->
  <div class="role-tabs">
    <button type="button" class="role-tab active" data-role="admin">
      <i class="fas fa-user-shield"></i> Admin
    </button>
    <button type="button" class="role-tab" data-role="staff">
      <i class="fas fa-user-gear"></i> Staff
    </button>
  </div>

  <div class="role-badge visible" id="role-badge">
    <i class="fas fa-circle-check" style="font-size:10px;"></i>
    <span id="role-label">Logging in as Admin</span>
  </div>

  <!-- LOGIN FORM -->
  <form id="login-form">

    <input type="hidden" name="role" id="role-input" value="admin">

    <!-- EMAIL -->
    <div class="field">
      <label>Email Address</label>
      <div class="input-wrap">
        <i class="fas fa-envelope field-icon"></i>
        <input type="email" name="email" id="email-input"
               placeholder="admin@sportscomplex.com" required>
      </div>
    </div>

    <!-- PASSWORD -->
    <div class="field">
      <label>Password</label>
      <div class="input-wrap">
        <i class="fas fa-lock field-icon"></i>
        <input type="password" name="password" id="password-input"
               placeholder="Enter your password" required>
        <button type="button" class="eye-btn" id="eye-btn" tabindex="-1">
          <i class="fas fa-eye" id="eye-icon"></i>
        </button>
      </div>
    </div>

    <button type="submit" class="submit-btn" id="submit-btn">
      <span class="btn-text">
        <i class="fas fa-arrow-right-to-bracket"></i> Sign In
      </span>
      <div class="btn-spinner"></div>
    </button>

  </form>

  <div class="divider"></div>
  <div class="card-footer">© 2026 Sports Complex Booking System</div>

</div>

<script>
// ── Portal metadata per role ──
const ROLE_META = {
  admin: {
    title:    'Admin Portal',
    subtitle: 'Secure access to the administration panel',
    badge:    'Logging in as Admin',
    icon:     'fa-shield-halved',
  },
  staff: {
    title:    'Staff Portal',
    subtitle: 'Secure access to the staff panel',
    badge:    'Logging in as Staff',
    icon:     'fa-user-gear',
  },
};

const tabs           = document.querySelectorAll('.role-tab');
const roleInput      = document.getElementById('role-input');
const roleBadge      = document.getElementById('role-badge');
const roleLabel      = document.getElementById('role-label');
const portalTitle    = document.getElementById('portal-title');
const portalSubtitle = document.getElementById('portal-subtitle');
const portalIconEl   = document.getElementById('portal-icon').querySelector('i');
const submitBtn      = document.getElementById('submit-btn');

let selectedRole = 'admin';

function applyRole(role) {
  selectedRole             = role;
  roleInput.value          = role;
  const meta               = ROLE_META[role];
  roleLabel.textContent    = meta.badge;
  portalTitle.textContent  = meta.title;
  portalSubtitle.textContent = meta.subtitle;
  portalIconEl.className   = `fas ${meta.icon}`;
  roleBadge.classList.remove('visible');
  setTimeout(() => roleBadge.classList.add('visible'), 10);
}

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    applyRole(tab.dataset.role);
  });
});

// ── Form submission ──
document.getElementById('login-form').addEventListener('submit', async function(e) {
  e.preventDefault();

  // Show loading state
  submitBtn.disabled = true;
  submitBtn.classList.add('loading');

  const fd = new FormData(this);

  let resp, data;

  try {
    resp = await fetch(window.location.pathname, {
      method:  'POST',
      body:    new URLSearchParams(fd),
      headers: { 'X-Requested-With': 'XMLHttpRequest' },
    });

    const contentType = resp.headers.get('Content-Type') || '';

    // If server sent back JSON, parse it
    if (contentType.includes('application/json')) {
      data = await resp.json();
    } else {
      // Non-JSON response (e.g. unexpected redirect or HTML error page)
      throw new Error('Unexpected response from server.');
    }

  } catch (err) {
    submitBtn.disabled = false;
    submitBtn.classList.remove('loading');
    Swal.fire({
      icon: 'error',
      title: 'Connection Error',
      text: 'Could not reach the server. Please try again.',
      background: '#0d1219',
      color: '#dde8f0',
      confirmButtonColor: '#00e5ff',
      confirmButtonText: 'OK',
    });
    return;
  }

  // Re-enable button after response
  submitBtn.disabled = false;
  submitBtn.classList.remove('loading');

  // ── Role mismatch ──
  if (data.role_mismatch) {
    const expectedLabel = selectedRole === 'admin' ? 'an Admin' : 'a Staff member';
    Swal.fire({
      icon: 'error',
      title: 'Role Mismatch',
      text: `This account is not registered as ${expectedLabel}. Please select the correct role tab and try again.`,
      background: '#0d1219',
      color: '#dde8f0',
      confirmButtonColor: '#00e5ff',
      confirmButtonText: 'Got it',
    });
    // Shake the role tabs to hint the user
    tabs.forEach(t => {
      t.style.animation = 'none';
      t.offsetHeight;    // reflow
      t.style.animation = 'shake .4s ease';
    });
    return;
  }

  // ── Invalid credentials or other error ──
  if (data.error) {
    Swal.fire({
      icon: 'error',
      title: 'Login Failed',
      text: data.error,
      background: '#0d1219',
      color: '#dde8f0',
      confirmButtonColor: '#00e5ff',
      confirmButtonText: 'Try Again',
    });
    return;
  }

  // ── Success — redirect ──
  if (data.redirect) {
    Swal.fire({
      icon: 'success',
      title: 'Welcome Back!',
      text: 'Redirecting you now…',
      background: '#0d1219',
      color: '#dde8f0',
      confirmButtonColor: '#00e5ff',
      timer: 1200,
      showConfirmButton: false,
    }).then(() => {
      window.location.href = data.redirect;
    });
  }
});

// ── Password toggle ──
document.getElementById('eye-btn').addEventListener('click', () => {
  const inp  = document.getElementById('password-input');
  const icon = document.getElementById('eye-icon');
  if (inp.type === 'password') {
    inp.type = 'text';
    icon.classList.replace('fa-eye', 'fa-eye-slash');
  } else {
    inp.type = 'password';
    icon.classList.replace('fa-eye-slash', 'fa-eye');
  }
});
</script>

<!-- Shake keyframe for role-tab hint -->
<style>
@keyframes shake {
  0%,100% { transform: translateX(0); }
  20%      { transform: translateX(-5px); }
  40%      { transform: translateX(5px); }
  60%      { transform: translateX(-4px); }
  80%      { transform: translateX(4px); }
}
</style>

{% if error %}
<script>
Swal.fire({
  icon: 'error',
  title: 'Login Failed',
  text: '{{ error }}',
  background: '#0d1219',
  color: '#dde8f0',
  confirmButtonColor: '#00e5ff',
  confirmButtonText: 'Try Again',
});
</script>
{% endif %}

{% if success %}
<script>
Swal.fire({
  icon: 'success',
  title: 'Welcome Back!',
  text: '{{ success }}',
  background: '#0d1219',
  color: '#dde8f0',
  confirmButtonColor: '#00e5ff'
});
</script>
{% endif %}

</body>
</html>