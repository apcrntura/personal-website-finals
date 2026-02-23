<template>
  <section id="about">
    <div class="container">
      <div class="about-grid">
        <div class="about-left">
          <p class="section-tag">// 01 — About</p>
          <h2 class="section-title">Who I Am</h2>
          <p class="about-text">
            I'm <strong>Rae Allen Tura</strong>, an IT-oriented individual who values precision and clean design.
            I believe great technology is invisible — it works so seamlessly that users never have to think about it.
          </p>
          <p class="about-text">
            Driven by curiosity and a love for problem-solving, I approach every project with discipline,
            attention to detail, and a desire to create meaningful digital solutions.
          </p>
          <div class="skills-grid">
            <div class="skill" v-for="skill in skills" :key="skill">{{ skill }}</div>
          </div>
        </div>

        <div class="about-right">
          <div class="avatar-wrap">
            <!-- 
              HOW TO ADD YOUR PROFILE PICTURE:
              1. Add your photo to the /frontend/public/ folder (e.g. profile.jpg)
              2. Change :src="profileImg" to src="/profile.jpg"
              3. Remove the placeholder div below
            -->
            <div class="avatar-frame">
              <img v-if="profileImg" :src="profileImg" alt="Rae Allen Tura" class="avatar-img" />
              <div v-else class="avatar-placeholder">
                <span class="avatar-initials">RAT</span>
                <p class="avatar-hint">Add photo to<br>/public/profile.jpg</p>
              </div>
            </div>
            <div class="ring ring-1"></div>
            <div class="ring ring-2"></div>
            <div class="ring ring-3"></div>
            <!-- Red glow behind avatar -->
            <div class="avatar-glow"></div>
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
      // To use your photo: change this to '/profile.jpg' (after uploading to /public/)
      profileImg: '/profile.jpg',
      skills: ['Vue.js', 'Flask', 'Supabase', 'PostgreSQL', 'Python', 'JavaScript', 'REST APIs', 'PC Troubleshooting']
    }
  },
  mounted() {
    // Check if image exists, fallback to placeholder
    const img = new Image()
    img.onerror = () => { this.profileImg = null }
    img.src = this.profileImg
  }
}
</script>

<style scoped>
section { padding: 120px 0; }

.about-grid {
  display: grid;
  grid-template-columns: 1fr 360px;
  gap: 80px;
  align-items: center;
}

.about-text {
  font-family: 'Crimson Pro', serif;
  font-size: 1.15rem;
  color: var(--muted);
  margin-bottom: 20px;
  line-height: 1.9;
}
.about-text strong {
  color: var(--stardust);
  text-shadow: 0 0 15px var(--glow-soft);
}

.skills-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 36px;
}

.skill {
  font-family: 'DM Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.1em;
  padding: 8px 18px;
  border: 1px solid rgba(200,50,70,0.2);
  border-radius: 100px;
  color: var(--muted);
  transition: all 0.3s;
  background: rgba(150,10,30,0.05);
}
.skill:hover {
  border-color: var(--accent);
  color: var(--accent2);
  text-shadow: 0 0 10px var(--glow-red);
  box-shadow: 0 0 15px rgba(200,30,50,0.15);
}

/* Avatar */
.avatar-wrap {
  position: relative;
  width: 280px;
  height: 280px;
  margin: 0 auto;
}

.avatar-frame {
  width: 210px; height: 210px;
  border-radius: 50%;
  overflow: hidden;
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  z-index: 3;
  border: 2px solid rgba(200,50,70,0.3);
  box-shadow: 0 0 30px rgba(180,20,40,0.3), inset 0 0 30px rgba(150,10,30,0.1);
}

.avatar-img {
  width: 100%; height: 100%;
  object-fit: cover;
  object-position: center top;
}

.avatar-placeholder {
  width: 100%; height: 100%;
  background: linear-gradient(135deg, rgba(120,10,30,0.3), rgba(60,5,40,0.4));
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.avatar-initials {
  font-family: 'Cinzel', serif;
  font-size: 2.5rem;
  font-weight: 600;
  color: var(--accent);
  text-shadow: 0 0 20px var(--glow-red);
}

.avatar-hint {
  font-size: 10px;
  color: rgba(200,150,150,0.5);
  text-align: center;
  letter-spacing: 0.05em;
  line-height: 1.5;
}

.ring {
  position: absolute;
  top: 50%; left: 50%;
  border-radius: 50%;
  border: 1px solid;
  transform: translate(-50%, -50%);
}
.ring-1 {
  width: 240px; height: 240px;
  border-color: rgba(200,50,70,0.2);
  animation: spin 20s linear infinite;
  box-shadow: 0 0 15px rgba(180,20,40,0.1);
}
.ring-2 {
  width: 270px; height: 270px;
  border-color: rgba(150,10,60,0.12);
  animation: spin 30s linear infinite reverse;
}
.ring-3 {
  width: 300px; height: 300px;
  border-color: rgba(200,50,70,0.06);
  animation: spin 45s linear infinite;
}

.avatar-glow {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 200px; height: 200px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(180,20,40,0.2) 0%, transparent 70%);
  filter: blur(20px);
  z-index: 1;
  animation: glowPulse 4s ease-in-out infinite;
}

@keyframes spin { to { transform: translate(-50%,-50%) rotate(360deg); } }
@keyframes glowPulse {
  0%, 100% { opacity: 0.6; transform: translate(-50%,-50%) scale(1); }
  50% { opacity: 1; transform: translate(-50%,-50%) scale(1.1); }
}

@media (max-width: 900px) {
  .about-grid { grid-template-columns: 1fr; gap: 60px; }
  .about-right { order: -1; }
}
</style>
