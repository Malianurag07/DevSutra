# 🚀 Quick Start Guide: Deploy DevSutra to Vercel

Your project is ready for deployment! Follow these steps to get DevSutra live on Vercel.

---

## ✅ What's Been Done

- ✅ Updated all API calls to use environment variables
- ✅ Created comprehensive deployment documentation
- ✅ Added Vercel configuration file
- ✅ Committed and pushed all changes to GitHub
- ✅ Created environment variable template

---

## 📋 Step-by-Step Deployment

### **Step 1: Sign Up on Vercel** (2 minutes)

1. Go to [vercel.com](https://vercel.com)
2. Click **"Sign Up"**
3. Choose **"Continue with GitHub"**
4. Authorize Vercel to access your GitHub

### **Step 2: Import Your Project** (1 minute)

1. Click **"Add New..."** → **"Project"**
2. Find **"DevSutra"** in your repository list
3. Click **"Import"**

### **Step 3: Configure Build Settings** (3 minutes)

⚠️ **CRITICAL:** Since your Next.js app is in the `frontend` folder:

```
Framework Preset: Next.js
Root Directory: frontend  ⭐ MUST SET THIS!
Build Command: npm run build
Output Directory: .next
Install Command: npm install
```

### **Step 4: Add Environment Variables** (5 minutes)

In the Vercel project settings, add:

#### For Clerk (Authentication):
```env
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...
```

**Get Clerk Keys:**
1. Go to [clerk.com](https://clerk.com) → Sign Up/Login
2. Create new application (or use existing)
3. Dashboard → API Keys
4. Copy both keys above

#### For Backend API (add after backend is deployed):
```env
NEXT_PUBLIC_API_URL=https://your-backend-url.com
```

### **Step 5: Deploy!** (2-3 minutes)

1. Click **"Deploy"**
2. Wait for build to complete
3. Your site will be live at: `https://your-project.vercel.app`

---

## 🐍 Deploy Backend (Choose One)

### Option A: Railway (Recommended - Easiest)

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. **"New Project"** → **"Deploy from GitHub repo"**
4. Select `DevSutra`
5. Add environment variables:
   ```env
   DEBUG=False
   ALLOWED_HOSTS=your-railway-url.railway.app
   ```
6. Railway auto-deploys! ✅

### Option B: Render

1. Go to [render.com](https://render.com)
2. **"New"** → **"Web Service"**
3. Connect `DevSutra` repo
4. **Build Command:** `pip install -r requirements.txt`
5. **Start Command:** `gunicorn DevSutra.wsgi:application`
6. Add same environment variables as Railway

---

## 🔗 Connect Frontend to Backend

### After Backend is Deployed:

1. Copy your backend URL (e.g., `https://devsutra.up.railway.app`)
2. Go to Vercel → Project → **Settings** → **Environment Variables**
3. Add/Update:
   ```env
   NEXT_PUBLIC_API_URL=https://devsutra.up.railway.app
   ```
4. Go to **Deployments** → Click **"..."** → **"Redeploy"**

### Update Django CORS:

In your `settings.py`, add:
```python
CORS_ALLOWED_ORIGINS = [
    "https://your-vercel-url.vercel.app",
]
```

Commit and push to GitHub, Railway/Render will auto-deploy.

---

## 🎯 Final Checklist

- [ ] Frontend deployed to Vercel
- [ ] Clerk keys added and authentication works
- [ ] Backend deployed (Railway/Render)
- [ ] Backend URL added to Vercel environment variables
- [ ] CORS configured in Django
- [ ] Frontend redeployed with backend URL
- [ ] Test authentication flow
- [ ] Test loading problems from all levels
- [ ] Test code execution

---

## 🆘 Troubleshooting

### Build Fails
- **Check:** Root Directory is set to `frontend`
- **Check:** All dependencies in `package.json`
- **View:** Build logs for errors

### Can't Sign In
- **Check:** Clerk keys are correct
- **Check:** Vercel domain added to Clerk allowed origins

### API Not Loading
- **Check:** `NEXT_PUBLIC_API_URL` environment variable
- **Check:** Backend is running and accessible
- **Check:** CORS settings in Django

---

## 📚 Next Steps After Deployment

1. **Custom Domain:** Add your own domain in Vercel settings
2. **Analytics:** Enable Vercel Analytics
3. **Monitoring:** Set up error tracking (Sentry)
4. **Database:** Migrate from SQLite to PostgreSQL for production
5. **Backups:** Set up automated database backups

---

## 📖 Full Documentation

For detailed instructions, see: [DEPLOYMENT.md](./DEPLOYMENT.md)

---

**You're all set!** 🎉 Your DevSutra project is deployment-ready.

Questions? Check the [DEPLOYMENT.md](./DEPLOYMENT.md) file for comprehensive docs.
