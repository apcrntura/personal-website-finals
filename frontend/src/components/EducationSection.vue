<template>
  <section id="education">
    <div class="container">
      <p class="section-tag">// 02 &mdash; Education</p>
      <h2 class="section-title">Academic Background</h2>
      <div class="edu-card card">
        <div class="edu-icon">🎓</div>
        <div class="edu-info">
          <span class="edu-degree">Bachelor of Science in Information Technology</span>
          <span class="edu-school">Asia Pacific College</span>
          <span class="edu-year">2022 – Present</span>
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
section { padding: 100px 0; background: rgba(255,255,255,0.01); }

.edu-card {
  display: flex;
  align-items: center;
  gap: 28px;
  flex-wrap: wrap;
}

.edu-icon { font-size: 2.5rem; }

.edu-info {
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 1;
}

.edu-degree {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--text);
}

.edu-school {
  font-size: 13px;
  color: var(--accent);
}

.edu-year {
  font-size: 12px;
  color: var(--muted);
  letter-spacing: 0.1em;
}

.edu-badge {
  padding: 6px 16px;
  border-radius: 100px;
  border: 1px solid var(--accent);
  color: var(--accent);
  font-size: 11px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
}
</style>
