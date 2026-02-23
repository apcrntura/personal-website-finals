<template>
  <footer>
    <div class="container footer-inner">
      <p class="footer-name">RAT<span>.</span></p>
      <p class="footer-sub">Rae Allen Tura — BS Information Technology, Asia Pacific College</p>
      <div class="footer-socials">
        <a href="https://github.com/apcrntura" target="_blank" rel="noopener">GitHub</a>
        <span>·</span>
        <a href="https://www.facebook.com/raeallen.tura/" target="_blank" rel="noopener">Facebook</a>
        <span>·</span>
        <a href="https://www.instagram.com/rae_allennn/" target="_blank" rel="noopener">Instagram</a>
      </div>
      <p class="footer-built">Built with Vue.js · Flask · Supabase</p>
    </div>
  </footer>
</template>

<script>
export default { name: 'FooterSection' }
</script>

<style scoped>
footer {
  border-top: 1px solid var(--border);
  padding: 52px 28px;
  text-align: center;
}
.footer-inner { display: flex; flex-direction: column; align-items: center; gap: 12px; }
.footer-name { font-family: 'Cinzel', serif; font-size: 1.6rem; font-weight: 700; color: var(--text); }
.footer-name span { color: var(--red); }
.footer-sub { font-size: 12px; color: var(--muted); }
.footer-socials { display: flex; align-items: center; gap: 12px; }
.footer-socials a { font-size: 11px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--muted); transition: color 0.25s; }
.footer-socials a:hover { color: var(--text); }
.footer-socials span { color: var(--border); }
.footer-built { font-size: 10px; color: rgba(138,130,150,0.4); letter-spacing: 0.15em; text-transform: uppercase; }
</style>
