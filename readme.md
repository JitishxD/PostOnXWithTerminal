# X Auto Poster on Twitter using terminal

A straightforward automation script used to  post X (Formerly Twitter) updaing the daily progress of your challenge!

---

## Needs

- Python 3.8+ 
- `pip install tweepy python-dotenv`

---

## 🔑 Configuration — Produce Keys and Tokens

1. Visit this link: https://developer.x.com/en/portal/dashboard
2. Establish a **Project** → Make a **App**
3. In the **User authentication settings** section:
   - App type → `Web App, Automated App, or Bot` - App permissions → `Read and Write`
   - Callback URL → `https://localhost`
   - Save modifications - Website URL → `https://example.com` (or any URL)
4. Select the **Keys and Tokens** tab.
5. Produce **these four values**:
   **API Key** - **API Key Secret** - **Access Token** - **Access Token Secret**

> _Note:_ If Access Token & Secret are not visible, ensure step 3 is saved.

---

## 🔧 Environment Variables

Create a `.env` file in the project root see `sample.env`

---

## 🧪 Run Script

```sh
python main.py
```
