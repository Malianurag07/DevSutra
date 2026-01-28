# DevSutra Deployment Guide

This guide will help you deploy DevSutra to Vercel (Frontend) and your choice of platform for the Django backend.

## 🚀 Quick Deployment Overview

### Frontend (Next.js) → Vercel
### Backend (Django) → Railway/Render/PythonAnywhere (Choose one)

---

## Part 1: Deploy Frontend to Vercel

### Step 1: Prepare Your Repository

Your code is already on GitHub at `https://github.com/Malianurag07/DevSutra`

### Step 2: Sign Up/Login to Vercel

1. Go to [vercel.com](https://vercel.com)
2. Click "Sign Up" or "Login"
3. Choose "Continue with GitHub"
4. Authorize Vercel to access your GitHub repositories

### Step 3: Import Your Project

1. Click "Add New..." → "Project"
2. Find and select your `DevSutra` repository
3. Vercel will auto-detect it's a Next.js project

### Step 4: Configure Project Settings

**IMPORTANT:** Since your Next.js app is in the `frontend` folder, configure:

- **Framework Preset**: Next.js
- **Root Directory**: `frontend` ⚠️ (MUST SET THIS!)
- **Build Command**: `npm run build` (auto-detected)
- **Output Directory**: `.next` (auto-detected)
- **Install Command**: `npm install` (auto-detected)

### Step 5: Add Environment Variables

In Vercel project settings, add these environment variables:

#### Required for Clerk Authentication:
```
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=your_clerk_publishable_key
CLERK_SECRET_KEY=your_clerk_secret_key
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
```

#### Backend API URL (will add after backend deployment):
```
NEXT_PUBLIC_API_URL=your_backend_url_here
```

**To get Clerk keys:**
1. Go to [clerk.com](https://clerk.com)
2. Sign in and navigate to your dashboard
3. Create a new application or use existing one
4. Copy the API keys from the dashboard

### Step 6: Deploy

1. Click "Deploy"
2. Wait 2-3 minutes for the build to complete
3. Your frontend will be live at `https://your-project-name.vercel.app`

---

## Part 2: Deploy Django Backend

You have several options for deploying the Django backend:

### Option A: Railway (Recommended - Easy & Free Tier)

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your `DevSutra` repository
5. Add environment variables:
   ```
   DJANGO_SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-railway-domain.railway.app
   DATABASE_URL=postgresql://... (Railway provides this)
   ```
6. Railway will auto-detect Django and deploy

### Option B: Render

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Create new "Web Service"
4. Connect your `DevSutra` repository
5. Configure:
   - **Root Directory**: Leave empty (root)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn DevSutra.wsgi:application`
6. Add environment variables (same as Railway)

### Option C: PythonAnywhere (Free but requires manual setup)

Follow their Django deployment guide at [help.pythonanywhere.com](https://help.pythonanywhere.com)

---

## Part 3: Connect Frontend to Backend

### Step 1: Get Your Backend URL

After deploying Django, you'll get a URL like:
- Railway: `https://devsutra-production.up.railway.app`
- Render: `https://devsutra.onrender.com`

### Step 2: Update Vercel Environment Variables

1. Go to your Vercel project
2. Settings → Environment Variables
3. Update `NEXT_PUBLIC_API_URL` with your backend URL
4. Redeploy the frontend

### Step 3: Update Django CORS Settings

In your `settings.py`, update:
```python
CORS_ALLOWED_ORIGINS = [
    "https://your-vercel-app.vercel.app",
]
```

Push changes to GitHub and redeploy.

---

## Part 4: Update Frontend API Calls

Currently, your frontend uses `http://127.0.0.1:8000` for API calls.

You need to update this to use the environment variable:

```typescript
// Instead of: fetch('http://127.0.0.1:8000/api/problems/')
// Use:
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';
fetch(`${API_URL}/api/problems/`)
```

---

## Deployment Checklist

### Before Deploying:
- [ ] GitHub repository is up to date
- [ ] All sensitive data is in environment variables
- [ ] Frontend API calls use environment variables
- [ ] Django has CORS configured
- [ ] requirements.txt is complete

### Frontend (Vercel):
- [ ] Set Root Directory to `frontend`
- [ ] Add Clerk environment variables
- [ ] Deploy and verify build succeeds
- [ ] Custom domain (optional)

### Backend:
- [ ] Deploy to Railway/Render
- [ ] Add environment variables
- [ ] Run migrations
- [ ] Import problems data
- [ ] Test API endpoints

### Final:
- [ ] Update frontend with backend URL
- [ ] Test authentication flow
- [ ] Test problem loading
- [ ] Verify all features work

---

## Troubleshooting

### Build Fails on Vercel
- Check Root Directory is set to `frontend`
- Verify all dependencies in package.json
- Check build logs for specific errors

### API Not Connecting
- Verify CORS settings in Django
- Check environment variable is set correctly
- Ensure backend is running and accessible

### Clerk Authentication Issues
- Verify all Clerk keys are set
- Add Vercel domain to Clerk allowed origins
- Check Clerk dashboard for errors

---

## Useful Commands

```bash
# Test production build locally
cd frontend
npm run build
npm start

# Django production checklist
python manage.py check --deploy

# Create Django superuser (on production)
python manage.py createsuperuser
```

---

## Next Steps After Deployment

1. Add custom domain to Vercel (optional)
2. Set up monitoring and analytics
3. Configure HTTPS for backend
4. Set up automated backups for database
5. Add CI/CD pipeline for automatic deployments

---

**Need Help?** Check Vercel and Railway documentation or open an issue on GitHub.
