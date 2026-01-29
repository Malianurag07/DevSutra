# DevSutra "Forever Free" Deployment Guide

You have requested a **completely free** hosting solution. Since Netlify is static-first and does not host persistent databases (like SQLite) or traditional Django servers, we will use the best "Free Tier" combo in the industry:

1.  **Frontend**: **Netlify** (Free, Global CDN, fast)
2.  **Backend & Database**: **PythonAnywhere** (Free, supports Django + SQLite natively)

### 💾 About the Database
We are using **SQLite**. 
*   **Where is it?** It is a file (`db.sqlite3`) that lives directly on your PythonAnywhere server.
*   **Cost?** Free (included with your PythonAnywhere account).
*   **Setup?** Automatic. The `python manage.py migrate` command creates it for you.

---

## Part 1: Push Changes to GitHub

I have created a `netlify.toml` file to help Netlify understand your frontend.

```bash
git add .
git commit -m "Setup for Netlify and PythonAnywhere"
git push origin main
```

---

## Part 2: Deploy Backend (PythonAnywhere)

PythonAnywhere gives you a free server forever.

1.  **Sign Up**: Go to [www.pythonanywhere.com](https://www.pythonanywhere.com/) and create a "Beginner" (Free) account.
2.  **Open Bash Console**: On your Dashboard, click **"$ Bash"**.
3.  **Clone Your Code**:
    ```bash
    git clone https://github.com/Malianurag07/DevSutra.git
    cd DevSutra
    ```
4.  **Create Virtual Environment**:
    ```bash
    mkvirtualenv --python=/usr/bin/python3.10 mysite
    pip install -r requirements.txt
    ```
    *(Note: If `mkvirtualenv` doesn't work, run `python3 -m venv venv` and `source venv/bin/activate`)*

5.  **Run Migrations**:
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    python generate_problems.py
    python manage.py import_problems
    ```

6.  **Configure Web App**:
    *   Go to the **Web** tab.
    *   Click **Add a new web app**.
    *   Select **Manual Configuration** -> **Python 3.10**.
    *   **Source code section**: Enter path `/home/yourusername/DevSutra`.
    *   **WSGI configuration file**: Click the link to edit it. Delete everything and paste this:
        ```python
        import os
        import sys

        path = '/home/yourusername/DevSutra'
        if path not in sys.path:
            sys.path.append(path)

        os.environ['DJANGO_SETTINGS_MODULE'] = 'dev_backend.settings'

        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        ```
        *(Replace `yourusername` with your actual PythonAnywhere username)*.

7.  **Get Your Backend URL**:
    *   It will be `https://yourusername.pythonanywhere.com`.
    *   **Keep this URL safe**.

---

## Part 3: Deploy Frontend (Netlify)

1.  **Sign Up**: Go to [netlify.com](https://www.netlify.com/) and sign up with GitHub.
2.  **Import Project**: Click **"Add new site"** -> **"Import from Git"**.
3.  **Connect GitHub**: Authorize and select `Malianurag07/DevSutra`.
4.  **Build Settings** (It should auto-detect thanks to `netlify.toml`):
    *   **Base directory**: `frontend`
    *   **Build command**: `npm run build`
    *   **Publish directory**: `.next`
5.  **Environment Variables**:
    *   Click **"Add environment variable"**.
    *   `NEXT_PUBLIC_API_URL`: Paste your PythonAnywhere URL (e.g., `https://yourusername.pythonanywhere.com`).
    *   `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`: Your Clerk Key.
    *   `CLERK_SECRET_KEY`: Your Clerk Secret.
6.  **Deploy**: Click **"Deploy site"**.

---

## Part 4: Final Connection

1.  **Update Clerk**:
    *   Go to Clerk Dashboard -> Domains.
    *   Add your new **Netlify URL** (e.g., `https://devsutra.netlify.app`) as an allowed origin.

2.  **Update Backend CORS (PythonAnywhere)**:
    *   Go to PythonAnywhere -> Files.
    *   Edit `dev_backend/settings.py`.
    *   Update `CORS_ALLOWED_ORIGINS` to include your Netlify URL:
        ```python
        CORS_ALLOWED_ORIGINS = [
            "https://your-site-name.netlify.app",
        ]
        ```
    *   Go to **Web** tab and click **Reload**.

🎉 **Done! completely Free Hosting.**
