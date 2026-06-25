import sqlite3
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Initialize OpenAI Client
# Ensure OPENAI_API_KEY is set in your environment
client = OpenAI()

def setup_mock_database():
    """Creates a local SQLite database with some mock HR data."""
    conn = sqlite3.connect("mock_hr.db")
    cursor = conn.cursor()
    
    # Create Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            salary INTEGER,
            remote_status TEXT
        )
    """)
    
    # Insert Mock Data
    cursor.execute("DELETE FROM employees") # Clear previous data
    mock_data = [
        (1, "Alice Smith", "Data Engineering", 120000, "Remote"),
        (2, "Bob Jones", "Data Science", 110000, "Office"),
        (3, "Charlie Brown", "DevOps", 135000, "Remote"),
        (4, "Diana Prince", "Product", 95000, "Hybrid"),
        (5, "Evan Wright", "Data Engineering", 115000, "Remote")
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", mock_data)
    conn.commit()
    return conn

def generate_sql(natural_language_query: str) -> str:
    """Uses Prompt Engineering to convert English to SQL safely."""
    
    schema_context = """
    Table: employees
    Columns: id (INT), name (TEXT), department (TEXT), salary (INT), remote_status (TEXT)
    """
    
    # Notice the Defensive Prompting (Module 10) and Context Injection
    system_prompt = f"""
    Act as an SQLite query generator.
    Your ONLY job is to convert the User's English request into a valid SQL SELECT statement.
    
    Database Schema:
    {schema_context}
    
    SECURITY RULES:
    1. NEVER generate INSERT, UPDATE, DELETE, DROP, or ALTER statements.
    2. Output ONLY the raw SQL query. Do not wrap it in markdown blockquotes like ```sql.
    """
    
    print("🤖 [AI] Thinking and generating SQL...")
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", # Using a cheaper model for simple SQL
        temperature=0.0, # Zero creativity, purely factual (Module 01)
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": natural_language_query}
        ]
    )
    
    return response.choices[0].message.content.strip()

def run_app():
    print("🚀 Welcome to the NL2SQL AI Agent!")
    print("Setting up mock database 'mock_hr.db'...")
    conn = setup_mock_database()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY is not set in your environment.")
        print("Please export it or add it to a .env file to run this app.")
        return
        
    print("✅ System Ready.")
    print("-" * 50)
    
    while True:
        user_input = input("\n🗣️  Ask a question in English (or type 'exit'): ")
        
        if user_input.lower() in ['exit', 'quit']:
            break
            
        try:
            # 1. Generate SQL via LLM
            generated_sql = generate_sql(user_input)
            print(f"💻 [Generated SQL]: {generated_sql}")
            
            # 2. Security Check (Basic Client-Side validation to back up the LLM)
            if any(forbidden in generated_sql.upper() for forbidden in ["DROP", "DELETE", "UPDATE", "INSERT"]):
                print("🚨 [SECURITY ALERT] Destructive SQL detected and blocked!")
                continue
                
            # 3. Execute SQL
            cursor = conn.cursor()
            cursor.execute(generated_sql)
            results = cursor.fetchall()
            
            # 4. Display Results
            print("📊 [Results]:")
            for row in results:
                print(f"   -> {row}")
                
        except Exception as e:
            print(f"❌ [Error Executing Query]: {e}")
            
    conn.close()
    print("Goodbye! 👋")

if __name__ == "__main__":
    run_app()
