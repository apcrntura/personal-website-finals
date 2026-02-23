<template>
  <section id="projects">
    <div class="container">
      <p class="section-label">02 — Projects</p>
      <h2 class="section-title">My Work</h2>
      <div class="projects-grid">
        <div class="project-card card" v-for="project in projects" :key="project.title">
          <div class="project-header">
            <div class="project-dots">
              <span></span><span></span><span></span>
            </div>
            <div class="project-tags">
              <span class="tag" v-for="t in project.tags" :key="t">{{ t }}</span>
            </div>
          </div>
          <h3 class="project-title">{{ project.title }}</h3>
          <p class="project-desc">{{ project.desc }}</p>
          <div class="project-footer">
            <a :href="project.url" target="_blank" rel="noopener" class="project-btn">
              View Project
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15,3 21,3 21,9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ProjectsSection',
  data() {
    return {
      projects: [
        {
          title: 'Personal Portfolio v1',
          desc: 'My first personal portfolio website featuring a galaxy video background, smooth scroll navigation, and sections for About, Education, IT Experience, Goals, and Gallery.',
          tags: ['HTML', 'CSS', 'JavaScript'],
          url: 'https://apcrntura.github.io/webportfolio/'
        },
        {
          title: 'Personal Website Finals',
          desc: 'Full-stack personal profile website built with Vue.js frontend, Flask REST API backend on Render.com, and Supabase PostgreSQL database with a working guestbook.',
          tags: ['Vue.js', 'Flask', 'Supabase'],
          url: 'https://github.com/apcrntura/personal-website-finals'
        },
      ]
    }
  }
}
</script>

<style scoped>
section { padding: 80px 0; }

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.project-card {
  display: flex; flex-direction: column; gap: 14px;
}

.project-header {
  display: flex; align-items: center;
  justify-content: space-between;
}

.project-dots { display: flex; gap: 6px; }
.project-dots span {
  width: 10px; height: 10px; border-radius: 50%;
  background: rgba(255,255,255,0.08);
}
.project-dots span:first-child { background: var(--red); }

.project-tags { display: flex; gap: 6px; }
.tag {
  font-size: 9px; letter-spacing: 0.12em; text-transform: uppercase;
  padding: 3px 10px; border: 1px solid var(--border);
  border-radius: 3px; color: var(--muted);
}

.project-title {
  font-family: 'Cinzel', serif;
  font-size: 1.1rem; font-weight: 400;
  color: var(--text); letter-spacing: 0.03em;
}

.project-desc {
  font-family: 'Crimson Pro', serif;
  font-size: 1rem; color: var(--muted);
  line-height: 1.8; flex: 1;
}

.project-footer { margin-top: 8px; }

.project-btn {
  display: inline-flex; align-items: center; gap: 7px;
  font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--red); border: 1px solid rgba(180,25,40,0.3);
  padding: 9px 18px; border-radius: 4px;
  transition: background 0.25s, color 0.25s, border-color 0.25s;
  font-family: 'DM Mono', monospace;
}
.project-btn:hover {
  background: var(--red); color: #fff;
  border-color: var(--red);
}
</style>
