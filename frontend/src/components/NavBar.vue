<template>
  <nav :class="['navbar', { scrolled }]">
    <div class="nav-inner">
      <a href="#hero" class="logo">RAT<span>.</span></a>

      <ul class="nav-links">
        <li v-for="link in links" :key="link.href">
          <a :href="link.href">{{ link.label }}</a>
        </li>
      </ul>

      <div class="nav-social">
        <a v-for="s in socials" :key="s.label" :href="s.url" target="_blank" rel="noopener" :title="s.label" class="social-icon">
          <span v-html="s.svg"></span>
        </a>
      </div>

      <button class="hamburger" @click="menuOpen = !menuOpen" :class="{ open: menuOpen }">
        <span></span><span></span><span></span>
      </button>
    </div>

    <!-- Mobile menu -->
    <div class="mobile-menu" :class="{ open: menuOpen }">
      <a v-for="link in links" :key="link.href" :href="link.href" @click="menuOpen=false">{{ link.label }}</a>
      <div class="mobile-socials">
        <a v-for="s in socials" :key="s.label" :href="s.url" target="_blank" rel="noopener" class="social-icon">
          <span v-html="s.svg"></span>
        </a>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  data() {
    return {
      scrolled: false,
      menuOpen: false,
      links: [
        { href: '#about',      label: 'About' },
        { href: '#projects',   label: 'Projects' },
        { href: '#education',  label: 'Education' },
        { href: '#experience', label: 'Experience' },
        { href: '#guestbook',  label: 'Guestbook' },
      ],
      socials: [
        {
          label: 'GitHub',
          url: 'https://github.com/apcrntura',
          svg: `<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/></svg>`
        },
        {
          label: 'Facebook',
          url: 'https://www.facebook.com/raeallen.tura/',
          svg: `<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>`
        },
        {
          label: 'Instagram',
          url: 'https://www.instagram.com/rae_allennn/',
          svg: `<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>`
        },
      ]
    }
  },
  mounted() {
    window.addEventListener('scroll', () => { this.scrolled = window.scrollY > 50 })
  }
}
</script>

<style scoped>
.navbar {
  position: fixed; top: 0; left: 0; right: 0;
  z-index: 100;
  padding: 18px 28px;
  transition: all 0.35s;
}
.navbar.scrolled {
  background: rgba(2, 0, 8, 0.92);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255,255,255,0.06);
  padding: 12px 28px;
}

.nav-inner {
  max-width: 1060px; margin: 0 auto;
  display: flex; align-items: center; gap: 32px;
}

.logo {
  font-family: 'Cinzel', serif;
  font-size: 1.3rem; font-weight: 700;
  color: var(--text);
  letter-spacing: 0.08em;
  flex-shrink: 0;
}
.logo span { color: var(--red); }

.nav-links {
  display: flex; gap: 28px; list-style: none; flex: 1;
  justify-content: center;
}
.nav-links a {
  font-size: 11px; letter-spacing: 0.15em; text-transform: uppercase;
  color: var(--muted); transition: color 0.25s;
}
.nav-links a:hover { color: var(--text); }

.nav-social { display: flex; gap: 14px; align-items: center; flex-shrink: 0; }

.social-icon {
  color: var(--muted);
  display: flex; align-items: center;
  transition: color 0.25s, transform 0.25s;
}
.social-icon:hover { color: var(--text); transform: translateY(-2px); }

.hamburger {
  display: none; flex-direction: column; gap: 5px;
  background: none; border: none; cursor: pointer; padding: 4px; margin-left: auto;
}
.hamburger span {
  display: block; width: 22px; height: 1.5px;
  background: var(--text); transition: all 0.3s;
}
.hamburger.open span:nth-child(1) { transform: translateY(6.5px) rotate(45deg); }
.hamburger.open span:nth-child(2) { opacity: 0; }
.hamburger.open span:nth-child(3) { transform: translateY(-6.5px) rotate(-45deg); }

.mobile-menu {
  display: none; flex-direction: column; gap: 24px;
  padding: 24px 28px;
  background: rgba(2,0,8,0.98);
  border-top: 1px solid rgba(255,255,255,0.06);
  max-height: 0; overflow: hidden; transition: max-height 0.3s;
}
.mobile-menu.open { max-height: 400px; }
.mobile-menu a {
  font-size: 12px; letter-spacing: 0.15em; text-transform: uppercase; color: var(--muted);
}
.mobile-socials { display: flex; gap: 16px; margin-top: 8px; }

@media (max-width: 768px) {
  .nav-links, .nav-social { display: none; }
  .hamburger { display: flex; }
  .mobile-menu { display: flex; }
}
</style>
