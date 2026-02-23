<template>
  <section id="goals">
    <div class="container">
      <p class="section-tag">// 04 &mdash; Goals</p>
      <h2 class="section-title">Where I'm Headed</h2>
      <div class="goals-grid">
        <div class="goal-item" v-for="(goal, i) in goals" :key="i">
          <span class="goal-num">0{{ i + 1 }}</span>
          <p class="goal-text">{{ goal }}</p>
        </div>
      </div>
      <blockquote class="big-quote">
        "To grow as a disciplined IT professional and create meaningful technology solutions that make a difference."
      </blockquote>
    </div>
  </section>
</template>

<script>
export default {
  name: 'GoalsSection',
  data() {
    return {
      goals: [
        'Master full-stack development with modern frameworks and cloud technologies.',
        'Contribute to open-source projects and build a meaningful developer portfolio.',
        'Pursue advanced expertise in backend systems, database architecture, and DevOps.',
        'Build technology solutions that solve real problems for real people.',
      ]
    }
  }
}
</script>

<style scoped>
section {
  padding: 100px 0;
  background: rgba(255,255,255,0.01);
}

.goals-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 32px;
  margin-bottom: 72px;
}

.goal-item {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 28px;
  border-left: 1px solid var(--border);
  transition: border-color 0.3s;
}

.goal-item:hover { border-color: var(--accent2); }

.goal-num {
  font-family: 'Cormorant Garamond', serif;
  font-size: 2.5rem;
  font-weight: 300;
  color: rgba(126,184,247,0.3);
  line-height: 1;
}

.goal-text {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.8;
}

.big-quote {
  border: none;
  border-top: 1px solid var(--border);
  padding-top: 48px;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(1.2rem, 3vw, 1.8rem);
  font-weight: 300;
  font-style: italic;
  color: var(--muted);
  text-align: center;
  line-height: 1.6;
  max-width: 800px;
  margin: 0 auto;
}
</style>
