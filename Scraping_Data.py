from google_play_scraper import reviews, Sort
import pandas as pd

# Aplikasi yang akan di-scrape yaitu WhatsApp
app_id = 'com.whatsapp'

result, _ = reviews(
    app_id,
    lang='id',  # Bahasa Indonesia
    country='id',  # Indonesia
    sort=Sort.NEWEST,  # Urutkan dari terbaru
    count=3000  # Jumlah ulasan
)

reviews_df = pd.DataFrame(result)

reviews_df[['content', 'score']].to_csv('playstore_reviews.csv', index=False)

print("✅ Data ulasan berhasil disimpan!")