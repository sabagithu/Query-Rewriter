**📌 Query Rewriter with Personalization and Evaluation**

🧠 **Overview**
This project implements a personalized query rewriting pipeline using synthetic data enriched with user profiles. It evaluates rewritten queries using ROUGE-L and BERTScore, and includes a Streamlit interface for interactive exploration.

📁** Dataset Description**
The dataset synthetic_queries_dataset.csv contains synthetic user queries and their rewritten versions, structured to simulate personalization. Each row includes:
<img width="873" height="523" alt="image" src="https://github.com/user-attachments/assets/717f3dac-abbb-4d49-acfc-2196edcab51b" />
This synthetic dataset is designed for controlled evaluation and explainability in query rewriting tasks.


📐 **Assumptions**
- User profiles are complete and consistent across rows
- Rewriting logic adapts based on interests, location, and device context
- Evaluation metrics are computed per query and averaged across the dataset
- Synthetic data approximates real-world personalization scenarios

⚙️ **Setup Instructions**
- Clone the repository:
git clone https://github.com/sabagithu/Query-Rewriter.git
cd Query-Rewriter


- Install dependencies:
pip install -r requirements.txt


- Run the Streamlit app:
streamlit run app.py

📊 **Evaluation Summary**
<img width="870" height="191" alt="image" src="https://github.com/user-attachments/assets/43dca02d-09c2-4266-bc16-9cfcd2015b1b" />
Evaluation scripts are included in evaluation.py. Scores are computed using HuggingFace’s bert-score and rouge-score libraries.


📓** Jupyter Notebook (Optional)**
The notebook Query.ipynb demonstrates:
- Dataset preview and schema validation
- Query rewriting logic
- Evaluation metric computation
- Sample outputs and score interpretation

📜 **License**
This project is licensed under the MIT License. See LICENSE for details.

