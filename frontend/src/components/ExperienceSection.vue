<template>
  <section id="experience">
    <div class="container">
      <p class="section-label">04 — Experience</p>
      <h2 class="section-title">IT Experience</h2>
      <div class="exp-grid">
        <div class="card exp-card" v-for="item in items" :key="item.title">
          <span class="exp-icon">{{ item.icon }}</span>
          <h3 class="exp-title">{{ item.title }}</h3>
          <p class="exp-desc">{{ item.desc }}</p>
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
      items: [
        { icon: '🌐', title: 'Web Development', desc: 'Building responsive full-stack web applications using Vue.js, Flask, and REST APIs with Supabase database integration.' },
        { icon: '🗄️', title: 'Database Management', desc: 'Designing and querying relational databases with PostgreSQL and Supabase — schema design, RLS policies, and data optimization.' },
        { icon: '🔧', title: 'PC Troubleshooting', desc: 'Hardware diagnostics, software repair, OS installation, network configuration for home and enterprise environments.' },
      ]
    }
  }
}
</script>
<style scoped>
section { padding: 80px 0; }
.exp-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px; }
.exp-card { display: flex; flex-direction: column; gap: 12px; }
.exp-icon { font-size: 1.8rem; }
.exp-title { font-family: 'Cinzel', serif; font-size: 1rem; font-weight: 400; color: var(--text); }
.exp-desc { font-family: 'Crimson Pro', serif; font-size: 1rem; color: var(--muted); line-height: 1.8; }
</style>
