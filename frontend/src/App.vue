<template>
  <div id="app">
    <canvas id="galaxy"></canvas>
    <div class="nebula-overlay"></div>
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
  components: { NavBar, HeroSection, AboutSection, EducationSection, ExperienceSection, GoalsSection, GuestbookSection, FooterSection },
  mounted() {
    this.initGalaxy()
  },
  methods: {
    initGalaxy() {
      const canvas = document.getElementById('galaxy')
      const ctx = canvas.getContext('2d')
      let W, H, stars = [], nebulaClouds = [], shootingStars = []
      let time = 0

      const resize = () => {
        W = canvas.width = window.innerWidth
        H = canvas.height = window.innerHeight

        // Generate stars with galaxy distribution
        stars = Array.from({ length: 350 }, () => {
          const angle = Math.random() * Math.PI * 2
          const radius = Math.pow(Math.random(), 0.5) * Math.max(W, H) * 0.7
          const cx = W / 2, cy = H / 2
          return {
            x: cx + Math.cos(angle) * radius * (0.3 + Math.random() * 0.7),
            y: cy + Math.sin(angle) * radius * 0.5 * (0.3 + Math.random() * 0.7),
            baseX: cx + Math.cos(angle) * radius * (0.3 + Math.random() * 0.7),
            baseY: cy + Math.sin(angle) * radius * 0.5 * (0.3 + Math.random() * 0.7),
            r: Math.random() * 1.8 + 0.2,
            alpha: Math.random() * 0.8 + 0.2,
            twinkleSpeed: Math.random() * 0.02 + 0.005,
            twinkleOffset: Math.random() * Math.PI * 2,
            // Color: mostly white/blue, some red/crimson for galaxy feel
            hue: Math.random() < 0.15 ? Math.random() * 30 + 340 : // red stars
                 Math.random() < 0.3  ? Math.random() * 40 + 200 : // blue stars
                 0, // white
            drift: { x: (Math.random() - 0.5) * 0.03, y: (Math.random() - 0.5) * 0.015 }
          }
        })

        // Nebula clouds
        nebulaClouds = Array.from({ length: 6 }, () => ({
          x: Math.random() * W,
          y: Math.random() * H,
          rx: Math.random() * 300 + 150,
          ry: Math.random() * 150 + 80,
          // Mix of deep red, crimson, and dark blue nebulas
          color: Math.random() < 0.5
            ? `rgba(${120 + Math.random()*60},${10 + Math.random()*20},${20 + Math.random()*20},`
            : `rgba(${10 + Math.random()*20},${10 + Math.random()*20},${80 + Math.random()*60},`,
          alpha: Math.random() * 0.06 + 0.02,
          drift: { x: (Math.random() - 0.5) * 0.008, y: (Math.random() - 0.5) * 0.005 }
        }))
      }

      const spawnShootingStar = () => {
        if (shootingStars.length < 2 && Math.random() < 0.003) {
          shootingStars.push({
            x: Math.random() * W,
            y: Math.random() * H * 0.5,
            len: Math.random() * 120 + 60,
            speed: Math.random() * 8 + 6,
            angle: Math.PI / 4 + (Math.random() - 0.5) * 0.4,
            alpha: 1,
            tail: []
          })
        }
      }

      const draw = () => {
        time += 0.01
        ctx.clearRect(0, 0, W, H)

        // Deep space background gradient
        const bg = ctx.createRadialGradient(W/2, H/2, 0, W/2, H/2, Math.max(W,H)*0.8)
        bg.addColorStop(0,   '#0a0005')
        bg.addColorStop(0.3, '#060012')
        bg.addColorStop(0.6, '#03000a')
        bg.addColorStop(1,   '#000000')
        ctx.fillStyle = bg
        ctx.fillRect(0, 0, W, H)

        // Draw nebula clouds
        nebulaClouds.forEach(n => {
          n.x += n.drift.x
          n.y += n.drift.y
          if (n.x < -n.rx) n.x = W + n.rx
          if (n.x > W + n.rx) n.x = -n.rx
          if (n.y < -n.ry) n.y = H + n.ry
          if (n.y > H + n.ry) n.y = -n.ry

          const grad = ctx.createRadialGradient(n.x, n.y, 0, n.x, n.y, n.rx)
          grad.addColorStop(0, n.color + (n.alpha) + ')')
          grad.addColorStop(0.5, n.color + (n.alpha * 0.4) + ')')
          grad.addColorStop(1, n.color + '0)')
          ctx.save()
          ctx.scale(1, n.ry / n.rx)
          ctx.fillStyle = grad
          ctx.beginPath()
          ctx.arc(n.x, n.y * (n.rx / n.ry), n.rx, 0, Math.PI * 2)
          ctx.fill()
          ctx.restore()
        })

        // Central galaxy glow (red/crimson core)
        const coreGrad = ctx.createRadialGradient(W/2, H/2, 0, W/2, H/2, W * 0.25)
        coreGrad.addColorStop(0,   'rgba(180,20,40,0.08)')
        coreGrad.addColorStop(0.4, 'rgba(120,10,30,0.04)')
        coreGrad.addColorStop(1,   'rgba(0,0,0,0)')
        ctx.fillStyle = coreGrad
        ctx.fillRect(0, 0, W, H)

        // Draw stars
        stars.forEach(s => {
          // Gentle drift
          s.x += s.drift.x
          s.y += s.drift.y
          if (Math.abs(s.x - s.baseX) > 15) s.drift.x *= -1
          if (Math.abs(s.y - s.baseY) > 8)  s.drift.y *= -1

          const twinkle = Math.sin(time * (s.twinkleSpeed * 100) + s.twinkleOffset) * 0.3 + 0.7
          const a = s.alpha * twinkle

          let color
          if (s.hue > 330) color = `rgba(255,${80 + Math.random()*20},${80 + Math.random()*20},${a})`
          else if (s.hue > 200) color = `rgba(${150 + Math.random()*50},${180 + Math.random()*40},255,${a})`
          else color = `rgba(255,255,${230 + Math.random()*25},${a})`

          // Star glow
          if (s.r > 1.2) {
            const glow = ctx.createRadialGradient(s.x, s.y, 0, s.x, s.y, s.r * 4)
            glow.addColorStop(0, color)
            glow.addColorStop(1, 'rgba(0,0,0,0)')
            ctx.fillStyle = glow
            ctx.beginPath()
            ctx.arc(s.x, s.y, s.r * 4, 0, Math.PI * 2)
            ctx.fill()
          }

          ctx.beginPath()
          ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2)
          ctx.fillStyle = color
          ctx.fill()
        })

        // Shooting stars
        spawnShootingStar()
        shootingStars = shootingStars.filter(ss => ss.alpha > 0)
        shootingStars.forEach(ss => {
          ss.x += Math.cos(ss.angle) * ss.speed
          ss.y += Math.sin(ss.angle) * ss.speed
          ss.alpha -= 0.015

          ctx.save()
          ctx.globalAlpha = ss.alpha
          const grad = ctx.createLinearGradient(
            ss.x, ss.y,
            ss.x - Math.cos(ss.angle) * ss.len,
            ss.y - Math.sin(ss.angle) * ss.len
          )
          grad.addColorStop(0, 'rgba(255,200,200,1)')
          grad.addColorStop(1, 'rgba(255,100,100,0)')
          ctx.strokeStyle = grad
          ctx.lineWidth = 1.5
          ctx.beginPath()
          ctx.moveTo(ss.x, ss.y)
          ctx.lineTo(ss.x - Math.cos(ss.angle) * ss.len, ss.y - Math.sin(ss.angle) * ss.len)
          ctx.stroke()
          ctx.restore()
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
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@300;400;600;700&family=Crimson+Pro:ital,wght@0,300;0,400;1,300;1,400&family=DM+Mono:wght@300;400;500&display=swap');

:root {
  --bg:       #000000;
  --surface:  rgba(255,255,255,0.03);
  --border:   rgba(255,255,255,0.07);
  --accent:   #e8404a;
  --accent2:  #ff7b7b;
  --gold:     #f5c842;
  --crimson:  #c0162a;
  --stardust: #ffd6d6;
  --text:     #f0e8e8;
  --muted:    #9e8888;
  --glow-red: rgba(200,30,50,0.25);
  --glow-soft:rgba(255,100,100,0.12);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }

body {
  background: #000;
  color: var(--text);
  font-family: 'DM Mono', monospace;
  font-size: 15px;
  line-height: 1.7;
  overflow-x: hidden;
}

#galaxy {
  position: fixed;
  top: 0; left: 0;
  width: 100%; height: 100%;
  z-index: 0;
  pointer-events: none;
}

.nebula-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background:
    radial-gradient(ellipse 80% 60% at 20% 30%, rgba(150,10,30,0.07) 0%, transparent 60%),
    radial-gradient(ellipse 60% 40% at 80% 70%, rgba(80,10,100,0.05) 0%, transparent 60%),
    radial-gradient(ellipse 100% 50% at 50% 100%, rgba(120,10,20,0.08) 0%, transparent 50%);
  z-index: 0;
  pointer-events: none;
  animation: nebulaPulse 12s ease-in-out infinite alternate;
}

@keyframes nebulaPulse {
  from { opacity: 0.6; }
  to   { opacity: 1; }
}

#app { position: relative; z-index: 1; }
main { padding-top: 70px; }
section { padding: 100px 0; }

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
  text-shadow: 0 0 20px var(--glow-red);
}

.section-title {
  font-family: 'Cinzel', serif;
  font-size: clamp(1.8rem, 4vw, 3rem);
  font-weight: 400;
  color: var(--text);
  margin-bottom: 60px;
  line-height: 1.2;
  text-shadow: 0 0 40px var(--glow-red), 0 0 80px rgba(200,30,50,0.15);
}

.card {
  background: rgba(15,0,5,0.6);
  border: 1px solid rgba(200,50,70,0.15);
  border-radius: 16px;
  padding: 36px;
  backdrop-filter: blur(16px);
  transition: border-color 0.4s, box-shadow 0.4s;
}

.card:hover {
  border-color: rgba(200,50,70,0.4);
  box-shadow: 0 0 40px rgba(180,20,40,0.15), inset 0 0 40px rgba(150,10,30,0.05);
}

a { color: var(--accent2); text-decoration: none; }

::-webkit-scrollbar { width: 3px; }
::-webkit-scrollbar-track { background: #000; }
::-webkit-scrollbar-thumb { background: var(--crimson); border-radius: 2px; }
</style>
