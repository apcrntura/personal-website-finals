<template>
  <div id="app">
    <canvas id="starfield"></canvas>
    <NavBar />
    <main>
      <HeroSection />
      <AboutSection />
      <EducationSection />
      <ExperienceSection />
      <GoalsSection />
      <GuestbookSection />
    </main>
    <FooterSection />
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import HeroSection from './components/HeroSection.vue'
import AboutSection from './components/AboutSection.vue'
import EducationSection from './components/EducationSection.vue'
import ExperienceSection from './components/ExperienceSection.vue'
import GoalsSection from './components/GoalsSection.vue'
import GuestbookSection from './components/GuestbookSection.vue'
import FooterSection from './components/FooterSection.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    HeroSection,
    AboutSection,
    EducationSection,
    ExperienceSection,
    GoalsSection,
    GuestbookSection,
    FooterSection,
  },
  mounted() {
    this.initStarfield()
  },
  methods: {
    initStarfield() {
      const canvas = document.getElementById('starfield')
      const ctx = canvas.getContext('2d')
      let stars = []

      const resize = () => {
        canvas.width = window.innerWidth
        canvas.height = window.innerHeight
        stars = Array.from({ length: 200 }, () => ({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          r: Math.random() * 1.5 + 0.3,
          alpha: Math.random(),
          speed: Math.random() * 0.3 + 0.05,
        }))
      }

      const draw = () => {
        ctx.clearRect(0, 0, canvas.width, canvas.height)
        stars.forEach(s => {
          s.alpha += s.speed * 0.02
          if (s.alpha > 1 || s.alpha < 0) s.speed *= -1
          ctx.beginPath()
          ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2)
          ctx.fillStyle = `rgba(255,255,255,${s.alpha})`
          ctx.fill()
        })
        requestAnimationFrame(draw)
      }

      resize()
      window.addEventListener('resize', resize)
      draw()
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600;700&family=DM+Mono:wght@300;400;500&display=swap');

:root {
  --bg: #020510;
  --bg2: #050b1a;
  --surface: rgba(255,255,255,0.03);
  --border: rgba(255,255,255,0.08);
  --accent: #7eb8f7;
  --accent2: #c9a0f5;
  --gold: #f0c97a;
  --text: #e8eaf6;
  --muted: #8892b0;
  --glow: rgba(126,184,247,0.15);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'DM Mono', monospace;
  font-size: 15px;
  line-height: 1.7;
  overflow-x: hidden;
}

#starfield {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  z-index: 0;
  pointer-events: none;
}

#app { position: relative; z-index: 1; }

main { padding-top: 70px; }

section {
  padding: 100px 0;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 32px;
}

.section-tag {
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.25em;
  color: var(--accent);
  text-transform: uppercase;
  margin-bottom: 12px;
}

.section-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 300;
  color: var(--text);
  margin-bottom: 60px;
  line-height: 1.1;
}

.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 36px;
  backdrop-filter: blur(12px);
  transition: border-color 0.3s, box-shadow 0.3s;
}

.card:hover {
  border-color: rgba(126,184,247,0.25);
  box-shadow: 0 0 40px var(--glow);
}

a { color: var(--accent); text-decoration: none; }

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 2px; }
</style>
