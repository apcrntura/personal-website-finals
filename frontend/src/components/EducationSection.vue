<template>
  <section id="education">
    <div class="container">
      <p class="section-label">03 — Education</p>
      <h2 class="section-title">Academic Background</h2>
      <div class="card edu-card">
        <div class="edu-left">
          <p class="edu-degree">Bachelor of Science in Information Technology</p>
          <p class="edu-school">Asia Pacific College</p>
          <p class="edu-year">2022 — Present</p>
        </div>
        <span class="edu-badge">Currently Enrolled</span>
      </div>
    </div>
  </section>
</template>
<script>
export default { name: 'EducationSection' }
</script>
<style scoped>
section { padding: 80px 0; }
.edu-card { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px; }
.edu-degree { font-family: 'Cinzel', serif; font-size: 1.15rem; font-weight: 400; color: var(--text); margin-bottom: 6px; }
.edu-school { font-size: 12px; color: var(--red); letter-spacing: 0.1em; margin-bottom: 4px; }
.edu-year { font-size: 11px; color: var(--muted); letter-spacing: 0.1em; }
.edu-badge {
  font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase;
  padding: 8px 18px; border: 1px solid rgba(180,25,40,0.35);
  border-radius: 4px; color: var(--red);
}
</style>
