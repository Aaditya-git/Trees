from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

pdf_path = "CSE539_F25_Midterm_Theoretical_Solutions_Aaditya_Bhilegaonkar.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
styles = getSampleStyleSheet()

title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], alignment=1, spaceAfter=20)
q_style = ParagraphStyle('QStyle', parent=styles['Heading3'], spaceAfter=6, fontSize=12)
a_style = ParagraphStyle('AStyle', parent=styles['BodyText'], spaceAfter=12, fontSize=11, leading=15)

story = []

story.append(Paragraph("Arizona State University", title_style))
story.append(Paragraph("CSE 539: Applied Cryptography — Fall 2025", styles['Heading2']))
story.append(Spacer(1, 10))
story.append(Paragraph("<b>Midterm Exam — Theoretical Questions (Part 1)</b>", styles['Heading2']))
story.append(Spacer(1, 20))
story.append(Paragraph("<b>Name:</b> Aaditya Bhilegaonkar", styles['Normal']))
story.append(Paragraph("<b>ASU ID:</b> 1233563489", styles['Normal']))
story.append(Spacer(1, 20))
story.append(Paragraph("This document contains complete, proof-based solutions for all seven theoretical questions from the CSE539 Fall 2025 Midterm Exam.", styles['Normal']))
story.append(PageBreak())

answers = [
("Question 1: OTP (2OTP)",
"Encryption: c = k2 ⊕ (k1 ⊕ m). (1) If k1 = k2 and m = 1001, then c = (k2 ⊕ k1) ⊕ m = 0 ⊕ m = 1001. "
"Thus, c = 1001. (2) Let s = k1 ⊕ k2. Since c1 = s ⊕ m1 = 1011 ⊕ 1001 = 0010, flipping both keys gives ¬s = 1101. "
"Then c2 = ¬s ⊕ m2 = 1101 ⊕ 1100 = 0001. Hence, the ciphertext is 0001."),

("Question 2: Shamir Secret Sharing",
"The secret is m = 5 mod 13 with threshold t = 3 (degree 2 polynomial). Let f(x) = ax² + bx + 5. "
"From the shares (1,8), (2,2), (3,0): a + b ≡ 3, 4a + 2b ≡ 10, 9a + 3b ≡ 8 mod 13. "
"Solving gives a = 2, b = 1. Thus f(4) = 2×16 + 4 + 5 = 41 ≡ 2 mod 13. The 4th share is (4,2)."),

("Question 3: MAC Insecurity",
"Given t1 = F(k, m2), t2 = F(k, m2 ⊕ m1), t3 = F(k, m1). "
"If an adversary knows a valid tag (t1, t2, t3) for (m1, m2), they can produce (t3, t2, t1) as a valid tag for (m2, m1) "
"because F(k, m1) = t3, F(k, m1 ⊕ m2) = t2, and F(k, m2) = t1. Hence, the MAC is insecure under forgery."),

("Question 4: Hash Function Collision",
"Let c1 = F(k, m1), c2 = F(k, m2 ⊕ c1), c3 = F(k, m3 ⊕ c2). Pick m1′ ≠ m1 and compute c1′ = F(k, m1′). "
"Let x = F⁻¹(k, c2) and set m2′ = x ⊕ c1′. Then c2′ = F(k, m2′ ⊕ c1′) = F(k, x) = c2. "
"Keeping m3′ = m3 gives c3′ = F(k, m3′ ⊕ c2′) = F(k, m3 ⊕ c2) = c3. Thus, (m1, m2, m3) and (m1′, m2′, m3′) form a collision."),

("Question 5: DHKE with Related Exponents",
"For instance i, a_i = a + 2i − 1 and b_i = b + 3i − 1. Observing A_i = g^{a_i}, B_i = g^{b_i}, Eve finds g^a = A1/g, g^b = B1/g². "
"Given K3 = g^{(a+5)(b+8)} = g^{ab}g^{8a}g^{5b}g^{40}, she computes g^{ab} = K3 / (g^{8a} g^{5b} g^{40}). "
"Then, K_i = g^{a_i b_i} = g^{ab} g^{(3i−1)a} g^{(2i−1)b} g^{(2i−1)(3i−1)}, enabling computation of all K₁, K₂, K₄, K₅."),

("Question 6: DHKE Variant (Alice Deriving Bob’s Key)",
"Alice sends X = g^x; Bob sends Y = X^{y+z} = g^{x(y+z)} and sets k = g^{y+z}. "
"Alice knows x and computes its modular inverse x⁻¹ mod q. She then calculates k = Y^{x⁻¹} mod p, "
"obtaining the same key value as Bob."),

("Question 7: RSA Factoring from (N, δ)",
"Given N = pq and δ = |p² − 2q|, if p² ≥ 2q, then 2q = p² − δ ⇒ p³ − δp − 2N = 0; otherwise, 2q = p² + δ ⇒ p³ + δp − 2N = 0. "
"Since p ≈ (2N)^{1/3}, test integers near ⌊(2N)^{1/3}⌉ for both cubics x³ ± δx − 2N = 0. "
"The correct p divides N; then q = N/p. This allows efficient factorization using standard integer arithmetic.")
]

for q, a in answers:
    story.append(Paragraph(f"<b>{q}</b>", q_style))
    story.append(Paragraph(a, a_style))
    story.append(PageBreak())

doc.build(story)
print("PDF created successfully as:", pdf_path)
