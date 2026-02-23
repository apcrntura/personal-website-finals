<template>
  <section id="hero" class="hero">
    <div class="hero-content">
      <p class="hero-tag">⟨ BS Information Technology — Asia Pacific College ⟩</p>
      <h1 class="hero-name">
        <span class="line">Rae Allen</span>
        <span class="line outline">Tura</span>
      </h1>
      <p class="hero-sub">Crafting precision-built digital experiences<br>from the depths of code and cosmos.</p>
      <div class="hero-cta">
        <a href="#about" class="btn-primary">Explore Portfolio</a>
        <a href="#guestbook" class="btn-ghost">Sign Guestbook</a>
      </div>
    </div>

    <!-- Floating cosmic orbs -->
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
    <div class="scroll-hint">
      <span class="scroll-line"></span>
      <p>scroll</p>
    </div>
  </section>
</template>

<script>
export default { name: 'HeroSection' }
</script>

<style scoped>
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  text-align: center;
  padding: 0 32px;
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 850px;
}

.hero-tag {
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.3em;
  color: var(--accent);
  margin-bottom: 32px;
  text-shadow: 0 0 20px var(--glow-red);
  animation: fadeUp 0.8s ease both;
}

.hero-name {
  font-family: 'Cinzel', serif;
  font-size: clamp(3.5rem, 13vw, 9.5rem);
  font-weight: 400;
  line-height: 0.92;
  margin-bottom: 32px;
  letter-spacing: 0.02em;
}

.hero-name .line {
  display: block;
  animation: fadeUp 0.9s ease both;
  color: var(--text);
  text-shadow: 0 0 60px rgba(220,50,70,0.4), 0 0 120px rgba(180,20,40,0.2);
}
.hero-name .line:nth-child(2) { animation-delay: 0.12s; }

.hero-name .outline {
  color: transparent;
  -webkit-text-stroke: 1.5px var(--accent);
  text-shadow: 0 0 40px var(--glow-red), 0 0 80px rgba(200,30,50,0.3);
}

.hero-sub {
  font-family: 'Crimson Pro', serif;
  font-size: 1.2rem;
  font-style: italic;
  color: var(--muted);
  margin-bottom: 52px;
  line-height: 1.9;
  animation: fadeUp 0.9s ease 0.2s both;
}

.hero-cta {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
  animation: fadeUp 0.9s ease 0.3s both;
}

.btn-primary {
  background: linear-gradient(135deg, var(--crimson), var(--accent));
  color: white;
  padding: 15px 40px;
  border-radius: 100px;
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  transition: all 0.3s;
  box-shadow: 0 0 30px rgba(180,20,40,0.3);
}
.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 50px rgba(200,30,50,0.5), 0 10px 30px rgba(0,0,0,0.4);
}

.btn-ghost {
  border: 1px solid rgba(200,50,70,0.3);
  color: var(--stardust);
  padding: 15px 40px;
  border-radius: 100px;
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  transition: all 0.3s;
  backdrop-filter: blur(8px);
}
.btn-ghost:hover {
  border-color: var(--accent);
  color: var(--accent2);
  text-shadow: 0 0 10px var(--glow-red);
  box-shadow: 0 0 20px rgba(200,30,50,0.2);
  transform: translateY(-3px);
}

.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  pointer-events: none;
  animation: orbFloat 8s ease-in-out infinite;
}
.orb-1 {
  width: 500px; height: 500px;
  top: -150px; left: -150px;
  background: radial-gradient(circle, rgba(180,20,40,0.1) 0%, transparent 70%);
  animation-delay: 0s;
}
.orb-2 {
  width: 400px; height: 400px;
  bottom: -100px; right: -100px;
  background: radial-gradient(circle, rgba(120,10,80,0.08) 0%, transparent 70%);
  animation-delay: -3s;
}
.orb-3 {
  width: 300px; height: 300px;
  top: 50%; left: 50%;
  background: radial-gradient(circle, rgba(200,30,50,0.06) 0%, transparent 70%);
  animation-delay: -5s;
}

@keyframes orbFloat {
  0%, 100% { transform: translateY(0) scale(1); }
  50% { transform: translateY(-20px) scale(1.05); }
}

.scroll-hint {
  position: absolute;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  animation: fadeUp 1s ease 1s both;
}
.scroll-line {
  width: 1px; height: 50px;
  background: linear-gradient(to bottom, var(--accent), transparent);
  box-shadow: 0 0 8px var(--accent);
  animation: scrollPulse 2s ease infinite;
}
.scroll-hint p {
  font-size: 9px;
  letter-spacing: 0.4em;
  color: var(--accent);
  text-transform: uppercase;
  text-shadow: 0 0 10px var(--glow-red);
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(30px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes scrollPulse {
  0%, 100% { opacity: 1; transform: scaleY(1); }
  50% { opacity: 0.3; transform: scaleY(0.6); }
}
</style>
