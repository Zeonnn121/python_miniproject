import sqlite3

# Sample question data including the additional 15 questions
questions = [
    {
        "question": "Which country celebrates the Day of the Dead (Día de los Muertos)?",
        "options": ["Spain", "Mexico", "Argentina", "Germany"],
        "answer": "Mexico",
        "explanation": "The Day of the Dead is a Mexican tradition that honors deceased loved ones with altars, offerings, and celebrations."
    },
    {
        "question": "Where is Machu Picchu located?",
        "options": ["India", "Peru", "Egypt", "China"],
        "answer": "Peru",
        "explanation": "Machu Picchu is a 15th-century Incan citadel situated in the Andes Mountains of Peru."
    },
    {
        "question": "Which city is the Colosseum in?",
        "options": ["Athens", "Rome", "Paris", "London"],
        "answer": "Rome",
        "explanation": "The Colosseum, also known as the Flavian Amphitheatre, is a historical arena located in Rome, Italy."
    },
    {
        "question": "Which temple in Odisha is known for its architectural brilliance and massive chariot structure?",
        "options": ["BRIHADESHWARA TEMPLE", "KONARK SUN TEMPLE", "DEVI TEMPLE", "KRISHNA TEMPLE"],
        "answer": "KONARK SUN TEMPLE",
        "explanation": "The Konark Sun Temple is an iconic 13th-century temple in Odisha, built in the shape of a giant chariot."
    },
    {
        "question": "In which country is it customary to give a pair of chopsticks as a wedding gift?",
        "options": ["China", "Russia", "South Korea", "India"],
        "answer": "China",
        "explanation": "In Chinese tradition, a pair of chopsticks symbolizes harmony and partnership, making it a popular wedding gift."
    },
    # Additional 15 questions related to cultural heritage
    {
        "question": "Which country is known for its traditional tea ceremony?",
        "options": ["Japan", "China", "India", "England"],
        "answer": "Japan",
        "explanation": "The Japanese tea ceremony is a cultural activity involving the ceremonial preparation and consumption of matcha, a powdered green tea."
    },
    {
        "question": "Where is the Great Wall located?",
        "options": ["India", "China", "Russia", "Mongolia"],
        "answer": "China",
        "explanation": "The Great Wall of China is a series of fortifications built along the northern borders of China to protect against invasions."
    },
    {
        "question": "Which city is known for the ancient pyramids?",
        "options": ["Cairo", "Athens", "Rome", "Paris"],
        "answer": "Cairo",
        "explanation": "Cairo is the capital city of Egypt, home to the Pyramids of Giza, one of the Seven Wonders of the Ancient World."
    },
    {
        "question": "What is the famous cultural heritage site in India known for its white marble architecture?",
        "options": ["Red Fort", "Taj Mahal", "Qutub Minar", "Gateway of India"],
        "answer": "Taj Mahal",
        "explanation": "The Taj Mahal, located in Agra, India, is a beautiful white marble mausoleum built by Mughal Emperor Shah Jahan in memory of his wife Mumtaz Mahal."
    },
    {
        "question": "Which of these is a UNESCO World Heritage Site in the United States?",
        "options": ["Yellowstone National Park", "Grand Canyon", "Statue of Liberty", "All of the above"],
        "answer": "All of the above",
        "explanation": "Yellowstone, the Grand Canyon, and the Statue of Liberty are all UNESCO World Heritage Sites, each representing cultural and natural heritage."
    },
    {
        "question": "In which country is the cultural event 'Carnival' celebrated with parades and dances?",
        "options": ["Brazil", "Argentina", "Spain", "Italy"],
        "answer": "Brazil",
        "explanation": "Carnival in Brazil is a world-famous festival celebrated before Lent with vibrant parades, music, and samba dancing."
    },
    {
        "question": "Where is the historic city of Petra located?",
        "options": ["Egypt", "Jordan", "Turkey", "Greece"],
        "answer": "Jordan",
        "explanation": "Petra, an archaeological site in Jordan, is known for its rock-cut architecture and water conduit system. It was once the capital of the Nabataean Kingdom."
    },
    {
        "question": "Which country is famous for the cultural event known as 'Diwali'?",
        "options": ["India", "China", "Nepal", "Bangladesh"],
        "answer": "India",
        "explanation": "Diwali, also known as the Festival of Lights, is a major Hindu festival celebrated across India with fireworks, sweets, and prayers to the goddess Lakshmi."
    },
    {
        "question": "Which ancient civilization built the Machu Picchu?",
        "options": ["Mayan", "Inca", "Aztec", "Egyptian"],
        "answer": "Inca",
        "explanation": "Machu Picchu was built by the Inca civilization in the 15th century as an estate for the Inca emperor Pachacuti."
    },
    {
        "question": "Where is the Angkor Wat temple complex located?",
        "options": ["India", "Cambodia", "Thailand", "Vietnam"],
        "answer": "Cambodia",
        "explanation": "Angkor Wat, located in Cambodia, is a large temple complex built by the Khmer Empire in the early 12th century."
    },
    {
        "question": "Which country is home to the famous Machu Picchu site?",
        "options": ["Peru", "Chile", "Mexico", "Colombia"],
        "answer": "Peru",
        "explanation": "Machu Picchu is a 15th-century Incan citadel located in the Andes Mountains of Peru, often called the Lost City of the Incas."
    },
    {
        "question": "Which famous monument is located in Paris, France?",
        "options": ["Eiffel Tower", "Statue of Liberty", "Colosseum", "Big Ben"],
        "answer": "Eiffel Tower",
        "explanation": "The Eiffel Tower, built in 1889, is a wrought-iron lattice tower located in Paris, France, and a symbol of French cultural heritage."
    },
    {
        "question": "Which ancient landmark is known as the symbol of ancient Greek civilization?",
        "options": ["Great Wall of China", "Parthenon", "Pyramids of Giza", "Colosseum"],
        "answer": "Parthenon",
        "explanation": "The Parthenon is an ancient Greek temple located on the Acropolis of Athens, dedicated to the goddess Athena."
    },
]

# Connect to the SQLite database
conn = sqlite3.connect("questions.db")
cursor = conn.cursor()

# Insert question data into the table
for q in questions:
    cursor.execute("""
        INSERT INTO questions (question, option1, option2, option3, option4, answer, explanation)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (q["question"], q["options"][0], q["options"][1], q["options"][2], q["options"][3], q["answer"], q["explanation"]))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Questions have been added to the database.")
