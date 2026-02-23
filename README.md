# 🌌 Personal Website Finals — Rae Allen Tura

> **BS Information Technology** | Asia Pacific College  
> Built with Vue.js + Flask + Supabase

---

## 📋 Project Overview

A full-stack personal profile website that satisfies all finals requirements:

| Requirement | Status | Details |
|---|---|---|
| Vue.js Frontend | ✅ | Vite + Vue 3, deployed on Vercel |
| REST API Backend | ✅ | Flask on Render.com |
| GET /comments | ✅ | Fetches all guestbook entries from Supabase |
| POST /comments | ✅ | Inserts new guestbook entry to Supabase |
| Supabase Database | ✅ | PostgreSQL via Supabase |
| Mobile Responsive | ✅ | Fully responsive, hamburger menu on mobile |
| Updated Design | ✅ | Space/galaxy dark theme, animations, professional UI |

---

## 🗂️ Project Structure

```
personal-website-finals/
├── frontend/                  ← Vue.js app (deploy to Vercel)
│   ├── src/
│   │   ├── App.vue            ← Root component + starfield animation
│   │   ├── main.js
│   │   └── components/
│   │       ├── NavBar.vue
│   │       ├── HeroSection.vue
│   │       ├── AboutSection.vue
│   │       ├── EducationSection.vue
│   │       ├── ExperienceSection.vue
│   │       ├── GoalsSection.vue
│   │       ├── GuestbookSection.vue  ← GET + POST API calls
│   │       └── FooterSection.vue
│   ├── index.html
│   ├── vite.config.js
│   ├── package.json
│   └── .env.example
│
├── backend-flask/             ← Flask API (deploy to Render.com)
│   ├── app.py                 ← GET /comments + POST /comments
│   ├── requirements.txt
│   ├── render.yaml
│   └── .env.example
│
└── supabase-setup/
    └── schema.sql             ← Run this in Supabase SQL Editor
```

---

## 🚀 Setup Guide (Step by Step)

### STEP 1 — Set Up Supabase

1. Go to [supabase.com](https://supabase.com) and create a free account
2. Click **"New Project"**, name it `personal-website-finals`
3. Choose a region close to you (e.g. Southeast Asia)
4. Wait for project to be ready (~1 minute)
5. Go to **SQL Editor** (left sidebar)
6. Paste the entire contents of `supabase-setup/schema.sql` and click **Run**
7. Go to **Settings → API**
8. Copy your:
   - **Project URL** (looks like `https://xxxx.supabase.co`)
   - **anon/public key** (the long JWT token)

---

### STEP 2 — Deploy Backend to Render.com

1. Go to [render.com](https://render.com) and sign up (free)
2. Click **"New" → "Web Service"**
3. Connect your GitHub account and select your repo
4. Set **Root Directory** to `backend-flask`
5. Configure:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Add **Environment Variables**:
   - `SUPABASE_URL` = your Supabase Project URL
   - `SUPABASE_KEY` = your Supabase anon key
7. Click **"Create Web Service"**
8. Wait for deploy (~2-3 minutes)
9. Copy your Render URL (e.g. `https://personal-website-finals-api.onrender.com`)

> ⚠️ **Free tier note**: Render free services spin down after inactivity. First load may take ~30 seconds.

---

### STEP 3 — Deploy Frontend to Vercel

1. Go to [vercel.com](https://vercel.com) and sign in with GitHub
2. Click **"Add New Project"**
3. Import your GitHub repo
4. Set **Root Directory** to `frontend`
5. Framework preset should auto-detect as **Vite**
6. Add **Environment Variables**:
   - `VITE_API_URL` = your Render.com backend URL (from Step 2)
     - e.g. `https://personal-website-finals-api.onrender.com`
7. Click **"Deploy"**
8. Your site will be live at `your-project.vercel.app`

---

### STEP 4 — Local Development

**Backend:**
```bash
cd backend-flask
pip install -r requirements.txt
cp .env.example .env
# Fill in your .env with SUPABASE_URL and SUPABASE_KEY
python app.py
# API running at http://localhost:5000
```

**Frontend:**
```bash
cd frontend
npm install
cp .env.example .env
# Set VITE_API_URL=http://localhost:5000
npm run dev
# App running at http://localhost:5173
```

---

## 🔌 API Endpoints

### `GET /comments`
Returns all guestbook comments, newest first.

**Response:**
```json
[
  {
    "id": "uuid",
    "name": "Rae Allen",
    "message": "Hello from the guestbook!",
    "created_at": "2025-01-01T00:00:00+00:00"
  }
]
```

### `POST /comments`
Inserts a new guestbook comment.

**Request Body:**
```json
{
  "name": "Your Name",
  "message": "Your message here"
}
```

**Response (201 Created):**
```json
{
  "id": "uuid",
  "name": "Your Name",
  "message": "Your message here",
  "created_at": "2025-01-01T00:00:00+00:00"
}
```

---

## 🎨 Design Features

- **Starfield canvas animation** — 200 animated twinkling stars
- **Glassmorphism cards** — frosted glass effect with glow on hover
- **Cormorant Garamond** — elegant serif display font
- **DM Mono** — technical monospace body font
- **Orbital avatar rings** — animated rotating rings in About section
- **Gradient orbs** — atmospheric light blobs for depth
- **Responsive hamburger menu** — full-screen overlay on mobile
- **Scroll indicator** — animated scroll hint on hero
- **Loading states** — spinner while fetching comments
- **Success/error feedback** — clear form submission states

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend Framework | Vue.js 3 + Vite |
| Styling | Scoped CSS + CSS Variables |
| Backend | Flask (Python) |
| Database | Supabase (PostgreSQL) |
| Frontend Hosting | Vercel |
| Backend Hosting | Render.com |
| Fonts | Google Fonts (Cormorant Garamond, DM Mono) |

---

## 🔧 Troubleshooting

**Comments not loading?**
- Check browser console for CORS errors
- Make sure `VITE_API_URL` is set correctly (no trailing slash)
- Make sure your Render service is running

**Supabase errors?**
- Double-check your `SUPABASE_URL` and `SUPABASE_KEY` values
- Make sure you ran the `schema.sql` script
- Check that RLS policies are enabled

**Build fails on Vercel?**
- Make sure Root Directory is set to `frontend`
- Check that `VITE_API_URL` env var is added

---

*Built for BS IT Finals — Asia Pacific College*
