<template>
  <section id="goals">
    <div class="container">
      <p class="section-tag">// 04 — Goals</p>
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
section { padding: 100px 0; }

.goals-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 32px;
  margin-bottom: 80px;
}

.goal-item {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 28px;
  border-left: 1px solid rgba(200,50,70,0.2);
  transition: border-color 0.3s, box-shadow 0.3s;
}
.goal-item:hover {
  border-color: var(--accent);
  box-shadow: -3px 0 20px rgba(200,30,50,0.15);
}

.goal-num {
  font-family: 'Cinzel', serif;
  font-size: 2.5rem;
  font-weight: 300;
  color: rgba(200,50,70,0.25);
  line-height: 1;
  text-shadow: 0 0 20px rgba(200,30,50,0.3);
}

.goal-text {
  font-family: 'Crimson Pro', serif;
  font-size: 1.05rem;
  color: var(--muted);
  line-height: 1.8;
}

.big-quote {
  border: none;
  border-top: 1px solid rgba(200,50,70,0.15);
  padding-top: 56px;
  font-family: 'Cinzel', serif;
  font-size: clamp(1rem, 2.5vw, 1.5rem);
  font-weight: 300;
  color: var(--muted);
  text-align: center;
  line-height: 1.7;
  max-width: 800px;
  margin: 0 auto;
  text-shadow: 0 0 30px rgba(200,30,50,0.2);
  letter-spacing: 0.03em;
}
</style>
