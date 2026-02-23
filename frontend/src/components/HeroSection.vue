<template>
  <section id="hero" class="hero">
    <div class="hero-inner">
      <p class="hero-eyebrow">BS Information Technology — Asia Pacific College</p>
      <h1 class="hero-name">
        Rae Allen<br><span class="outline">Tura</span>
      </h1>
      <p class="hero-desc">Full-stack developer. Database architect. Precision-driven problem solver.</p>

      <div class="hero-actions">
        <a href="#about" class="btn-primary">View My Work</a>
        <a href="#guestbook" class="btn-outline">Sign Guestbook</a>
      </div>

      <div class="hero-socials">
        <a href="https://github.com/apcrntura" target="_blank" rel="noopener" class="hero-social-link">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>
          GitHub
        </a>
        <a href="https://www.facebook.com/raeallen.tura/" target="_blank" rel="noopener" class="hero-social-link">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
          Facebook
        </a>
        <a href="https://www.instagram.com/rae_allennn/" target="_blank" rel="noopener" class="hero-social-link">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          Instagram
        </a>
      </div>
    </div>

    <div class="scroll-cue">
      <span></span>
    </div>
  </section>
</template>

<script>
export default { name: 'HeroSection' }
</script>

<style scoped>
.hero {
  min-height: 100vh;
  display: flex; align-items: center; justify-content: center;
  position: relative; text-align: center; padding: 0 28px;
}

.hero-inner { max-width: 760px; position: relative; z-index: 2; }

.hero-eyebrow {
  font-size: 11px; letter-spacing: 0.28em; text-transform: uppercase;
  color: var(--red); margin-bottom: 28px;
  animation: fadeUp 0.7s ease both;
}

.hero-name {
  font-family: 'Cinzel', serif;
  font-size: clamp(3.2rem, 11vw, 8.5rem);
  font-weight: 400; line-height: 0.95;
  color: var(--text); margin-bottom: 28px;
  letter-spacing: 0.02em;
  animation: fadeUp 0.8s ease 0.08s both;
}

.outline {
  color: transparent;
  -webkit-text-stroke: 1px rgba(255,255,255,0.5);
}

.hero-desc {
  font-family: 'Crimson Pro', serif;
  font-size: 1.15rem; color: var(--muted);
  margin-bottom: 44px; line-height: 1.8;
  animation: fadeUp 0.8s ease 0.16s both;
}

.hero-actions {
  display: flex; gap: 12px; justify-content: center;
  flex-wrap: wrap; margin-bottom: 48px;
  animation: fadeUp 0.8s ease 0.24s both;
}

.btn-primary {
  background: var(--red); color: #fff;
  padding: 13px 32px; border-radius: 6px;
  font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase;
  font-family: 'DM Mono', monospace;
  transition: background 0.25s, transform 0.25s;
}
.btn-primary:hover { background: #a8131f; transform: translateY(-2px); }

.btn-outline {
  border: 1px solid rgba(255,255,255,0.18); color: var(--text);
  padding: 13px 32px; border-radius: 6px;
  font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase;
  font-family: 'DM Mono', monospace;
  transition: border-color 0.25s, transform 0.25s;
}
.btn-outline:hover { border-color: rgba(255,255,255,0.4); transform: translateY(-2px); }

.hero-socials {
  display: flex; gap: 24px; justify-content: center; flex-wrap: wrap;
  animation: fadeUp 0.8s ease 0.32s both;
}

.hero-social-link {
  display: flex; align-items: center; gap: 7px;
  font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase;
  color: var(--muted); transition: color 0.25s;
}
.hero-social-link:hover { color: var(--text); }

.scroll-cue {
  position: absolute; bottom: 36px; left: 50%;
  transform: translateX(-50%);
  animation: fadeUp 1s ease 0.8s both;
}
.scroll-cue span {
  display: block; width: 1px; height: 52px;
  background: linear-gradient(to bottom, var(--red), transparent);
  margin: 0 auto;
  animation: scrollLine 2s ease infinite;
}

@keyframes fadeUp { from { opacity:0; transform:translateY(24px); } to { opacity:1; transform:translateY(0); } }
@keyframes scrollLine { 0%,100% { opacity:1; transform:scaleY(1); } 50% { opacity:0.3; transform:scaleY(0.5); } }
</style>
