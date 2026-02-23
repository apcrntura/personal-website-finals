<template>
  <section id="guestbook">
    <div class="container">
      <p class="section-label">06 — Guestbook</p>
      <h2 class="section-title">Leave a Message</h2>

      <div class="gb-grid">
        <form @submit.prevent="submit" class="card gb-form">
          <h3 class="form-heading">Sign the Guestbook</h3>
          <div class="field">
            <label>Name</label>
            <input v-model="form.name" type="text" placeholder="Your name" required :disabled="submitting" />
          </div>
          <div class="field">
            <label>Message</label>
            <textarea v-model="form.message" placeholder="Say something..." rows="5" required :disabled="submitting"></textarea>
          </div>
          <button type="submit" class="submit-btn" :disabled="submitting">
            {{ submitting ? 'Sending...' : 'Send Message' }}
          </button>
          <p v-if="success" class="msg-success">{{ success }}</p>
          <p v-if="error" class="msg-error">{{ error }}</p>
        </form>

        <div class="gb-list-wrap">
          <div class="gb-list-header">
            <span class="gb-count">{{ comments.length }} message{{ comments.length !== 1 ? 's' : '' }}</span>
            <button @click="load" class="refresh-btn" :disabled="loading">{{ loading ? 'Loading...' : 'Refresh' }}</button>
          </div>

          <div v-if="loading && !comments.length" class="gb-loading">
            <div class="spinner"></div>
          </div>
          <p v-else-if="!comments.length" class="gb-empty">No messages yet. Be the first!</p>

          <div v-else class="gb-list">
            <div class="gb-item card" v-for="c in comments" :key="c.id">
              <div class="gb-item-header">
                <div class="gb-avatar">{{ initials(c.name) }}</div>
                <div>
                  <p class="gb-name">{{ c.name }}</p>
                  <p class="gb-date">{{ formatDate(c.created_at) }}</p>
                </div>
              </div>
              <p class="gb-msg">{{ c.message }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
const API = import.meta.env.VITE_API_URL || 'http://localhost:5000'
export default {
  name: 'GuestbookSection',
  data() {
    return { comments: [], loading: false, submitting: false, success: '', error: '', form: { name: '', message: '' } }
  },
  mounted() { this.load() },
  methods: {
    async load() {
      this.loading = true
      try {
        const r = await fetch(`${API}/comments`)
        this.comments = await r.json()
      } catch { } finally { this.loading = false }
    },
    async submit() {
      this.submitting = true; this.success = ''; this.error = ''
      try {
        const r = await fetch(`${API}/comments`, {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.form)
        })
        if (!r.ok) throw new Error()
        this.success = '✓ Message sent successfully!'
        this.form = { name: '', message: '' }
        await this.load()
      } catch { this.error = 'Failed to send. Please try again.' }
      finally { this.submitting = false }
    },
    initials(n) { return n.split(' ').map(x => x[0]).join('').toUpperCase().slice(0,2) },
    formatDate(d) { return new Date(d).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' }) }
  }
}
</script>

<style scoped>
section { padding: 80px 0; }

.gb-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; align-items: start; }

.form-heading { font-family: 'Cinzel', serif; font-size: 1rem; font-weight: 400; color: var(--text); margin-bottom: 24px; letter-spacing: 0.04em; }

.field { display: flex; flex-direction: column; gap: 7px; margin-bottom: 16px; }
label { font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--muted); }

input, textarea {
  background: rgba(255,255,255,0.03);
  border: 1px solid var(--border); border-radius: 6px;
  padding: 12px 14px; color: var(--text);
  font-family: 'DM Mono', monospace; font-size: 13px;
  transition: border-color 0.25s; resize: vertical;
}
input:focus, textarea:focus { outline: none; border-color: rgba(255,255,255,0.2); }
input::placeholder, textarea::placeholder { color: rgba(138,130,150,0.4); }

.submit-btn {
  width: 100%; padding: 13px;
  background: var(--red); color: #fff;
  border: none; border-radius: 6px;
  font-family: 'DM Mono', monospace; font-size: 11px;
  letter-spacing: 0.18em; text-transform: uppercase;
  cursor: pointer; transition: background 0.25s;
  margin-top: 4px;
}
.submit-btn:hover:not(:disabled) { background: #a8131f; }
.submit-btn:disabled { opacity: 0.5; cursor: not-allowed; }

.msg-success { margin-top: 12px; font-size: 12px; color: #6fcf97; }
.msg-error { margin-top: 12px; font-size: 12px; color: #eb5757; }

.gb-list-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; }
.gb-count { font-size: 11px; color: var(--muted); letter-spacing: 0.1em; }
.refresh-btn {
  background: none; border: 1px solid var(--border); color: var(--muted);
  font-family: 'DM Mono', monospace; font-size: 10px; letter-spacing: 0.12em;
  padding: 5px 12px; border-radius: 4px; cursor: pointer; transition: all 0.25s;
}
.refresh-btn:hover:not(:disabled) { border-color: rgba(255,255,255,0.2); color: var(--text); }

.gb-loading { display: flex; justify-content: center; padding: 40px; }
.spinner {
  width: 24px; height: 24px; border: 1.5px solid var(--border);
  border-top-color: var(--red); border-radius: 50%;
  animation: spin 0.7s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

.gb-empty { font-size: 13px; color: var(--muted); text-align: center; padding: 40px; font-family: 'Crimson Pro', serif; font-style: italic; }

.gb-list { display: flex; flex-direction: column; gap: 12px; max-height: 560px; overflow-y: auto; padding-right: 4px; }

.gb-item { padding: 20px; }
.gb-item-header { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
.gb-avatar {
  width: 34px; height: 34px; border-radius: 50%;
  background: rgba(180,25,40,0.2); border: 1px solid rgba(180,25,40,0.25);
  display: flex; align-items: center; justify-content: center;
  font-family: 'Cinzel', serif; font-size: 11px; color: var(--red); flex-shrink: 0;
}
.gb-name { font-size: 13px; color: var(--text); }
.gb-date { font-size: 11px; color: var(--muted); margin-top: 2px; }
.gb-msg { font-family: 'Crimson Pro', serif; font-size: 1rem; color: var(--muted); line-height: 1.7; }

@media (max-width: 768px) { .gb-grid { grid-template-columns: 1fr; } }
</style>
