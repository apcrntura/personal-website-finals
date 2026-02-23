<template>
  <section id="experience">
    <div class="container">
      <p class="section-tag">// 03 &mdash; Experience</p>
      <h2 class="section-title">IT Experience</h2>
      <div class="exp-grid">
        <div class="card exp-card" v-for="item in experiences" :key="item.title">
          <span class="exp-icon">{{ item.icon }}</span>
          <div>
            <h3 class="exp-title">{{ item.title }}</h3>
            <p class="exp-desc">{{ item.desc }}</p>
          </div>
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
}

.exp-icon { font-size: 2rem; }

.exp-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 8px;
}

.exp-desc {
  font-size: 13px;
  color: var(--muted);
  line-height: 1.8;
}
</style>
