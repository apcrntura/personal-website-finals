<template>
  <div id="app">
    <canvas id="galaxy"></canvas>
    <NavBar />
    <main>
      <HeroSection />
      <AboutSection />
      <ProjectsSection />
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
import ProjectsSection from './components/ProjectsSection.vue'
import EducationSection from './components/EducationSection.vue'
import ExperienceSection from './components/ExperienceSection.vue'
import GoalsSection from './components/GoalsSection.vue'
import GuestbookSection from './components/GuestbookSection.vue'
import FooterSection from './components/FooterSection.vue'

export default {
  name: 'App',
  components: { NavBar, HeroSection, AboutSection, ProjectsSection, EducationSection, ExperienceSection, GoalsSection, GuestbookSection, FooterSection },
  mounted() { this.initGalaxy() },
  methods: {
    initGalaxy() {
      const canvas = document.getElementById('galaxy')
      const ctx = canvas.getContext('2d')
      let W, H, stars = [], shootingStars = [], frameCount = 0

      const resize = () => {
        W = canvas.width = window.innerWidth
        H = canvas.height = window.innerHeight
        generateStars()
      }

      const generateStars = () => {
        stars = Array.from({ length: 280 }, () => ({
          x: Math.random() * W,
          y: Math.random() * H,
          z: Math.random() * W, // depth for parallax
          r: Math.random() * 1.4 + 0.2,
          alpha: Math.random() * 0.7 + 0.3,
          twinkle: Math.random() * Math.PI * 2,
          twinkleSpeed: Math.random() * 0.04 + 0.01,
          // Speed based on depth: closer = faster
          speed: 0,
        }))
        // Sort by depth so closer stars are faster
        stars.forEach(s => {
          const depth = s.z / W // 0 = far, 1 = close
          s.speed = 0.08 + depth * 0.35 // range 0.08 to 0.43 px/frame
          s.r = 0.2 + depth * 1.4
          s.alpha = 0.2 + depth * 0.8
        })
      }

      const spawnShootingStar = () => {
        if (frameCount % 240 === 0 && shootingStars.length < 3) {
          shootingStars.push({
            x: Math.random() * W * 0.7,
            y: Math.random() * H * 0.4,
            vx: 5 + Math.random() * 4,
            vy: 2 + Math.random() * 2,
            len: 80 + Math.random() * 80,
            life: 1.0,
          })
        }
      }

      const draw = () => {
        frameCount++

        // Deep space gradient bg
        const bg = ctx.createLinearGradient(0, 0, 0, H)
        bg.addColorStop(0,   '#000005')
        bg.addColorStop(0.4, '#04000e')
        bg.addColorStop(1,   '#080010')
        ctx.fillStyle = bg
        ctx.fillRect(0, 0, W, H)

        // Subtle nebula — one only, very faint
        const neb = ctx.createRadialGradient(W * 0.75, H * 0.3, 0, W * 0.75, H * 0.3, W * 0.35)
        neb.addColorStop(0,   'rgba(100, 8, 20, 0.045)')
        neb.addColorStop(0.6, 'rgba(40, 5, 60, 0.02)')
        neb.addColorStop(1,   'rgba(0,0,0,0)')
        ctx.fillStyle = neb
        ctx.fillRect(0, 0, W, H)

        // Move & draw stars (parallax drift to the right, slight downward)
        stars.forEach(s => {
          s.x += s.speed
          s.y += s.speed * 0.15

          // Wrap around
          if (s.x > W) { s.x = 0; s.y = Math.random() * H }
          if (s.y > H) { s.y = 0; s.x = Math.random() * W }

          s.twinkle += s.twinkleSpeed
          const tw = Math.sin(s.twinkle) * 0.2 + 0.8
          const a = s.alpha * tw

          ctx.beginPath()
          ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2)
          ctx.fillStyle = `rgba(230, 220, 255, ${a})`
          ctx.fill()
        })

        // Shooting stars
        spawnShootingStar()
        shootingStars = shootingStars.filter(ss => ss.life > 0)
        shootingStars.forEach(ss => {
          ss.x += ss.vx
          ss.y += ss.vy
          ss.life -= 0.018

          const grad = ctx.createLinearGradient(ss.x, ss.y, ss.x - ss.vx * ss.len / ss.vx, ss.y - ss.vy * ss.len / ss.vx)
          grad.addColorStop(0, `rgba(255, 200, 210, ${ss.life})`)
          grad.addColorStop(1, 'rgba(180, 50, 80, 0)')
          ctx.strokeStyle = grad
          ctx.lineWidth = 1.5
          ctx.beginPath()
          ctx.moveTo(ss.x, ss.y)
          ctx.lineTo(ss.x - ss.vx * (ss.len / ss.vx), ss.y - ss.vy * (ss.len / ss.vx))
          ctx.stroke()
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
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Crimson+Pro:ital,wght@0,300;0,400;1,300&family=DM+Mono:wght@300;400;500&display=swap');

:root {
  --bg:       #000008;
  --surface:  rgba(255, 255, 255, 0.035);
  --border:   rgba(255, 255, 255, 0.08);
  --red:      #c8202e;
  --red-soft: rgba(180, 25, 40, 0.18);
  --text:     #ede8f0;
  --muted:    #8a8296;
  --white:    #ffffff;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'DM Mono', monospace;
  line-height: 1.7;
  overflow-x: hidden;
}

#galaxy {
  position: fixed; top: 0; left: 0;
  width: 100%; height: 100%;
  z-index: 0; pointer-events: none;
}

#app { position: relative; z-index: 1; }
main { padding-top: 64px; }

/* Sections are tighter for easier navigation */
section { padding: 80px 0; }
section:nth-child(even) { background: rgba(255,255,255,0.012); }

.container { max-width: 1060px; margin: 0 auto; padding: 0 28px; }

.section-label {
  font-size: 10px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--red);
  margin-bottom: 10px;
  font-family: 'DM Mono', monospace;
}

.section-title {
  font-family: 'Cinzel', serif;
  font-size: clamp(1.6rem, 3.5vw, 2.6rem);
  font-weight: 400;
  color: var(--text);
  margin-bottom: 48px;
  letter-spacing: 0.04em;
}

.card {
  background: rgba(10, 5, 15, 0.7);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 28px;
  backdrop-filter: blur(12px);
  transition: border-color 0.3s, box-shadow 0.3s;
}
.card:hover {
  border-color: rgba(180, 25, 40, 0.3);
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}

a { color: var(--text); text-decoration: none; }

::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-track { background: #000; }
::-webkit-scrollbar-thumb { background: var(--red); border-radius: 2px; }
</style>
