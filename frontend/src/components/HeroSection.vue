<template>
  <section id="hero" class="hero">
    <div class="hero-content">
      <p class="hero-tag">[ IT Student — Asia Pacific College ]</p>
      <h1 class="hero-name">
        <span class="line">Rae Allen</span>
        <span class="line accent">Tura</span>
      </h1>
      <p class="hero-sub">BS Information Technology &mdash; building precision-crafted<br>digital experiences, one commit at a time.</p>
      <div class="hero-cta">
        <a href="#about" class="btn-primary">Explore</a>
        <a href="#guestbook" class="btn-ghost">Leave a Message</a>
      </div>
      <div class="scroll-hint">
        <span></span>
        <p>scroll</p>
      </div>
    </div>

    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
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
  max-width: 800px;
}

.hero-tag {
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.3em;
  color: var(--accent);
  margin-bottom: 28px;
  animation: fadeUp 0.8s ease both;
}

.hero-name {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(3.5rem, 12vw, 9rem);
  font-weight: 300;
  line-height: 0.95;
  margin-bottom: 28px;
  letter-spacing: -0.02em;
}

.hero-name .line {
  display: block;
  animation: fadeUp 0.8s ease both;
}

.hero-name .line:nth-child(2) { animation-delay: 0.1s; }

.hero-name .accent {
  color: transparent;
  -webkit-text-stroke: 1px var(--accent);
}

.hero-sub {
  font-size: 14px;
  color: var(--muted);
  margin-bottom: 48px;
  line-height: 1.9;
  animation: fadeUp 0.8s ease 0.2s both;
}

.hero-cta {
  display: flex;
  gap: 16px;
  justify-content: center;
  flex-wrap: wrap;
  animation: fadeUp 0.8s ease 0.3s both;
}

.btn-primary {
  background: var(--accent);
  color: var(--bg);
  padding: 14px 36px;
  border-radius: 100px;
  font-family: 'DM Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  transition: all 0.3s;
  font-weight: 500;
}

.btn-primary:hover {
  background: white;
  box-shadow: 0 0 30px rgba(126,184,247,0.5);
  transform: translateY(-2px);
}

.btn-ghost {
  border: 1px solid var(--border);
  color: var(--text);
  padding: 14px 36px;
  border-radius: 100px;
  font-family: 'DM Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  transition: all 0.3s;
}

.btn-ghost:hover {
  border-color: var(--accent2);
  color: var(--accent2);
  transform: translateY(-2px);
}

.scroll-hint {
  position: absolute;
  bottom: -120px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  animation: fadeUp 1s ease 0.8s both;
}

.scroll-hint span {
  width: 1px;
  height: 60px;
  background: linear-gradient(to bottom, var(--accent), transparent);
  animation: scrollLine 2s ease infinite;
}

.scroll-hint p {
  font-size: 10px;
  letter-spacing: 0.3em;
  color: var(--muted);
  text-transform: uppercase;
}

.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  pointer-events: none;
}

.orb-1 {
  width: 600px; height: 600px;
  top: -200px; left: -200px;
  background: radial-gradient(circle, rgba(126,184,247,0.08) 0%, transparent 70%);
}

.orb-2 {
  width: 500px; height: 500px;
  bottom: -100px; right: -100px;
  background: radial-gradient(circle, rgba(201,160,245,0.08) 0%, transparent 70%);
}

.orb-3 {
  width: 300px; height: 300px;
  top: 40%; left: 60%;
  background: radial-gradient(circle, rgba(240,201,122,0.05) 0%, transparent 70%);
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(30px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes scrollLine {
  0%, 100% { transform: scaleY(1); opacity: 1; }
  50% { transform: scaleY(0.5); opacity: 0.3; }
}
</style>
