# MRC x SULAV FF — Setup Guide

## Project Structure

```
sulavxmrc/
├── api/
│   ├── like.py          ← Like API: GET /like?uid=&region=
│   ├── webhook.py       ← Telegram webhook receiver
│   ├── set_webhook.py   ← Register webhook with Telegram
│   └── delete_webhook.py← Remove webhook (for polling mode)
├── like-accs/
│   └── accs_bd.json     ← BD region bot accounts
├── static/
│   └── index.html       ← Professional website
├── bot.py               ← Full Telegram bot logic
├── MajoRLoGinrEq_pb2.py ← Protobuf: MajorLogin request
├── MajoRLoGinrEs_pb2.py ← Protobuf: MajorLogin response
├── PlayerPersonalShow_pb2.py ← Protobuf: Player info
├── requirements.txt     ← Python dependencies
├── vercel.json          ← Vercel deployment config
├── bot_data.json        ← Bot state (auto-created)
├── .env.example         ← Example environment variables
└── .vercelignore        ← Files to ignore on Vercel
```

## Vercel Deployment Steps

### 1. Import to Vercel
- Go to https://vercel.com/new
- Import this folder (or drag & drop the ZIP)
- Framework preset: **Other**

### 2. Set Environment Variables
In Vercel dashboard → Project → Settings → Environment Variables:

| Variable | Value |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Your bot token from @BotFather |
| `SHRINK_API` | Your ShrinkEarn API key |
| `SUPER_ADMINS` | Comma-separated Telegram user IDs |
| `ALLOWED_GROUP_IDS` | Comma-separated group IDs (with - prefix) |
| `REDIRECT_LINK` | Your Telegram channel URL |
| `OWNERS` | Credit line shown in bot messages |

### 3. Deploy
Click **Deploy**. Wait for build to finish.

### 4. Register Webhook
Visit once after deploy:
```
https://YOUR-DOMAIN.vercel.app/api/set_webhook
```
You should see: `{"ok": true, "webhook_set": "..."}`

### 5. Use the Like API
```
GET https://YOUR-DOMAIN.vercel.app/like?uid=3074306062&region=BD
```

Response:
```json
{
  "name": "PlayerName",
  "uid": "3074306062",
  "LikesBefore": "1500",
  "LikeAfter": "1523",
  "LikesAddedByMrcSulav": "23",
  "status": "success"
}
```

## Bot Commands

### User Commands
- `/like <region> <uid>` — Send likes
- `/visits <region> <uid>` — Send visits  
- `/spam <region> <uid>` — Send friend requests
- `/info <region> <uid>` — View player info
- `/ping` — Check bot status
- `/help` — Full command list

### Admin Commands
- `/admin` — Open admin control panel
- `/autolike <region> <uid> <days>` — Schedule daily likes
- `/autovisit <region> <uid> <days>` — Schedule daily visits
- `/autospam <region> <uid> <days>` — Schedule daily spam
- `/autolist` — List active tasks
- `/autocancel <task_id>` — Cancel a task
- `/autostatus` — Detailed task status
- `/ban <id> [reason]` — Ban user
- `/unban <id>` — Unban user
- `/warn <id> [reason]` — Warn user (3 = auto-ban)
- `/clear_warnings <id>` — Clear warnings
- `/maintenance on|off` — Toggle maintenance
- `/setlimit <n>` — Set daily limit (1-10000)
- `/broadcast <message>` — Broadcast to groups
- `/stats` — Full bot statistics

## Supported Regions
- `BD` — Bangladesh
- `SG` — Singapore
- `IND` — India
- `EU` — Europe (uses SG accounts)

## Adding More Accounts

Add JSON files in `like-accs/` folder:
- `accs_bd.json` → BD region
- `accs_sg.json` → SG/EU region
- `accs_ind.json` → IND region

Format:
```json
[
  {"uid": "4637056719", "password": "YOUR_PASSWORD_HEX"},
  {"uid": "4637184606", "password": "YOUR_PASSWORD_HEX"}
]
```

## Credits
Built by **@MRCxCheats** and **@sulav_codex_ff**
Channel: https://t.me/SulavXMRCLIKES
