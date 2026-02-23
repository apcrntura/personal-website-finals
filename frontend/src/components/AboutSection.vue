<template>
  <section id="about">
    <div class="container">
      <div class="about-grid">
        <div class="about-left">
          <p class="section-tag">// 01 &mdash; About</p>
          <h2 class="section-title">Who I Am</h2>
          <p class="about-text">
            I'm <strong>Rae Allen Tura</strong>, an IT-oriented individual who values precision and clean design.
            I believe great technology is invisible — it works so seamlessly that users never have to think about it.
          </p>
          <p class="about-text">
            Driven by curiosity and a love for problem-solving, I approach every project with discipline,
            attention to detail, and a desire to create meaningful, impactful digital solutions.
          </p>
          <div class="skills-grid">
            <div class="skill" v-for="skill in skills" :key="skill">{{ skill }}</div>
          </div>
        </div>
        <div class="about-right">
          <div class="avatar-wrap">
            <div class="avatar-placeholder">
              <span>RAT</span>
            </div>
            <div class="avatar-ring"></div>
            <div class="avatar-ring ring-2"></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'AboutSection',
  data() {
    return {
      skills: ['Vue.js', 'NestJS', 'Flask', 'Supabase', 'PostgreSQL', 'Python', 'JavaScript', 'PC Troubleshooting']
    }
  }
}
</script>

<style scoped>
section { padding: 120px 0; }

.about-grid {
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 80px;
  align-items: center;
}

.about-text {
  color: var(--muted);
  margin-bottom: 20px;
  font-size: 15px;
}

.about-text strong { color: var(--text); }

.skills-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 36px;
}

.skill {
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.1em;
  padding: 8px 16px;
  border: 1px solid var(--border);
  border-radius: 100px;
  color: var(--muted);
  transition: all 0.3s;
}

.skill:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.avatar-wrap {
  position: relative;
  width: 280px;
  height: 280px;
  margin: 0 auto;
}

.avatar-placeholder {
  width: 200px; height: 200px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(126,184,247,0.2), rgba(201,160,245,0.2));
  border: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
}

.avatar-placeholder span {
  font-family: 'Cormorant Garamond', serif;
  font-size: 2.5rem;
  font-weight: 600;
  color: var(--accent);
  letter-spacing: 0.1em;
}

.avatar-ring {
  position: absolute;
  top: 50%; left: 50%;
  width: 240px; height: 240px;
  border-radius: 50%;
  border: 1px solid rgba(126,184,247,0.2);
  transform: translate(-50%, -50%);
  animation: spin 20s linear infinite;
}

.ring-2 {
  width: 280px; height: 280px;
  border-color: rgba(201,160,245,0.1);
  animation: spin 30s linear infinite reverse;
}

@keyframes spin { to { transform: translate(-50%, -50%) rotate(360deg); } }

@media (max-width: 900px) {
  .about-grid {
    grid-template-columns: 1fr;
    gap: 60px;
  }
  .about-right { order: -1; }
}
</style>
