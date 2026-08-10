
# 🛡️ Roman Urdu Smishing Detector - AI for Pakistan

> **Can Machine Learning detect social engineering scams in Roman-Urdu SMS?**
> A-Level Research Project by Syed Sameel Uzzaman | Nixor College | 93.75% Accuracy

[![Accuracy](https://img.shields.io/badge/Accuracy-93.75%25-brightgreen)](https://github.com)
[![Dataset](https://img.shields.io/badge/Dataset-160%20Messages-blue)](https://github.com)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://github.com)
[![Model](https://img.shields.io/badge/Model-TF--IDF%20%2B%20Logistic%20Regression-orange)](https://github.com)

## 🚨 The Problem

Pakistan loses **$9.3B yearly** to digital scams (GASA 2025). PTA reported **150,000+ spam SMS** complaints in 2023.

Scammers exploit **Roman Urdu** - Urdu in Latin script with no standard spelling:
- `apka / aapka / ap ka` = same word
- `Bhai apka easypaisa account block ho gaya hai OTP bata dein`
- New 2025 **Approval Scam**: `Galti se 48500 bhej diye My Approvals me ja kar approve kar do` → Victim loses money by approving payment request.

English spam filters **FAIL** on this code-switched, phonetic language.

## 💡 Our Solution

Lightweight, deployable AI that understands Roman Urdu code-switching.

### Dataset (Novel Contribution)
- **160 balanced messages**: 80 SCAM + 80 HAM
- Categories:
  - Approval Scam (2025 novel): 30 msgs
  - OTP/Block Scam: 25 msgs
  - BISP/Ehsaas: 10 msgs
  - Lottery: 10 msgs
  - Fake Easypaisa Trx: 5 msgs
  - HAM (legit chats, real bank alerts): 80 msgs
- Source: Real user donations + 10 images of 2025 scams

### Model Pipeline
```
Raw SMS -> Lowercase -> TF-IDF (1,3)-grams, 8000 features -> Logistic Regression (C=10, balanced)
```

**Why not BERT?** Small dataset (160) + need mobile deployment. Logistic Regression gives 94% F1 with probability output.

### Results
- **Accuracy: 93.75% (30/32 correct)**
- Precision: 94% | Recall: 94% | F1: 0.94
- Confusion Matrix: TN=15, TP=15, FP=1, FN=1

#### Live Demo:
```
🔴 SCAM (83%) -> Bhai apka easypaisa account block ho gaya hai OTP bata dein
🔴 SCAM (82%) -> Bhai galti se 48500 My Approvals me approve kar do
🟢 HAM SAFE (89%) -> Yar kal milte hain chai peete hain
```

## 🚀 Try It Yourself

### 1. Clone & Install
```bash
git clone https://github.com/yourusername/roman-urdu-smishing-detector.git
pip install -r requirements.txt
```

### 2. Run Prediction
```python
import pickle

with open('roman_urdu_scam_model.pkl','rb') as f:
    model = pickle.load(f)
with open('roman_urdu_vectorizer.pkl','rb') as f:
    vectorizer = pickle.load(f)

msg = "Bhai apka easypaisa account block ho gaya OTP bata dein"
vec = vectorizer.transform([msg.lower()])
pred = model.predict(vec)[0]
prob = model.predict_proba(vec).max()
print("SCAM" if pred==1 else "HAM", f"{prob:.0%}")
```

### 3. Streamlit App
```bash
streamlit run app.py
```

## 📊 Files in this Repo
- `FINAL_THESIS_160_ROWS.xlsx` - Labeled dataset (text, label, category)
- `roman_urdu_scam_model.pkl` - Trained Logistic Regression
- `roman_urdu_vectorizer.pkl` - TF-IDF vectorizer
- `NIXOR_FINAL_Sameel_20280556.docx` - Full thesis
- `confusion_matrix.png`, `performance_chart.png`

## 🎓 Author
**Syed Sameel Uzzaman**
- A-Level Student, Nixor College, Karachi (2025-26)
- ID: 20280556
- Aspiring: Oxford/Cambridge/MIT/Imperial - Computer Science
- Focus: Low-resource NLP, Cybersecurity for Pakistan

## 📚 Citation
If you use this dataset:
```
Uzzaman, S.S. (2026). Roman Urdu Smishing Dataset 2025 - Pakistan (160 messages, Approval Scam included). Nixor College.
```

## 🔮 Future Work
- [ ] Expand to 1000+ messages
- [ ] Fine-tune XLM-RoBERTa + Roman Urdu normalization lexicon
- [ ] Deploy Android SMS filter app
- [ ] Integration with PTA reporting API

## 📄 License
MIT License - Free for research, please cite.

---
**Built for Pakistan, by a student from Karachi. Protecting Easypaisa/JazzCash users from evolving scams.**
