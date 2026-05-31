# ======================
# ADMIN LOGIN
# ======================
@app.route('/admin', methods=['GET', 'POST'])
@app.route('/auth/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email         = request.form.get('email')
        password      = request.form.get('password')
        selected_role = request.form.get('role', 'admin')   # 'admin' or 'staff'
        is_ajax       = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

        c = sqlite3.connect(db_path)
        c.row_factory = sqlite3.Row
        cur = c.cursor()
        cur.execute("SELECT * FROM users WHERE email = ? AND role IN ('admin', 'staff')", (email,))
        admin = cur.fetchone()
        c.close()

        # Wrong credentials
        if not admin or not check_password_hash(admin['password'], password):
            if is_ajax:
                return jsonify({'error': 'Invalid credentials.'})
            return render_template('auth/admin-login.html', error='Invalid credentials.')

        # Role mismatch — account exists but selected role tab doesn't match
        if admin['role'] != selected_role:
            if is_ajax:
                return jsonify({'role_mismatch': True})
            return render_template('auth/admin-login.html',
                                   error=f"This account is not registered as a {selected_role.capitalize()}.")

        # Success
        session['admin']      = admin['email']
        session['admin_role'] = admin['role']
        session['admin_name'] = admin['name']

        if is_ajax:
            return jsonify({'redirect': url_for('dashboard')})
        return redirect(url_for('dashboard'))

    # Already logged in
    if 'admin' in session:
        return redirect(url_for('dashboard'))

    return render_template('auth/admin-login.html')
