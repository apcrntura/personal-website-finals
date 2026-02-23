<template>
  <section id="guestbook">
    <div class="container">
      <p class="section-tag">// 05 — Guestbook</p>
      <h2 class="section-title">Leave a Message</h2>

      <div class="guestbook-grid">
        <div class="form-wrap">
          <form @submit.prevent="submitComment" class="card guestbook-form">
            <h3 class="form-title">Sign the Guestbook</h3>
            <div class="field">
              <label for="name">Your Name</label>
              <input id="name" v-model="form.name" type="text" placeholder="e.g. Alex Santos" required :disabled="submitting" />
            </div>
            <div class="field">
              <label for="message">Message</label>
              <textarea id="message" v-model="form.message" placeholder="Leave a kind word or feedback 👋" rows="5" required :disabled="submitting"></textarea>
            </div>
            <button type="submit" class="submit-btn" :disabled="submitting">
              <span v-if="!submitting">Send Message ✦</span>
              <span v-else class="loading">Transmitting...</span>
            </button>
            <p v-if="successMsg" class="success-msg">{{ successMsg }}</p>
            <p v-if="errorMsg" class="error-msg">{{ errorMsg }}</p>
          </form>
        </div>

        <div class="messages-wrap">
          <div class="messages-header">
            <span class="messages-count">✦ {{ comments.length }} transmissions received</span>
            <button @click="fetchComments" class="refresh-btn" :disabled="loading">
              {{ loading ? '⟳ Loading...' : '⟳ Refresh' }}
            </button>
          </div>

          <div v-if="loading && comments.length === 0" class="loading-state">
            <div class="spinner"></div>
            <p>Receiving transmissions...</p>
          </div>

          <div v-else-if="comments.length === 0" class="empty-state">
            <p>No messages yet. Be the first to sign!</p>
          </div>

          <div v-else class="comments-list">
            <div class="comment-card card" v-for="comment in comments" :key="comment.id">
              <div class="comment-header">
                <div class="comment-avatar">{{ getInitials(comment.name) }}</div>
                <div>
                  <p class="comment-name">{{ comment.name }}</p>
                  <p class="comment-date">{{ formatDate(comment.created_at) }}</p>
                </div>
              </div>
              <p class="comment-msg">{{ comment.message }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

export default {
  name: 'GuestbookSection',
  data() {
    return {
      comments: [],
      loading: false,
      submitting: false,
      successMsg: '',
      errorMsg: '',
      form: { name: '', message: '' }
    }
  },
  mounted() { this.fetchComments() },
  methods: {
    async fetchComments() {
      this.loading = true
      try {
        const res = await fetch(`${API_URL}/comments`)
        if (!res.ok) throw new Error('Failed to fetch')
        this.comments = await res.json()
      } catch (e) {
        console.error(e)
      } finally {
        this.loading = false
      }
    },
    async submitComment() {
      this.submitting = true
      this.successMsg = ''
      this.errorMsg = ''
      try {
        const res = await fetch(`${API_URL}/comments`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ name: this.form.name, message: this.form.message })
        })
        if (!res.ok) throw new Error('Failed to submit')
        this.successMsg = '✦ Message transmitted to the cosmos!'
        this.form = { name: '', message: '' }
        await this.fetchComments()
      } catch (e) {
        this.errorMsg = '⚠ Signal lost. Please try again.'
      } finally {
        this.submitting = false
      }
    },
    getInitials(name) {
      return name.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2)
    },
    formatDate(dateStr) {
      return new Date(dateStr).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' })
    }
  }
}
</script>

<style scoped>
section { padding: 100px 0; }

.guestbook-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
  align-items: start;
}

.form-title {
  font-family: 'Cinzel', serif;
  font-size: 1.2rem;
  font-weight: 400;
  margin-bottom: 28px;
  color: var(--text);
  text-shadow: 0 0 20px var(--glow-soft);
}

.field { display: flex; flex-direction: column; gap: 8px; margin-bottom: 20px; }

label {
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

input, textarea {
  background: rgba(10,0,5,0.6);
  border: 1px solid rgba(200,50,70,0.15);
  border-radius: 10px;
  padding: 14px 16px;
  color: var(--text);
  font-family: 'DM Mono', monospace;
  font-size: 13px;
  transition: border-color 0.3s, box-shadow 0.3s;
  resize: vertical;
}
input:focus, textarea:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 20px rgba(200,30,50,0.15);
}
input::placeholder, textarea::placeholder { color: rgba(158,136,136,0.4); }

.submit-btn {
  width: 100%;
  padding: 15px;
  background: linear-gradient(135deg, var(--crimson), var(--accent));
  color: white;
  border: none;
  border-radius: 10px;
  font-family: 'DM Mono', monospace;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.15em;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 0 20px rgba(180,20,40,0.2);
  margin-top: 8px;
}
.submit-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 0 40px rgba(200,30,50,0.4);
}
.submit-btn:disabled { opacity: 0.5; cursor: not-allowed; }

.success-msg { margin-top: 14px; font-size: 13px; color: #ff9b9b; text-align: center; text-shadow: 0 0 10px rgba(255,100,100,0.3); }
.error-msg { margin-top: 14px; font-size: 13px; color: #eb5757; text-align: center; }

.messages-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}
.messages-count { font-size: 11px; color: var(--accent); text-shadow: 0 0 10px var(--glow-red); letter-spacing: 0.1em; }

.refresh-btn {
  background: none;
  border: 1px solid rgba(200,50,70,0.2);
  color: var(--muted);
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  padding: 6px 14px;
  border-radius: 100px;
  cursor: pointer;
  transition: all 0.3s;
}
.refresh-btn:hover:not(:disabled) {
  border-color: var(--accent);
  color: var(--accent2);
  box-shadow: 0 0 10px rgba(200,30,50,0.2);
}

.loading-state, .empty-state {
  text-align: center;
  padding: 60px 20px;
  color: var(--muted);
  font-size: 13px;
  font-family: 'Crimson Pro', serif;
  font-style: italic;
}

.spinner {
  width: 28px; height: 28px;
  border: 1.5px solid rgba(200,50,70,0.2);
  border-top-color: var(--accent);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin: 0 auto 16px;
  box-shadow: 0 0 10px rgba(200,30,50,0.2);
}
@keyframes spin { to { transform: rotate(360deg); } }

.comments-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
  max-height: 600px;
  overflow-y: auto;
  padding-right: 4px;
}

.comment-card { padding: 24px; }
.comment-header { display: flex; align-items: center; gap: 14px; margin-bottom: 14px; }

.comment-avatar {
  width: 38px; height: 38px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--crimson), rgba(120,10,60,0.8));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 600;
  color: var(--stardust);
  flex-shrink: 0;
  box-shadow: 0 0 15px rgba(180,20,40,0.3);
  font-family: 'Cinzel', serif;
}

.comment-name { font-size: 13px; font-weight: 500; color: var(--text); }
.comment-date { font-size: 11px; color: var(--muted); margin-top: 2px; }
.comment-msg { font-family: 'Crimson Pro', serif; font-size: 1rem; color: var(--muted); line-height: 1.7; }

@media (max-width: 768px) {
  .guestbook-grid { grid-template-columns: 1fr; }
}
</style>
