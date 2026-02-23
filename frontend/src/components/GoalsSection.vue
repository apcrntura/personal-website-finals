<template>
  <section id="goals">
    <div class="container">
      <p class="section-label">05 — Goals</p>
      <h2 class="section-title">Where I'm Headed</h2>
      <div class="goals-list">
        <div class="goal-row" v-for="(g, i) in goals" :key="i">
          <span class="goal-num">0{{ i+1 }}</span>
          <p class="goal-text">{{ g }}</p>
        </div>
      </div>
      <p class="quote">"To grow as a disciplined IT professional and create meaningful technology solutions."</p>
    </div>
  </section>
</template>
<script>
export default {
  name: 'GoalsSection',
  data() {
    return {
      goals: [
        'Master full-stack development with modern frameworks and cloud infrastructure.',
        'Contribute to open-source projects and build a portfolio with real-world impact.',
        'Deepen expertise in backend systems, database architecture, and DevOps pipelines.',
        'Build technology that genuinely solves problems for real people.',
      ]
    }
  }
}
</script>
<style scoped>
section { padding: 80px 0; }
.goals-list { display: flex; flex-direction: column; gap: 0; margin-bottom: 56px; }
.goal-row {
  display: flex; align-items: baseline; gap: 24px;
  padding: 22px 0; border-bottom: 1px solid var(--border);
}
.goal-row:first-child { border-top: 1px solid var(--border); }
.goal-num { font-family: 'Cinzel', serif; font-size: 0.9rem; color: var(--red); flex-shrink: 0; width: 28px; }
.goal-text { font-family: 'Crimson Pro', serif; font-size: 1.1rem; color: var(--muted); line-height: 1.7; }
.quote {
  font-family: 'Cinzel', serif; font-size: clamp(0.95rem, 2vw, 1.3rem);
  font-weight: 400; color: var(--muted); text-align: center;
  font-style: italic; max-width: 700px; margin: 0 auto; line-height: 1.7;
  letter-spacing: 0.02em;
}
</style>
