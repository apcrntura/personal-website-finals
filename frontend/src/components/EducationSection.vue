<template>
  <section id="education">
    <div class="container">
      <p class="section-tag">// 02 — Education</p>
      <h2 class="section-title">Academic Background</h2>
      <div class="edu-card card">
        <div class="edu-icon">🎓</div>
        <div class="edu-info">
          <span class="edu-degree">Bachelor of Science in Information Technology</span>
          <span class="edu-school">Asia Pacific College</span>
          <span class="edu-year">2022 — Present</span>
        </div>
        <div class="edu-badge">Current</div>
      </div>
    </div>
  </section>
</template>

<script>
export default { name: 'EducationSection' }
</script>

<style scoped>
section { padding: 100px 0; }

.edu-card {
  display: flex;
  align-items: center;
  gap: 28px;
  flex-wrap: wrap;
}

.edu-icon { font-size: 2.5rem; filter: drop-shadow(0 0 10px rgba(200,50,70,0.4)); }

.edu-info { display: flex; flex-direction: column; gap: 6px; flex: 1; }

.edu-degree {
  font-family: 'Cinzel', serif;
  font-size: 1.3rem;
  font-weight: 400;
  color: var(--text);
  text-shadow: 0 0 30px var(--glow-soft);
}

.edu-school { font-size: 13px; color: var(--accent2); text-shadow: 0 0 10px var(--glow-red); }
.edu-year { font-size: 12px; color: var(--muted); letter-spacing: 0.1em; }

.edu-badge {
  padding: 7px 20px;
  border-radius: 100px;
  border: 1px solid var(--accent);
  color: var(--accent);
  font-size: 11px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  text-shadow: 0 0 10px var(--glow-red);
  box-shadow: 0 0 15px rgba(200,30,50,0.15);
}
</style>
