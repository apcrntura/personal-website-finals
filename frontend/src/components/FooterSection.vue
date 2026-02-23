<template>
  <footer>
    <div class="container footer-inner">
      <div class="footer-glow"></div>
      <p class="footer-logo">RAT<span>.</span></p>
      <p class="footer-text">© 2025 Rae Allen Tura — BS Information Technology, Asia Pacific College</p>
      <p class="footer-built">✦ Built with Vue.js + Flask + Supabase ✦</p>
    </div>
  </footer>
</template>

<script>
export default { name: 'FooterSection' }
</script>

<style scoped>
footer {
  border-top: 1px solid rgba(200,50,70,0.15);
  padding: 56px 32px;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.footer-glow {
  position: absolute;
  bottom: -60px; left: 50%;
  transform: translateX(-50%);
  width: 400px; height: 200px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(180,20,40,0.12) 0%, transparent 70%);
  pointer-events: none;
}

.footer-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  position: relative;
  z-index: 1;
}

.footer-logo {
  font-family: 'Cinzel', serif;
  font-size: 2rem;
  font-weight: 700;
  color: var(--text);
  text-shadow: 0 0 30px var(--glow-red);
}
.footer-logo span { color: var(--accent); text-shadow: 0 0 15px var(--accent); }

.footer-text { font-size: 12px; color: var(--muted); }
.footer-built {
  font-size: 11px;
  color: rgba(200,50,70,0.3);
  letter-spacing: 0.15em;
}
</style>
