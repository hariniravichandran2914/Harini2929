import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_data():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        products = []
        
        # Select the container for each book
        for item in soup.select(".product_pod"):
            # Get the book title
            name = item.select_one("h3 a").get("title", "N/A")
            # Get the price
            price = item.select_one(".price_color").get_text(strip=True) if item.select_one(".price_color") else "N/A"
            # Get the rating (this will give a class name, map it to a readable rating)
            rating_class = item.select_one("p")["class"][1] if item.select_one("p") else "N/A"
            rating_map = {
                'One': '1/5',
                'Two': '2/5',
                'Three': '3/5',
                'Four': '4/5',
                'Five': '5/5'
            }
            rating = rating_map.get(rating_class, "N/A")
            
            products.append({"Name": name, "Price": price, "Rating": rating})
        
        if not products:
            messagebox.showinfo("Result", "No products found. Please check the URL or website structure.")
            return
        
        # Save data to CSV
        df = pd.DataFrame(products)
        df.to_csv("products.csv", index=False)
        messagebox.showinfo("Success", "Data extracted and saved to products.csv.")
    
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve data: {e}")

# GUI setup
root = tk.Tk()
root.title("E-commerce Product Scraper")

tk.Label(root, text="Enter the URL of the e-commerce website:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

scrape_button = tk.Button(root, text="Extract and Save to CSV", command=extract_data)
scrape_button.pack(pady=20)

root.mainloop()










