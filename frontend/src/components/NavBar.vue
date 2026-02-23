<template>
  <nav :class="['navbar', { scrolled, 'menu-open': menuOpen }]">
    <div class="nav-inner">
      <a href="#hero" class="logo">RAT<span>.</span></a>
      <button class="hamburger" @click="menuOpen = !menuOpen">
        <span></span><span></span><span></span>
      </button>
      <ul class="nav-links" :class="{ open: menuOpen }">
        <li v-for="link in links" :key="link.href">
          <a :href="link.href" @click="menuOpen = false">{{ link.label }}</a>
        </li>
      </ul>
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
        { href: '#education',  label: 'Education' },
        { href: '#experience', label: 'Experience' },
        { href: '#goals',      label: 'Goals' },
        { href: '#guestbook',  label: 'Guestbook' },
      ]
    }
  },
  mounted() {
    window.addEventListener('scroll', () => { this.scrolled = window.scrollY > 40 })
  }
}
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
  padding: 22px 32px;
  transition: all 0.4s;
}

.navbar.scrolled {
  background: rgba(5,0,3,0.88);
  backdrop-filter: blur(24px);
  border-bottom: 1px solid rgba(200,50,70,0.15);
  padding: 14px 32px;
  box-shadow: 0 4px 40px rgba(150,10,30,0.12);
}

.nav-inner {
  max-width: 1100px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  font-family: 'Cinzel', serif;
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--text);
  letter-spacing: 0.1em;
  text-shadow: 0 0 20px var(--glow-red);
}
.logo span { color: var(--accent); text-shadow: 0 0 15px var(--accent); }

.nav-links { display: flex; gap: 36px; list-style: none; }

.nav-links a {
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
  transition: color 0.3s, text-shadow 0.3s;
  position: relative;
}

.nav-links a::after {
  content: '';
  position: absolute;
  bottom: -4px; left: 0;
  width: 0; height: 1px;
  background: var(--accent);
  box-shadow: 0 0 6px var(--accent);
  transition: width 0.3s;
}

.nav-links a:hover {
  color: var(--accent2);
  text-shadow: 0 0 12px var(--glow-red);
}
.nav-links a:hover::after { width: 100%; }

.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
}
.hamburger span {
  display: block;
  width: 24px; height: 1.5px;
  background: var(--text);
  transition: all 0.3s;
}

@media (max-width: 768px) {
  .hamburger { display: flex; }
  .nav-links {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(3,0,8,0.97);
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 40px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s;
  }
  .nav-links.open { opacity: 1; pointer-events: all; }
  .nav-links a { font-size: 1.1rem; }
  .menu-open .hamburger span:nth-child(1) { transform: translateY(6.5px) rotate(45deg); }
  .menu-open .hamburger span:nth-child(2) { opacity: 0; }
  .menu-open .hamburger span:nth-child(3) { transform: translateY(-6.5px) rotate(-45deg); }
}
</style>
