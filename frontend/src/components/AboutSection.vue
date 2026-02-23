<template>
  <section id="about">
    <div class="container">
      <div class="about-grid">
        <div class="about-text-col">
          <p class="section-label">01 — About</p>
          <h2 class="section-title">Who I Am</h2>
          <p class="about-body">
            I'm <strong>Rae Allen Tura</strong>, a BS Information Technology student at Asia Pacific College.
            I value precision, clean design, and building things that work exactly as intended.
          </p>
          <p class="about-body">
            I enjoy tackling complex problems across the full stack — from designing relational databases
            to crafting responsive frontend interfaces that users actually enjoy using.
          </p>
          <div class="skills">
            <span class="skill" v-for="s in skills" :key="s">{{ s }}</span>
          </div>
        </div>

        <div class="about-photo-col">
          <div class="photo-frame">
            <img
              src="/profile.jpg"
              alt="Rae Allen Tura"
              class="photo"
            />
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
      skills: ['Vue.js', 'Flask', 'Supabase', 'PostgreSQL', 'Python', 'JavaScript', 'REST APIs', 'PC Troubleshooting']
    }
  }
}
</script>

<style scoped>
section { padding: 80px 0; }

.about-grid {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 64px;
  align-items: center;
}

.about-body {
  font-family: 'Crimson Pro', serif;
  font-size: 1.1rem; color: var(--muted);
  margin-bottom: 18px; line-height: 1.85;
}
.about-body strong { color: var(--text); }

.skills {
  display: flex; flex-wrap: wrap; gap: 8px; margin-top: 28px;
}
.skill {
  font-size: 10px; letter-spacing: 0.12em; text-transform: uppercase;
  padding: 6px 14px; border: 1px solid var(--border);
  border-radius: 4px; color: var(--muted);
  transition: color 0.25s, border-color 0.25s;
}
.skill:hover { color: var(--text); border-color: rgba(255,255,255,0.2); }

.photo-frame {
  width: 100%; aspect-ratio: 1;
  border-radius: 12px; overflow: hidden;
  border: 1px solid var(--border);
}
.photo {
  width: 100%; height: 100%;
  object-fit: cover; object-position: center top;
  display: block;
}

@media (max-width: 800px) {
  .about-grid { grid-template-columns: 1fr; gap: 40px; }
  .about-photo-col { max-width: 240px; margin: 0 auto; }
}
</style>
