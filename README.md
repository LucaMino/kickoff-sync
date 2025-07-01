# kickoff-sync

**kickoff-sync** is a lightweight tool that automatically syncs your favorite football team’s upcoming matches to your Google Calendar.
It fetches match data from a reliable source and creates calendar events with key details such as date, opponent, venue, and optional reminders.

Whether you’re tracking your club’s domestic league or international competitions, kickoff-sync helps you stay organized and never miss a match.

---

## 🚀 Getting Started

### ⚙️ Configuration

1. Activate the **Google Calendar API** via [Google Cloud Console](https://console.cloud.google.com/).
2. Subscribe to **SofaScore API** on [RapidAPI](https://rapidapi.com/apidojo/api/sofascore) (Free 500/Month).

---

### 🧪 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/LucaMino/kickoff-sync
   cd kickoff-sync
2. Create `.env` from [.env.example](src/.env.example)
3. Build container
   ```sh
   docker-compose up -d --build
   ```

<!-- LICENSE -->
### License

Distributed under the MIT License. See `LICENSE.txt` for more information.


fly ssh console --app kickoff-sync