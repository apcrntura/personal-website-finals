<template>
  <footer>
    <div class="container footer-inner">
      <p class="footer-logo">RAT<span>.</span></p>
      <p class="footer-text">© 2025 Rae Allen Tura — BS Information Technology, Asia Pacific College</p>
      <p class="footer-built">Built with Vue.js + NestJS + Supabase</p>
    </div>
  </footer>
</template>

<script>
export default { name: 'FooterSection' }
</script>

<style scoped>
footer {
  border-top: 1px solid var(--border);
  padding: 48px 32px;
  text-align: center;
}

.footer-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.footer-logo {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--text);
}

.footer-logo span { color: var(--accent); }

.footer-text {
  font-size: 12px;
  color: var(--muted);
}

.footer-built {
  font-size: 11px;
  color: rgba(136,146,176,0.4);
  letter-spacing: 0.1em;
}
</style>
