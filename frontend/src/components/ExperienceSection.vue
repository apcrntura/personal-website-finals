<template>
  <section id="experience">
    <div class="container">
      <p class="section-tag">// 03 — Experience</p>
      <h2 class="section-title">IT Experience</h2>
      <div class="exp-grid">
        <div class="card exp-card" v-for="item in experiences" :key="item.title">
          <span class="exp-icon">{{ item.icon }}</span>
          <div>
            <h3 class="exp-title">{{ item.title }}</h3>
            <p class="exp-desc">{{ item.desc }}</p>
          </div>
          <div class="exp-glow"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ExperienceSection',
  data() {
    return {
      experiences: [
        {
          icon: '🌐',
          title: 'Web Development',
          desc: 'Building responsive and dynamic web applications using modern frameworks like Vue.js and React, with REST API integration and database connectivity.'
        },
        {
          icon: '🗄️',
          title: 'Database Management',
          desc: 'Designing and querying relational databases using PostgreSQL and Supabase. Proficient in SQL, schema design, and data management.'
        },
        {
          icon: '🔧',
          title: 'PC Troubleshooting',
          desc: 'Hardware and software diagnostics, system optimization, OS installation, and network configuration for both home and enterprise setups.'
        },
      ]
    }
  }
}
</script>

<style scoped>
section { padding: 100px 0; }

.exp-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

.exp-card {
  display: flex;
  flex-direction: column;
  gap: 16px;
  position: relative;
  overflow: hidden;
}

.exp-icon {
  font-size: 2rem;
  filter: drop-shadow(0 0 8px rgba(200,50,70,0.5));
}

.exp-title {
  font-family: 'Cinzel', serif;
  font-size: 1.15rem;
  font-weight: 400;
  color: var(--text);
  margin-bottom: 8px;
  text-shadow: 0 0 20px var(--glow-soft);
}

.exp-desc { font-size: 13px; color: var(--muted); line-height: 1.8; font-family: 'Crimson Pro', serif; font-size: 1rem; }

.exp-glow {
  position: absolute;
  bottom: -20px; right: -20px;
  width: 100px; height: 100px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(180,20,40,0.1) 0%, transparent 70%);
  pointer-events: none;
}
</style>
